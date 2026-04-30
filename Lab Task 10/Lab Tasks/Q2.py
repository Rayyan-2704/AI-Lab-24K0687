import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

housing_data = pd.read_csv("train.csv")

housing_data.drop("Id", axis=1, inplace=True)
housing_data.fillna(housing_data.median(numeric_only=True), inplace=True)
housing_data.fillna("None", inplace=True)

encoded_data = pd.get_dummies(housing_data)
features = encoded_data.drop("SalePrice", axis=1)
target = encoded_data["SalePrice"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

linear_model = LinearRegression()
tree_model = DecisionTreeRegressor()

linear_model.fit(x_train, y_train)
tree_model.fit(x_train, y_train)

linear_predictions = linear_model.predict(x_test)
tree_predictions = tree_model.predict(x_test)

linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_rmse = np.sqrt(mean_squared_error(y_test, linear_predictions))

print("\n==> Linear Regression")
print(f"\tMAE : {linear_mae:.4f}")
print(f"\tRMSE: {linear_rmse:.4f}")

tree_mae = mean_absolute_error(y_test, tree_predictions)
tree_rmse = np.sqrt(mean_squared_error(y_test, tree_predictions))

print("\n==> Decision Tree")
print(f"\tMAE : {tree_mae:.4f}")
print(f"\tRMSE: {tree_rmse:.4f}")
