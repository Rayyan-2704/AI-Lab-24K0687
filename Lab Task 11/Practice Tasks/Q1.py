import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

mall_data = pd.read_csv("Mall_Customers.csv")
customer_features = mall_data.drop("CustomerID", axis=1)
customer_features = pd.get_dummies(customer_features, drop_first=True)

kmeans_raw = KMeans(n_clusters=5, random_state=42)
labels_raw = kmeans_raw.fit_predict(customer_features)

plt.figure(figsize=(6,4))
plt.scatter(customer_features.iloc[:, 0], customer_features.iloc[:, 1], c=labels_raw)
plt.title("Clustering Without Scaling")
plt.show()

scaled_features = customer_features.copy()
scaler = StandardScaler()
scale_cols = scaled_features.columns.drop("Age")

scaled_features[scale_cols] = scaler.fit_transform(scaled_features[scale_cols])
kmeans_scaled = KMeans(n_clusters=5, random_state=42)
labels_scaled = kmeans_scaled.fit_predict(scaled_features)

plt.figure(figsize=(6,4))
plt.scatter(scaled_features.iloc[:, 0], scaled_features.iloc[:, 1], c=labels_scaled)
plt.title("Clustering With Scaling")
plt.show()
