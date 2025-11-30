import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from preprocess import extract_features

# Load phishing dataset
df = pd.read_csv("phishing_urls.csv")   # make sure this file exists

# Extract features
feature_data = []
for url in df['url']:
    feature_data.append(extract_features(url))

X = pd.DataFrame(feature_data)
y = df['label']

X.fillna(-1, inplace=True)

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model as .pkl
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully as model.pkl")
