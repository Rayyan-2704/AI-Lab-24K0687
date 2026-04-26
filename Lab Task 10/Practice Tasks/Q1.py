import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

housing_data = pd.read_csv("/content/sample_data/california_housing_test.csv")
housing_data = housing_data.dropna()

features = housing_data.drop("median_house_value", axis=1)
target = housing_data["median_house_value"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

predictions = reg_model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, predictions)}")

rmse_value = np.sqrt(mean_squared_error(y_test, predictions))
print(f"RMSE: {rmse_value}")

sample_input = pd.DataFrame([features.iloc[0]], columns=features.columns)
print(f"Predicted Price: {reg_model.predict(sample_input)}")
