# 1. Improt necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Load the dataset
df = pd.read_csv('Housing Data.csv')
print(df.head())

print("\nMissing values (per chosen column):")
print(df[['RM', 'LSTAT', 'MEDV']].isna().sum())

# 3.Select Features

# Drop rows with missing values in relevant columns
df = df.dropna(subset=['RM', 'LSTAT', 'MEDV'])
X = df[['RM','LSTAT']]
y = df[['MEDV']]

# 4.Train Test Split
X_train, X_test, y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)

# 5.Train Model
model= LinearRegression()
model.fit(X_train,y_train)

# 6. Predictions
y_pred=model.predict(X_test)

# 7. Evaluation Metrics
print("MAE:",mean_absolute_error(y_test,y_pred))
print("RMSE:",np.sqrt(mean_squared_error(y_test,y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))
print("Coefficients:",model.coef_)
print("Intercept:",model.intercept_)

# 8. Visualization
plt.figure(figsize=(6,6))
plt.scatter(y_test,y_pred,color='blue')
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color='red')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()

# 9. Visualization: One Feature(RM vs Price)
sns.regplot(x=df['RM'], y=df['MEDV'], line_kws={"color":"red"})
plt.title("Relationship between RM and Price")
plt.show()

# SCORES
# MAE: 3.73778017058728
# RMSE: 4.771521061926863
# R2 Score: 0.6635262709616975
# Coefficients: [[ 5.12299271 -0.64577994]]
# Intercept: [-1.30383097]