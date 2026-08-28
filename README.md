# Python-3.12.3-Django-6.1.0-React-19.2.8-Miniconda-3-Stock-Prediction-App
This application predicts stock prices 100 and 200 days into the future. The tech stack includes Python, Miniconda, TensorFlow, Scikit-learn, and Matplotlib. You need to create an account and enter the company's stock ticker symbol into the input field.

# 📈 Stock Price Prediction App

An AI-powered web application for predicting stock prices 100 and 200 days ahead using Deep Learning (LSTM networks).

---

## 🔑 Demo Account / Credentials

To quickly test the application, use the following credentials:

* **Email:** `admin@admin.com`
* **Username:** `admin`
* **Password:** `Pass12345`

> **Note:** Enter the company's official stock ticker symbol (e.g., `AAPL`, `TSLA`, `NVDA`) in the search input field to generate predictions.

---

## 🛠 Tech Stack & Installation

### Core Technologies
* **Python** — Core language & backend logic
* **Miniconda3** — Isolated virtual environment management
* **TensorFlow / Keras** — Deep learning framework for building and training LSTM models
* **Scikit-learn** — Data preprocessing (MinMax scaling) & evaluation metrics
* **Matplotlib** — Data visualization and forecasting plots

### Environment Setup
Create and activate your Conda environment, then install the required dependencies:

```bash
# Create Conda environment
conda create -n stock-app python=3.12 -y
conda activate stock-app

# Install ML dependencies
conda install -c conda-forge scikit-learn matplotlib -y
pip install tensorflow keras
