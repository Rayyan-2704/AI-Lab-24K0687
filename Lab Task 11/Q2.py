import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

vehicle_data = {
    'serial_no': [5,3,8,2,4,7,6,10,1,9],
    'distance_driven': [150000,120000,250000,80000,100000,220000,180000,300000,75000,280000],
    'efficiency': [15,18,10,22,20,12,16,8,24,9],
    'service_cost': [5000,4000,7000,2000,3000,6500,5500,8000,1500,7500],
    'type': ['SUV','Sedan','Truck','Hatchback','Sedan','Truck','SUV','Truck','Hatchback','SUV']
}

vehicles_df = pd.DataFrame(vehicle_data)
encoded_df = pd.get_dummies(vehicles_df, columns=['type'])

model_without_scaling = KMeans(n_clusters=3, random_state=42)
clusters_raw = model_without_scaling.fit_predict(encoded_df)

vehicles_df['Cluster_NoScaling'] = clusters_raw
scaler = StandardScaler()
scaled_values = scaler.fit_transform(encoded_df)

model_with_scaling = KMeans(n_clusters=3, random_state=42)
clusters_scaled = model_with_scaling.fit_predict(scaled_values)

vehicles_df['Cluster_Scaling'] = clusters_scaled
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(vehicles_df.to_string(index=False))
