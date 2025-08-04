
# NVIDIA Stock Price Prediction Project

## 🧠 Project Summary

Analyzed and predicted NVIDIA (NVDA) stock price trends using a full data pipeline: data cleaning (Python), feature engineering (SQL), predictive modeling (Python), and dashboard visualization (Power BI).

---

## 📊 Dataset

- **Source**: Historical NVDA stock data (2015–2024)
- **Fields**: `date`, `open`, `high`, `low`, `close`, `adjclose`, `volume`

---

## 🛠️ Workflow & Tools

### ✏️ 1. Data Cleaning (Python)

- Loaded raw CSV with misaligned headers
- Cleaned and standardised column names
- Parsed dates and ensured numeric data types
- Removed nulls and sorted chronologically

### 📈 2. SQL Feature Engineering (PostgreSQL)

- Engineered the following fields:
  - `daily_return`: % change from previous close
  - `price_change`: close-open
  - `price_range`: high-low
  - `volume_change`: daily volume difference
  - `ma_5`, `ma_10`: 5-day and 10-day moving averages (window functions)
- Rounded all outputs to 2 or 4 decimal places

### 📊 3. Predictive Modeling (Python)

- Target: next-day `close` price
- Features: all price-related columns + engineered features
- Preprocessing: shifted close column, dropped nulls, sorted by date
- Model: `LinearRegression` from `scikit-learn`
- Evaluation: RMSE, R², actual vs. predicted chart

### 🔄 4. Visualisation (Power BI)

- Time-series line chart with moving averages
- Daily return and price range visuals
- Scatter plot: volume vs daily return
- KPI cards: latest closing price, daily return, volume
- Interactive slicers and filters

---

## 📊 Results

- **RMSE**: 10.2453
- **R² Score**: 0.9381
- Model captured overall trend with reasonable accuracy
- Dashboard provided intuitive financial insights

---

## 📁 Project Structure

```
nvidia-stock-prediction/
├── cleaning/
│   └── data_cleaning.py
├── data/
│   └── nvidia_features.csv
│   └── NVIDIA_STOCK.csv
├── sql/
│   └── feature_engineering.sql
├── scripts/
│   └── prediction_model.py
├── visuals/
│   └── Nvidia_Stock_Analysis.png
│   └── Prediction_Graph.png
├── dashboard/
│   └── nvidia_dashboard.pbix
└── README.md
```

---

## 🚀 Future Work

- Use advanced models (XGBoost, Random Forest)
- Incorporate external data (news sentiment, earnings dates)
- Deploy as a Streamlit app or web dashboard

---

## ✨ Author

Rudra Bhende — [LinkedIn](https://www.linkedin.com/in/rudra-bhende/) | [GitHub](https://github.com/rudrabhende03/Rudra-s-Portfolio)
