# Forecasting-System
**Objective:**
The objective of this project is to develop a comprehensive forecasting system capable of implementing and comparing various time series models (ARIMA, ANN, Hybrid ARIMA-ANN) across different sectors. Additionally, the system includes a user-friendly front-end interface for visualizing data and forecasts.

**Data Sources and Preprocessing:**

*Data Sources:*

- Finance Sector: Monthly stock prices from the S&P 500 index.
- Energy Sector: Hourly energy consumption data.
- Environmental Sector: Daily atmospheric CO2 concentrations.

*Preprocessing Steps:*

- Cleaning: Identifying and handling missing values.
- Normalization/Standardization: Scaling data to a uniform range.
- Stationarization: Applying differencing and logarithmic transformations for achieving stationarity.

**Tools and Technologies:**
- Backend: Python with Flask for server-side logic and handling API requests.
- Frontend: ReactJS for building a dynamic and responsive user interface, HTML/CSS for layout and styling.
- Data Science: Python with Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, TensorFlow/Keras.
- Database: SQLite for storing processed data and results, facilitating quick retrieval for visualization.
- Version Control: Git for code management and version control.

**Model Development:**

*ARIMA Configuration and Tuning:*
- Purpose: Modeling and forecasting time series data showing non-stationarity or seasonal patterns.
- Process: Identifying order of differencing (d), number of autoregressive terms (p), and number of lagged forecast errors (q) using statistical tests like ADF and ACF/PACF plots.

*ANN Design and Training:*
- Purpose: Modeling complex nonlinear relationships and interactions in data.
- Process: Designing neural networks with varying architectures and implementing backpropagation for training.

**Other Models:**
- SARIMA: Extending ARIMA for seasonal time series data.
- Exponential Smoothing (ETS): Forecasting with weighted averages of past observations.
- Prophet: Handling time series with strong seasonal effects and historical holidays.
- SVR: Modeling nonlinear relationships using support vector regression.
- LSTM: Suitable for sequence prediction problems.

**Hybrid Models Integration:**
Combining ARIMA and ANN models to leverage their respective strengths and improve forecast accuracy.

**Frontend Development:**

*Interface Design:*
Creating an intuitive UI for dataset selection, model comparisons, and forecast viewing.

*Visualization Tools:*
Implementing interactive charts and graphs for effective data and forecast presentation.

**Interactive Dashboard:**
- Select different forecasting models.
- Display time series data, forecasts, residuals, and accuracy metrics dynamically.
- Compare results between different models side-by-side.
- Upload new data and retrain models interactively.

**Testing and Validation:**

*Model Testing:*
Ensuring reliability and accuracy through historical data validation and techniques like cross-validation.

*System Testing:*
Confirming proper functionality of both backend and frontend components without errors.

**Results:**

*ARIMA:*
- Best model: ARIMA(1, 2, 1) with MSE of 9.9467.

*ANN:*
- Finance Dataset: Loss: 298.91, Metric: 10.59.
- Energy Dataset: Loss: 0.00008, Metric: 0.00732.
- Environment Dataset: Loss: 0.000001, Metric: 0.00086.

*ETS:*
- Finance Dataset: MSE: 618.79, MAE: 15.11, RMSE: 24.88, R2: 0.9994.
- Energy Dataset: MSE: 213363.86, MAE: 304.03, RMSE: 461.91, R2: 0.9682.
- Environment Dataset: MSE: 0.267, MAE: 0.358, RMSE: 0.517, R2: 0.9996.

*SVR:*
- Finance: MAE: 0.124, MSE: 0.035, RMSE: 0.187, R2: 0.967.
- Energy: MAE: 0.777, MSE: 0.957, RMSE: 0.978, R2: 0.041.
- Environment: MAE: 0.072, MSE: 0.007, RMSE: 0.085, R2: 0.993.

*Hybrid:*
- Finance: MAE: 4107.04.
- Energy: MAE: 19893.34.
- Environment: MAE: 406.74.


**FOR RUNNING:**
- git clone https://github.com/shitbaKashif/forecasting-system.git
- Then run flask

*Requirements:*
- python3
- SQlite
- Libraries for models (Prophet, SRIMA, ExponentailSmoothing)
- Tensorflow

**NOTE:** "static" folder has an "image" folder in it which contains all the visualization results of all models.
