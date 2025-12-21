---
name: Time Series Analysis
description: Analyze temporal data patterns including trends, seasonality, autocorrelation, and forecasting for time series decomposition, trend analysis, and forecasting models
---

# Time Series Analysis

## Overview

Time series analysis examines data points collected over time to identify patterns, trends, and seasonality for forecasting and understanding temporal dynamics.

## When to Use

- Forecasting future values based on historical trends
- Detecting seasonality and cyclical patterns in data
- Analyzing trends over time in sales, stock prices, or website traffic
- Understanding autocorrelation and temporal dependencies
- Making time-based predictions with confidence intervals
- Decomposing data into trend, seasonal, and residual components

## Core Components

- **Trend**: Long-term directional movement
- **Seasonality**: Repeating patterns at fixed intervals
- **Cyclicity**: Long-term oscillations (non-fixed periods)
- **Stationarity**: Constant mean, variance over time
- **Autocorrelation**: Correlation with past values

## Key Techniques

- **Decomposition**: Separating trend, seasonal, residual components
- **Differencing**: Making data stationary
- **ARIMA**: AutoRegressive Integrated Moving Average models
- **Exponential Smoothing**: Weighted average of past values
- **SARIMA**: Seasonal ARIMA models

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Create sample time series data
dates = pd.date_range('2020-01-01', periods=365, freq='D')
values = 100 + np.sin(np.arange(365) * 2*np.pi / 365) * 20 + np.random.normal(0, 5, 365)
ts = pd.Series(values, index=dates)

# Visualize time series
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

axes[0, 0].plot(ts)
axes[0, 0].set_title('Original Time Series')
axes[0, 0].set_ylabel('Value')

# Decomposition
decomposition = seasonal_decompose(ts, model='additive', period=30)
axes[0, 1].plot(decomposition.trend)
axes[0, 1].set_title('Trend Component')

axes[1, 0].plot(decomposition.seasonal)
axes[1, 0].set_title('Seasonal Component')

axes[1, 1].plot(decomposition.resid)
axes[1, 1].set_title('Residual Component')

plt.tight_layout()
plt.show()

# Test for stationarity (Augmented Dickey-Fuller)
result = adfuller(ts)
print(f"ADF Test Statistic: {result[0]:.6f}")
print(f"P-value: {result[1]:.6f}")
print(f"Critical Values: {result[4]}")

if result[1] <= 0.05:
    print("Time series is stationary")
else:
    print("Time series is non-stationary - differencing needed")

# First differencing for stationarity
ts_diff = ts.diff().dropna()
result_diff = adfuller(ts_diff)
print(f"\nAfter differencing - ADF p-value: {result_diff[1]:.6f}")

# Autocorrelation and Partial Autocorrelation
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

plot_acf(ts_diff, lags=40, ax=axes[0])
axes[0].set_title('ACF')

plot_pacf(ts_diff, lags=40, ax=axes[1])
axes[1].set_title('PACF')

plt.tight_layout()
plt.show()

# ARIMA Model
arima_model = ARIMA(ts, order=(1, 1, 1))
arima_result = arima_model.fit()
print(arima_result.summary())

# Forecast
forecast_steps = 30
forecast = arima_result.get_forecast(steps=forecast_steps)
forecast_df = forecast.conf_int()
forecast_mean = forecast.predicted_mean

# Plot forecast
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(ts.index[-90:], ts[-90:], label='Historical')
ax.plot(forecast_df.index, forecast_mean, label='Forecast', color='red')
ax.fill_between(
    forecast_df.index,
    forecast_df.iloc[:, 0],
    forecast_df.iloc[:, 1],
    color='red', alpha=0.2
)
ax.set_title('ARIMA Forecast with Confidence Interval')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# Exponential Smoothing
exp_smooth = ExponentialSmoothing(
    ts, seasonal_periods=30, trend='add', seasonal='add', initialization_method='estimated'
)
exp_result = exp_smooth.fit()

# Model diagnostics
fig = exp_result.plot_diagnostics(figsize=(12, 8))
plt.tight_layout()
plt.show()

# Custom moving average analysis
window_sizes = [7, 30, 90]
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(ts.index, ts.values, label='Original', alpha=0.7)

for window in window_sizes:
    ma = ts.rolling(window=window).mean()
    ax.plot(ma.index, ma.values, label=f'MA({window})')

ax.set_title('Moving Averages')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# Seasonal subseries plot
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for i, month in enumerate(range(1, 5)):
    month_data = ts[ts.index.month == month]
    axes[i // 2, i % 2].plot(month_data.values)
    axes[i // 2, i % 2].set_title(f'Month {month} Pattern')

plt.tight_layout()
plt.show()

# Forecast accuracy metrics
def calculate_forecast_metrics(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return {'MAE': mae, 'RMSE': rmse, 'MAPE': mape}

metrics = calculate_forecast_metrics(ts[-30:], forecast_mean[:30])
print(f"\nForecast Metrics:\n{metrics}")

# Additional analysis techniques

# Step 10: Seasonal subseries plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for i, season in enumerate([1, 2, 3, 4]):
    seasonal_ts = ts[ts.index.month % 4 == season % 4]
    axes[i // 2, i % 2].plot(seasonal_ts.values)
    axes[i // 2, i % 2].set_title(f'Season {season}')
plt.tight_layout()
plt.show()

# Step 11: Granger causality (for multiple series)
from statsmodels.tsa.stattools import grangercausalitytests

# Create another series for testing
ts2 = ts.shift(1).fillna(method='bfill')

try:
    print("\nGranger Causality Test:")
    print(f"Test whether ts2 Granger-causes ts:")
    gc_result = grangercausalitytests(np.column_stack([ts.values, ts2.values]), maxlag=3)
except Exception as e:
    print(f"Granger causality not performed: {str(e)[:50]}")

# Step 12: Autocorrelation and partial autocorrelation analysis
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

acf_values = acf(ts.dropna(), nlags=20)
pacf_values = pacf(ts.dropna(), nlags=20)

# Step 13: Seasonal strength
def seasonal_strength(series, seasonal_period=30):
    seasonal = seasonal_decompose(series, model='additive', period=seasonal_period)
    var_residual = np.var(seasonal.resid.dropna())
    var_seasonal = np.var(seasonal.seasonal)
    return 1 - (var_residual / (var_residual + var_seasonal)) if (var_residual + var_seasonal) > 0 else 0

ss = seasonal_strength(ts)
print(f"\nSeasonal Strength: {ss:.3f}")

# Step 14: Forecasting with uncertainty
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(ts.index[-60:], ts.values[-60:], label='Historical', linewidth=2)

# Multiple horizon forecasts
for steps_ahead in [10, 20, 30]:
    try:
        fc = arima_result.get_forecast(steps=steps_ahead)
        fc_mean = fc.predicted_mean
        ax.plot(pd.date_range(ts.index[-1], periods=steps_ahead+1)[1:],
               fc_mean.values, marker='o', label=f'Forecast (+{steps_ahead})')
    except:
        pass

ax.set_title('Multi-step Ahead Forecasts')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 15: Model comparison summary
print("\nTime Series Analysis Complete!")
print(f"Original series length: {len(ts)}")
print(f"Trend strength: {1 - np.var(decomposition.resid.dropna()) / np.var((ts - ts.mean()).dropna()):.3f}")
print(f"Seasonal strength: {ss:.3f}")
```

## Stationarity

- **Stationary**: Mean, variance, autocorrelation constant over time
- **Non-stationary**: Trend or seasonal patterns present
- **Solution**: Differencing, log transformation, or detrending

## Model Selection

- **ARIMA**: Good for univariate forecasting
- **SARIMA**: Includes seasonal components
- **Exponential Smoothing**: Simpler, good for trends
- **Prophet**: Handles holidays and changepoints

## Evaluation Metrics

- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Squared Error
- **MAPE**: Mean Absolute Percentage Error

## Deliverables

- Decomposition analysis charts
- Stationarity test results
- ACF/PACF plots
- Fitted models with diagnostics
- Forecast with confidence intervals
- Accuracy metrics comparison
