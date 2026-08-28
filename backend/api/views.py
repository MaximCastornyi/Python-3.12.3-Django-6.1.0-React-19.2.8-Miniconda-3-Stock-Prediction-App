import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from django.conf import settings
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StockPredictionSerializer
from .utils import save_plot

# Путь к файлу модели в папке Resources (поднимаемся из backend в корень)
MODEL_PATH = os.path.join(settings.BASE_DIR.parent, 'Resources', 'stock_prediction_model.keras')

# Загружаем модель 1 раз при старте сервера
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    model = None
    print(f" Ошибка загрузки модели: {e}")


class StockPredictionAPIView(APIView):
    def post(self, request):
        serializer = StockPredictionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if model is None:
            return Response(
                {"error": f"Файл модели не найден по пути: {MODEL_PATH}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        ticker = serializer.validated_data['ticker']

        # 1. Загрузка данных через yfinance
        now = datetime.now()
        start = datetime(now.year - 10, now.month, now.day)
        end = now
        df = yf.download(ticker, start, end)

        if df.empty:
            return Response(
                {"error": "No data found for the given ticker."},
                status=status.HTTP_404_NOT_FOUND
            )

        df = df.reset_index()

        # Безопасное извлечение Close (защита от MultiIndex)
        if isinstance(df.columns, pd.MultiIndex):
            close_prices = df['Close'].iloc[:, 0]
        else:
            close_prices = df['Close']

        # 2. Генерация графиков
        plt.switch_backend('AGG')

        # Базовый график цен
        plt.figure(figsize=(12, 5))
        plt.plot(close_prices, label='Closing Price')
        plt.title(f'Closing price of {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plot_img = save_plot(f'{ticker}_plot.png')
        plt.close()

        # 100 DMA
        ma100 = close_prices.rolling(100).mean()
        plt.figure(figsize=(12, 5))
        plt.plot(close_prices, label='Closing Price')
        plt.plot(ma100, 'r', label='100 DMA')
        plt.title(f'100 Days Moving Average of {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plot_100_dma = save_plot(f'{ticker}_100_dma.png')
        plt.close()

        # 200 DMA
        ma200 = close_prices.rolling(200).mean()
        plt.figure(figsize=(12, 5))
        plt.plot(close_prices, label='Closing Price')
        plt.plot(ma100, 'r', label='100 DMA')
        plt.plot(ma200, 'g', label='200 DMA')
        plt.title(f'200 Days Moving Average of {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plot_200_dma = save_plot(f'{ticker}_200_dma.png')
        plt.close()

        # 3. Подготовка данных для предсказания
        train_size = int(len(close_prices) * 0.7)
        data_training = pd.DataFrame(close_prices[0:train_size])
        data_testing = pd.DataFrame(close_prices[train_size:])

        # Обучаем Scaler ТОЛЬКО на тренировочной выборке (чтобы избежать Data Leakage)
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(data_training)

        past_100_days = data_training.tail(100)
        final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
        input_data = scaler.transform(final_df)

        x_test, y_test = [], []
        for i in range(100, input_data.shape[0]):
            x_test.append(input_data[i - 100:i])
            y_test.append(input_data[i, 0])

        x_test, y_test = np.array(x_test), np.array(y_test)

        # 4. Прогнозирование
        y_predicted = model.predict(x_test)

        # Денормализация (возврат к оригинальным ценам)
        y_predicted = scaler.inverse_transform(y_predicted.reshape(-1, 1)).flatten()
        y_test = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()

        # График предсказаний
        plt.figure(figsize=(12, 5))
        plt.plot(y_test, 'b', label='Original Price')
        plt.plot(y_predicted, 'r', label='Predicted Price')
        plt.title(f'Final Prediction for {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plot_prediction = save_plot(f'{ticker}_final_prediction.png')
        plt.close()

        # 5. Оценка качества
        mse = mean_squared_error(y_test, y_predicted)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_predicted)

        return Response({
            'status': 'success',
            'plot_img': plot_img,
            'plot_100_dma': plot_100_dma,
            'plot_200_dma': plot_200_dma,
            'plot_prediction': plot_prediction,
            'mse': float(mse),
            'rmse': float(rmse),
            'r2': float(r2)
        }, status=status.HTTP_200_OK)