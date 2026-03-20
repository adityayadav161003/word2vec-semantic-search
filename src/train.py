import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

nltk.download('punkt')

# Load dataset (fixed encoding)
df = pd.read_csv("../data/FA-KES-Dataset.csv", encoding='latin1')

# Use main text column
text_data = df['article_content'].astype(str)

# Cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return word_tokenize(text)

# Apply preprocessing
print("🔄 Cleaning data...")
processed_data = [clean_text(text) for text in text_data]

# Train model
print("🚀 Training Word2Vec model...")
model = Word2Vec(
    sentences=processed_data,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4
)

# Save model
model.save("../models/word2vec.model")

print("✅ Model trained and saved successfully!")