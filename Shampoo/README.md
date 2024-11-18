# Shampoo Sales Analysis Project

## Background and Objective
The objective of this project is to forecast shampoo sales using various time series models and machine learning. Accurately predicting future sales can help optimize production, inventory management and marketing strategies.

## Data used
The data used comes from monthly shampoo sales history. The data was explored to understand trends and seasonality.

## Methodology
1. **Data preparation** :
- Logarithmic transformation to stabilize variance.
- Checked for stationarity and differentiated if necessary.

2. **Modeling** :
- Implementation of several models to capture trends and seasonal effects:
- SARIMA
- Prophet
- Linear regression
- LSTM (Long Short-Term Memory)

3. **Validation and Evaluation** :
- Division of data into training and test sets.
- Evaluation of model performance with metrics such as RMSE, MAE and R².
- Comparison of models to select the one with the best performance.

## Preliminary results 

### SARIMA :
- **RMSE**: 172.37 - Indicates a large mean prediction error. 
- **R²** : -1.36 - Suggests that the model does not explain the data variance well. 
- **MAE** : 140.16 - Shows significant prediction errors. 
### Prophet : 
- **RMSE** : 161.26 - Shows slight improvement over SARIMA. 
- **R²** : -1.06 - Also indicates that the model does not explain data variance well. 
- **MAE** : 131.30 - Indicates still significant prediction errors. 
- **MSE** : 26004.22 - Confirms that prediction errors are significant.

