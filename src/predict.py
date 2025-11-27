import pickle

# Charger le modèle
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_sentiment(text):
    prediction = model.predict([text])[0]
    return prediction

if __name__ == "__main__":
    phrase = input("Entrez une phrase: ")
    print("Sentiment:", predict_sentiment(phrase))
