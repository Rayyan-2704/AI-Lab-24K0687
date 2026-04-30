import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.utils import resample

data = pd.read_csv("creditcard.csv")
fraud_cases = data[data['Class'] == 1]
legit_cases = data[data['Class'] == 0]

legit_sample = resample(legit_cases, replace=False, n_samples=len(fraud_cases), random_state=42)
balanced_data = pd.concat([fraud_cases, legit_sample])
balanced_data = balanced_data.sample(frac=1, random_state=42)

features = balanced_data.drop('Class', axis=1)
target = balanced_data['Class']

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

x_train, x_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.3, random_state=42)

log_model = LogisticRegression(max_iter=1000)
forest_model = RandomForestClassifier()

log_model.fit(x_train, y_train)
forest_model.fit(x_train, y_train)

log_predictions = log_model.predict(x_test)
forest_predictions = forest_model.predict(x_test)

print("\n==> Logistic Regression")
print(f"\tAccuracy: {accuracy_score(y_test, log_predictions):.4f}")
print(f"\tPrecision: {precision_score(y_test, log_predictions):.4f}")
print(f"\tRecall: {recall_score(y_test, log_predictions):.4f}")
print(f"\tF1-score: {f1_score(y_test, log_predictions):.4f}")

print("\n==> Random Forest")
print(f"\tAccuracy: {accuracy_score(y_test, forest_predictions):.4f}")
print(f"\tPrecision: {precision_score(y_test, forest_predictions):.4f}")
print(f"\tRecall: {recall_score(y_test, forest_predictions):.4f}")
print(f"\tF1-score: {f1_score(y_test, forest_predictions):.4f}")
