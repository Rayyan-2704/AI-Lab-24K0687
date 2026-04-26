import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

student_data = {
    'id': [1,2,3,4,5,6,7,8,9,10],
    'gpa': [3.5,2.8,3.9,1.8,2.5,3.2,3.7,2.0,2.9,3.8],
    'hours_studied': [20,10,25,5,12,18,22,7,15,24],
    'attendance': [90,70,95,60,75,85,92,65,80,96]
}

students_df = pd.DataFrame(student_data)
features = students_df[['gpa', 'hours_studied', 'attendance']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

inertia_values = []
k_range = range(2, 7)

for k in k_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(scaled_features)
    inertia_values.append(model.inertia_)

plt.plot(k_range, inertia_values)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

final_model = KMeans(n_clusters=3, random_state=42)
cluster_labels = final_model.fit_predict(scaled_features)
students_df['Cluster'] = cluster_labels

plt.scatter(students_df['hours_studied'], students_df['gpa'], c=cluster_labels)
plt.xlabel("Hours Studied")
plt.ylabel("GPA")
plt.title("Student Clusters")

plt.tight_layout()
plt.show()
print(students_df.to_string(index=False))
