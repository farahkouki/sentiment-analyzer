import streamlit as st
import pickle

# Charger le modèle
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌍 Multilingual Sentiment Analyzer (FR/EN/AR)")
st.write("Entrez une phrase en Arabe, Français ou Anglais")

text_input = st.text_area("Votre texte ici...")

if st.button("Analyser"):
    if text_input.strip() == "":
        st.warning("Veuillez entrer une phrase.")
    else:
        prediction = model.predict([text_input])[0]
        if prediction == "positive":
            st.success("💚 Sentiment : POSITIF")
        elif prediction == "negative":
            st.error("💔 Sentiment : NÉGATIF")
        else:
            st.info("😐 Sentiment : NEUTRE")
