# Python-3.12.3-Django-6.1.0-React-19.2.8-Miniconda-3-Stock-Prediction-App
This application predicts stock prices 100 and 200 days into the future. The tech stack includes Python, Miniconda, TensorFlow, Scikit-learn, and Matplotlib. You need to create an account and enter the company's stock ticker symbol into the input field.

# 📈 Stock Price Prediction App

The project uses LSTM. "Deep Learning with LSTM Models" generally refers to using the LSTM (Long Short-Term Memory) architecture within deep learning for working with sequential data—such as text, time series, audio, or any data where temporal context matters. It is one of the key approaches to modeling long-term dependencies, overcoming the limitations of standard RNNs.

🔎 What is LSTM?
LSTM (Long Short-Term Memory) is a type of Recurrent Neural Network (RNN).

Key feature: The presence of a cell state and control mechanisms (gates—input, output, and forget gates).

These mechanisms allow the network to retain or discard information over long periods, solving the vanishing/exploding gradient problem inherent in traditional RNNs.

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


## 📊 Model Evaluation

The performance of the LSTM stock price prediction model is evaluated using standard regression metrics:

| Metric | Value | Status |
| :--- | :--- | :--- |
| **R-Squared ($R^2$)** | `0.9828` (98.28%) | 🟢 Excellent |
| **RMSE** | `12.03` | 🔵 Good |
| **MSE** | `144.83` | ⚪ Baseline |

---

### 🔍 Metrics Breakdown

* **R-Squared ($R^2$) = `0.9828` (98.28%) — Excellent Result**
  * Measures the proportion of variance (trends) in price movement explained by the model.
  * The maximum possible value is **`1.0` (100%)**.
  * The model captures the overall market direction with **98.28%** precision, tracking general price trends effectively.

* **RMSE (Root Mean Squared Error) = `12.03` — Average Error ($)**
  * Provides an intuitive metric for real-world accuracy as it is measured in the **same units as stock prices (USD)**.
  * On average, predictions deviate from actual closing prices by approximately **~$12.03**.
  * > **Note:** For a stock priced between **$150–$200**, a $12 margin represents strong relative accuracy (~6–8%).

* **MSE (Mean Squared Error) = `144.83`**
  * Represents the squared value of RMSE ($12.03^2 \approx 144.83$).
  * Heavily penalizes **large mispredictions and price spikes** (outliers).
  * Used internally by the machine learning framework as the optimization loss function.
  
<br/><br/>
<img width="1212" height="616" alt="1" src="https://github.com/user-attachments/assets/d6eecb20-d17a-4569-b0a6-37b711b26907" />
<br/><br/>
<img width="1212" height="616" alt="2" src="https://github.com/user-attachments/assets/52912f2d-24b2-483b-91f0-741bc0733787" />
<br/><br/>
<img width="1212" height="616" alt="3" src="https://github.com/user-attachments/assets/19e873ed-9792-4bbb-81d5-26cfc628db18" />
<br/><br/>
<img width="1212" height="616" alt="4" src="https://github.com/user-attachments/assets/c0e6e9bf-a93b-451b-81bb-ad4835e70da5" />
<br/><br/>
<img width="1212" height="616" alt="5" src="https://github.com/user-attachments/assets/79c2ad43-a34b-4d93-b08c-43679a80f3c2" />
<br/><br/>
<img width="1212" height="616" alt="6" src="https://github.com/user-attachments/assets/4a44fb0e-9228-4f32-92cf-c826752cf7c8" />
<br/><br/>
<img width="1212" height="616" alt="7" src="https://github.com/user-attachments/assets/ff629bc4-eea4-437d-92b9-d25e8f43d7ba" />
<br/><br/>
<img width="1212" height="616" alt="8" src="https://github.com/user-attachments/assets/c071027e-1cec-4c40-96b6-6d5dc01807c7" />
<br/><br/>
<img width="1212" height="616" alt="9" src="https://github.com/user-attachments/assets/37b6b7ef-5572-4c8d-ab1c-0557ec5167ec" />
<br/><br/>
<img width="1212" height="616" alt="10" src="https://github.com/user-attachments/assets/0ff8e7f5-5980-44bb-a352-14634bf3b401" />
<br/><br/>
<img width="1212" height="616" alt="11" src="https://github.com/user-attachments/assets/6a514a87-cb22-45d3-b0d7-07226b6e8065" />
<br/><br/>
<img width="1212" height="616" alt="12" src="https://github.com/user-attachments/assets/e0013f7d-383f-488d-a0bd-c9591ff50d94" />
<br/><br/>
<img width="1212" height="616" alt="13" src="https://github.com/user-attachments/assets/e7d7c0cc-36fd-499c-93a8-8a539ad45ef8" />
<br/><br/>
<br/><br/>
