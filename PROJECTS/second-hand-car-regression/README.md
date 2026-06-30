# Second-Hand Car Price Prediction (Linear Regression)

Predicts used-car prices from brand, body type, mileage, engine size, engine type, year, and registration status.

## Approach
1. Clean the data (drop unusable columns, remove missing values)
2. Remove outliers in price, mileage, engine volume, and year
3. Check linearity and log-transform the price target (price is right-skewed)
4. Check multicollinearity with VIF and drop `Year`
5. One-hot encode categorical features
6. Scale features, split train/test, fit a linear regression
7. Evaluate residuals and prediction error on the test set

## Files
- `second_hand_car_price_prediction.ipynb` — full analysis, documented step by step
- `1.04. Real-life example.csv` — input data

## Run it
```bash
pip install numpy pandas matplotlib seaborn scikit-learn statsmodels
jupyter notebook second_hand_car_price_prediction.ipynb
```

## Result
The model explains a solid share of price variance after addressing skew, outliers, and multicollinearity. See the notebook's final section for residual analysis on the test set.
