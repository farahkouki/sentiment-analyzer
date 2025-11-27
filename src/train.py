import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# Charger le dataset
data = pd.read_csv("data/dataset.csv")

X = data["text"]
y = data["label"]

# Pipeline TF-IDF + Logistic Regression
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=200))
])

# Entraînement
model.fit(X, y)

# Sauvegarde du modèle
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Modèle entraîné et sauvegardé dans models/model.pkl")
