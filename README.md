# 🎯 Projet Deep Learning - Word2Vec & Streamlit

## 📝 Objectif

Ce projet a pour but de mettre en œuvre un projet complet de **Deep Learning** et de le présenter de manière interactive grâce à **Streamlit**.

L’objectif principal est de :
- Construire un modèle **Word2Vec** (word embeddings),
- L'entraîner sur un corpus de critiques de films,
- Sauvegarder le modèle (`.h5`),
- Visualiser et explorer les résultats à travers une application **Streamlit** déployée.

## 📁 Organisation du projet

```graphql
.
├── app/                  # Application Streamlit (app.py)
├── models/               # Modèle entraîné et tokenizer (fichiers suivis avec Git LFS)
├── notebooks/            # Notebook d'entraînement du modèle Word2Vec
├── requirements.txt      # Dépendances Python
├── .gitattributes        # Suivi Git LFS pour le modèle
└── README.md             # Ce fichier
```

## 💡 Environnement requis

- Python 3.10
- Si tu utilises conda, tu peux créer un environnement comme suit :

```bash
conda create -n movie_review_env python=3.10
conda activate movie_review_env
pip install -r requirements.txt
```

### requirements.txt

Ce fichier liste les packages compatibles avec mon code et mon environnement :

```txt
streamlit==1.35.0
tensorflow==2.19.0
scikit-learn==1.4.1
numpy==1.24.4
pandas==2.1.4
nltk==3.8.1
```
⚠️ Remarque : tensorflow==2.19.0 car c’est celle que j'utilise. Si tu veux être compatible avec tensorflow-cpu, tu peux préciser :

```txt
tensorflow-cpu==2.19.0
```

Mais ne mets pas les deux en même temps (tensorflow et tensorflow-cpu sont mutuellement exclus).


## 🧠 Données

Le jeu de données comprend **25 000 critiques de films** en anglais. Ces critiques serviront à entraîner le modèle Word2Vec pour apprendre des représentations vectorielles du langage (embeddings).
⚠️ Ce fichier n’est pas stocké dans le dépôt pour ne pas alourdir le repo. Il est à télécharger manuellement pour l’entraînement ici : **[lien](https://train-exo.s3.eu-west-1.amazonaws.com/2317/MovieReview.csv)**

## 🧪 Entraînement du modèle Word2Vec

Un notebook d'entraînement est disponible dans notebooks/, contenant :
- Le nettoyage des données textuelles,
- La tokenisation et la construction du vocabulaire,
- L’entraînement du modèle de type skip-gram via Keras,
- La sauvegarde des artefacts :
    - word2vec.h5 (modèle Keras),
    - tokenizer.pkl (tokenizer TensorFlow).

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
