import os
import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import Normalizer
from tensorflow.keras.models import load_model

# Définir les chemins en partant du fichier actuel
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_DIR = os.path.join(BASE_DIR, "models")

st.title("🧠 Modèle Word2Vec – Similarité de mots")

@st.cache_resource
def load_tokenizer():
    with open(os.path.join(MODEL_DIR, "tokenizer.pkl"), "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_word2vec_model():
    return load_model(os.path.join(MODEL_DIR, "word2vec.h5"))

tokenizer = load_tokenizer()
model = load_word2vec_model()

word2idx = tokenizer.word_index
idx2word = {v: k for k, v in word2idx.items()}
vocab_size = tokenizer.num_words
vectors = model.layers[0].get_weights()[0]  # Embeddings

def dot_product(vec1, vec2):
    return np.sum((vec1 * vec2))

def cosine_similarity(vec1, vec2):
    return dot_product(vec1, vec2) / np.sqrt(dot_product(vec1, vec1) * dot_product(vec2, vec2))

def find_closest(word_index, vectors, number_closest=10):
    list1 = []
    query_vector = vectors[word_index]
    for index, vector in enumerate(vectors):
        if not np.array_equal(vector, query_vector):
            dist = cosine_similarity(vector, query_vector)
            list1.append([dist, index])
    return sorted(list1, reverse=True)[:number_closest]

word_input = st.text_input("🔍 Entrez un mot pour voir les mots les plus proches :")
number_input = st.slider("📏 Nombre de mots similaires à afficher :", 1, 20, 10)

if word_input:
    word = word_input.lower().strip()
    if word not in word2idx:
        st.error(f"❌ Le mot '{word}' n'est pas dans le vocabulaire du modèle.")
    else:
        index_closest = find_closest(word2idx[word], vectors, number_input)
        st.subheader(f"🔗 Mots les plus proches de : **{word}**")
        for score, idx in index_closest:
            st.markdown(f"- **{idx2word.get(idx, '[UNK]')}** — Similarité : `{score:.4f}`")
