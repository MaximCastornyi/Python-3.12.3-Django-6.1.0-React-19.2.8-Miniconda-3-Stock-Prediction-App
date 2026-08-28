from django.urls import path
from accounts import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import StockPredictionAPIView

# Простая view-функция для корневого пути /api/v1/
@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to Stock Prediction API v1",
        "endpoints": {
            "register": "/api/v1/register/",
            "token_obtain": "/api/v1/token/",
            "token_refresh": "/api/v1/token/refresh/",
            "protected_view": "/api/v1/protected-view/",
            "predict": "/api/v1/predict/"
        }
    })

urlpatterns = [
    # Главная страница для /api/v1/
    path('', api_root, name='api_root'),

    path('register/', UserViews.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected-view/', UserViews.ProtectedView.as_view(), name='protected_view'),

    # Prediction API
    path('predict/', StockPredictionAPIView.as_view(), name='stock_prediction'),
]


# from django.urls import path
# from accounts import views as UserViews
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import StockPredictionAPIView


# urlpatterns = [
#     path('register/', UserViews.RegisterView.as_view()),

#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     path('protected-view/', UserViews.ProtectedView.as_view()),

#     # Prediction API
#     path('predict/', StockPredictionAPIView.as_view(), name='stock_prediction')
# ]
