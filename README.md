# 🏠 Housing Price Prediction with Linear Regression  

## 📌 Objective  
Build a simple **Linear Regression Model** to predict **housing prices** using **2 features** (`RM` and `LSTAT`) from the dataset.  

---

## 📂 Contents  
- `Housing Data.csv` → dataset used  
- `linear-regression-housing-prices.ipynb` → Jupyter notebook with code  
- `images/` → visualizations (scatter plots, regression line, etc.)  
- `README.md` → project story  

---

## ⚙️ Tools & Libraries  
- Python 3.x  
- pandas  
- scikit-learn  
- matplotlib, seaborn  

---

## 🚀 Steps  
1. Loaded dataset (`Housing Data.csv`)  
2. Selected 2 features:  
   - **RM** → Average number of rooms  
   - **LSTAT** → % lower status population  
3. Handled missing values (`LSTAT` had 20 missing values → dropped)  
4. Split data into **train** and **test** using `train_test_split`  
5. Trained a **Linear Regression Model** using scikit-learn  
6. Evaluated with **R², MAE, RMSE**  
7. Visualized **Actual vs Predicted Prices** and **Regression Line**  

---

## 📊 Results  
- **R² Score**: ~0.66  
- **MAE**: ~3.7  
- **RMSE**: ~4.8  
- Positive correlation between **RM** (rooms) and **MEDV** (price)  
- Negative correlation between **LSTAT** (lower status %) and **MEDV**  

---

## 🖼 Visualizations  
### 1. Actual vs Predicted Prices  
![Actual vs Predicted](images/actual_vs_predicted.png)  

### 2. Regression Line (RM vs MEDV)  
![Regression Line](images/regression_line.png)  

---

## 📝 Conclusion  
Linear Regression with just **2 features** gives a **decent prediction accuracy** (R² ≈ 0.66).  
Adding more features or advanced models (e.g., Random Forest, XGBoost) can further improve performance.  
