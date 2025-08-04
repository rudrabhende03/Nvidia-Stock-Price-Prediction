import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("P:/Data Tools/Datasets/nvidia_features.csv")

# Drop nulls just in case
df.dropna(inplace=True)

# Sort by date
df.sort_values("date", inplace=True)

# Create target: next day's close
df["next_close"] = df["close"].shift(-1)
df.dropna(inplace=True)

# Select features
features = [
    "open", "high", "low", "adjclose", "volume",
    "daily_return", "price_change", "price_range",
    "volume_change", "ma_5", "ma_10"
]
X = df[features]
y = df["next_close"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
import numpy as np
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", round(rmse, 4))
print("R²:", round(r2, 4))

# Plot actual vs predicted
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label="Actual", linewidth=2)
plt.plot(y_pred, label="Predicted", linewidth=2)
plt.title("NVIDIA Stock Price Prediction")
plt.xlabel("Test Data Index")
plt.ylabel("Close Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# Save the model for future use
