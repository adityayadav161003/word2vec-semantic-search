from gensim.models import Word2Vec

# Load trained model
model = Word2Vec.load("../models/word2vec.model")

print("Vocab size:", len(model.wv.index_to_key))
print("Sample words:", model.wv.index_to_key[:30])

# Find similar words
def find_similar(word):
    if word not in model.wv:
        return f"'{word}' not in vocabulary"
    
    results = model.wv.most_similar(word, topn=5)
    
    formatted = []
    for word, score in results:
        formatted.append(f"{word} ({score:.3f})")
    
    return formatted

# Word analogy (vector math)
def word_math(a, b, c):
    try:
        results = model.wv.most_similar(positive=[a, c], negative=[b], topn=5)
        return results
    except:
        return "Error with given words"

# CLI interface
if __name__ == "__main__":
    print("🔍 Word2Vec Semantic Search")
    
    while True:
        word = input("\nEnter a word (or type 'exit'): ").strip().lower()
        
        if word == "exit":
            break
        
        results = find_similar(word)

        print("\nSimilar words:")
        
        if isinstance(results, str):
            print(results)
        else:
            for w in results:
                print(" -", w)

    print("\n📌 Vector Example:")
    print("king - man + woman =")
    print(word_math("king", "man", "woman"))
    