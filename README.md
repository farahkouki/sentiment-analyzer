<<<<<<< HEAD
# 🌍 Multilingual Sentiment Analyzer (FR/EN/AR)

Ce projet IA analyse le sentiment d’une phrase (positif, négatif, neutre) en **trois langues** :
- 🇫🇷 Français  
- 🇬🇧 Anglais  
- 🇹🇳 / 🇸🇦 Arabe (Darija / MSA)

Il utilise un pipeline classique NLP : **TF-IDF + Logistic Regression**.

---

## 🚀 Fonctionnalités

- Entrée : phrase FR/EN/AR
- Sortie : positif / négatif / neutre
- Modèle léger, rapide, facile à déployer
- Interface web Streamlit

---

## 🧠 Technologies

- Python 3  
- scikit-learn  
- pandas  
- streamlit  

---
🧪 Tester la prédiction

Pour tester le modèle dans la console :

python src/predict.py


Tape une phrase et le modèle renverra son sentiment (positif, négatif ou neutre).

🌐 Lancer l’interface Web Streamlit
streamlit run src/app.py


Une page va s’ouvrir dans ton navigateur, et ton IA sera prête à l’emploi ! 🚀🤖

✨ Auteur

Farah KOUKI — Full-Stack & AI Developer





