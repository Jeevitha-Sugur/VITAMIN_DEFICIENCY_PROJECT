import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load dataset
data = pd.read_csv('data/dataset.csv')

X = data.drop('deficiency', axis=1)
y = data['deficiency']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Ensure folder exists
os.makedirs('model', exist_ok=True)

# Save model in correct folder
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved!")