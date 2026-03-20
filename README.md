# 🧠 Word2Vec Semantic Search (Fake News Dataset)

An NLP-based project that uses **Word2Vec** to learn semantic relationships between words from a fake news dataset and perform **context-aware similarity search**.

---

## 🚀 Overview

This project demonstrates how machine learning models can understand **contextual meaning** of words rather than just exact matches. Using Word2Vec, words are converted into vector representations, enabling semantic search and analogy tasks.

---

## ✨ Features

* 📊 Text preprocessing using NLTK
* 🧠 Word2Vec model training using Gensim
* 🔍 Semantic similarity search
* ➕ Word analogy using vector arithmetic
* 💻 Interactive CLI interface

---

## 📊 Sample Results

### Input:

```
attack
```

### Output:

```
- suspected (0.814)
- bombing (0.802)
- exploded (0.781)
- car (0.814)
- double (0.784)
```

👉 The model captures **contextual meaning**, not just keyword matching.

---

## 🧠 How It Works

1. Raw text is cleaned and tokenized using NLTK
2. Word2Vec model is trained on the dataset
3. Each word is converted into a numerical vector
4. Cosine similarity is used to find similar words

👉 Words appearing in similar contexts have similar vector representations.

---

## 📂 Project Structure

```
word2vec-semantic-search/
│
├── src/
│   ├── train.py        # Train Word2Vec model
│   ├── inference.py    # CLI for semantic search
│   ├── check.py        # Dataset validation
│
├── models/             # Saved model (ignored in Git)
├── data/               # Dataset (ignored if large)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/adityayadav161003/word2vec-semantic-search.git
cd word2vec-semantic-search

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Training the Model

```bash
cd src
python train.py
```

---

## 🔍 Running Semantic Search

```bash
python inference.py
```

### Example:

```
Enter a word: city

Similar words:
- countryside (0.966)
- eastern (0.953)
- town (0.943)
- capital (0.940)
```

---

## 🧪 Word Analogy Example

```
king - man + woman ≈ queen
```

👉 Demonstrates how Word2Vec captures relationships using vector math.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NLTK
* Gensim (Word2Vec)

---

## 📌 Limitations

* Vocabulary depends on dataset size
* Some common words may not appear due to preprocessing
* Model is domain-specific (news dataset)

---

## 🚀 Future Improvements

* 🌐 Add Streamlit web interface
* 🧹 Improve preprocessing (lemmatization, stopwords removal)
* 📦 Use pre-trained embeddings (GloVe, FastText)
* 📊 Add visualization (t-SNE / PCA)

---

## 👨‍💻 Author

**Aditya Yadav**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
