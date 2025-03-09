from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words(sentences):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(sentences).toarray()
    vocab = vectorizer.get_feature_names_out()
    
    return vectors, vocab

# Example usage
sentences = [
    "I love programming",
    "Python is great for programming",
    "I love Python"
]

vectors, vocabulary = bag_of_words(sentences)

print("Vocabulary:", vocabulary)
print("Vectors:\n", vectors)
