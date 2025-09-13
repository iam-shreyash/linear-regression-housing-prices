🏠 Housing Price Prediction with Linear Regression
📌 Objective

Build a simple Linear Regression Model to predict housing prices using 1–2 features (RM and LSTAT) from the dataset.

📂 Contents

Housing Data.csv → dataset used

linear-regression-housing-prices.ipynb → Jupyter notebook with code

images/ → visualizations (scatter plots, regression line, etc.)

README.md → project story

⚙️ Tools & Libraries

Python 3.x

pandas

scikit-learn

matplotlib, seaborn

🚀 Steps

Loaded dataset (Housing Data.csv)

Selected 2 features:

RM → Average number of rooms

LSTAT → % lower status population

Handled missing values (LSTAT had 20 missing values → dropped)

Split data into train and test using train_test_split

Trained a Linear Regression Model using scikit-learn

Evaluated with R², MAE, RMSE

Visualized Actual vs Predicted prices and Regression Line

📊 Results

R² Score: ~0.66

MAE: ~3.7

RMSE: ~4.8

Positive correlation between RM (rooms) and MEDV (price).

Negative correlation between LSTAT (lower status %) and MEDV.

🖼 Visualizations
1. Actual vs Predicted Prices
![Actual vs Predicted](images/Figure_1.png)

2. Regression Line (RM vs MEDV)
![Actual vs Predicted](images/Figure_2.png)

📝 Conclusion

Linear Regression with just 2 features gives a decent prediction accuracy (R² ≈ 0.66).
