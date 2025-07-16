# 🎯 Projet Deep Learning - Word2Vec & Streamlit

## 📝 Objectif

Ce projet a pour but de mettre en œuvre un projet complet de **Deep Learning** et de le présenter de manière interactive grâce à **Streamlit**.

L’objectif principal est de :
- Construire un modèle **Word2Vec** (word embeddings),
- L'entraîner sur un corpus de critiques de films,
- Sauvegarder le modèle (`.h5`),
- Visualiser et explorer les résultats à travers une application **Streamlit** déployée.

## 📁 Organisation du projet

- `notebooks/` : Contient le code d'entraînement, le prétraitement et les tests.
- `data/` : Contient les données d'entraînement (critiques de films).
- `models/` : Contiendra le fichier `.h5` sauvegardé avec Git LFS.
- `app/` : Application Streamlit à déployer.
- `requirements.txt` : Liste des dépendances nécessaires.
- `.gitattributes` : Fichier de configuration Git LFS.

## 🧠 Données

Le jeu de données comprend **25 000 critiques de films** en anglais. Ces critiques serviront à entraîner le modèle Word2Vec pour apprendre des représentations vectorielles du langage (embeddings).

🔗 Les données peuvent être téléchargées ici : **[lien](https://train-exo.s3.eu-west-1.amazonaws.com/2317/MovieReview.csv)**

## 🚀 Lancement du projet

### 1. Cloner le dépôt

```bash
git clone <url_du_repo>
cd <nom_du_projet>
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```
### 3. Lancer l'application Streamlit

```bash
cd app
streamlit run app.py
```

## Suivi des fichiers .h5 avec Git LFS

Ce projet utilise **Git LFS** pour suivre les fichiers de modèles volumineux :

```bash
git lfs install
git lfs track "*.h5"
git add .gitattributes
```

Le fichier `.gitattributes` contient déjà les règles nécessaires.

## Technologies utilisées

- Python 3.x
- TensorFlow / Keras
- NLTK
- Gensim (Word2Vec)
- Pandas / NumPy
- Streamlit
- Git / Git LFS

## Auteur

Projet réalisé dans le cadre du module Deep Learning de la formation **[Data-Scientist](https://datascientest.com/formation-data-scientist)** de l'organisme de formation **[DataScientest](https://datascientest.com)**
