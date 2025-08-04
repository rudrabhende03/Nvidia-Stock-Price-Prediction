-- Create the Table
CREATE TABLE nvidia_stock (
    date DATE,
    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    adjclose DOUBLE PRECISION,
    volume BIGINT
);

-- Import the CSV File
COPY nvidia_stock(date, open, high, low, close, adjclose, volume)
FROM 'P:/Data Tools/Datasets/NVIDIA_STOCK_cleaned.csv'
DELIMITER ','
CSV HEADER;

-- Add new columns
ALTER TABLE nvidia_stock
ADD COLUMN daily_return DOUBLE PRECISION,
ADD COLUMN price_change DOUBLE PRECISION,
ADD COLUMN price_range DOUBLE PRECISION,
ADD COLUMN volume_change BIGINT,
ADD COLUMN ma_5 DOUBLE PRECISION,
ADD COLUMN ma_10 DOUBLE PRECISION;

-- Populate engineered columns
UPDATE nvidia_stock
SET daily_return = ROUND((close - LAG(close) OVER (ORDER BY date)) / LAG(close) OVER (ORDER BY date) * 100, 4),
    price_change = ROUND(close - open, 2),
    price_range = ROUND(high - low, 2),
    volume_change = volume - LAG(volume) OVER (ORDER BY date),
    ma_5 = ROUND(AVG(close) OVER (ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 2),
    ma_10 = ROUND(AVG(close) OVER (ORDER BY date ROWS BETWEEN 9 PRECEDING AND CURRENT ROW), 2);
