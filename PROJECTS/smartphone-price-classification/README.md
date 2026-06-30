# Smartphone Price-Range Classification & Feature Ranking

TCS iON RIO 125 internship project: *"Rank Features of a Smartphone."* Uses smartphone specs (battery, RAM, screen, connectivity, etc.) to:
1. Rank which specs matter most to price
2. Train and compare classifiers that predict a phone's price range from its specs

## Approach
1. Explore distributions of all features
2. Rank phones and individual features by price contribution
3. Prepare data: encode, scale, train/test split
4. Train and compare Logistic Regression, Gaussian Naive Bayes, SVM, Decision Tree, and Random Forest
5. Tune Random Forest estimator count
6. Cross-validate all models (10-fold) for a more reliable comparison

## Files
- `smartphone_price_classification.ipynb` — full analysis, documented step by step
- `INDUSTRY_REPORT_RIO.docx` — written report for the internship submission
- `data/` — place `train.csv` and `test.csv` here before running (not included; see below)

## Data
This project uses the public [Mobile Price Classification dataset](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification) on Kaggle. Download `train.csv` and `test.csv` into a `data/` folder next to the notebook.

## Run it
```bash
pip install numpy pandas matplotlib seaborn scikit-learn plotly
jupyter notebook smartphone_price_classification.ipynb
```

## Result
Random Forest and SVM perform best in cross-validation; Logistic Regression is a solid, more interpretable baseline. RAM, battery power, and pixel resolution rank as the specs most consistently associated with higher price range.
