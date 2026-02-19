import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("data/dummy_data.csv")

X = data[["heart_rate", "temperature", "motion"]]

model = IsolationForest(contamination=0.2)
model.fit(X)

joblib.dump(model, "ml/model.pkl")

print("Model trained")
