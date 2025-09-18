import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SearchEngine:
    def __init__(self):
        self.tfidf_vectorizer = None
        self.tfidf_matrix = None
        self.documents = None
        self.load_models()
    
    def load_models(self):
        data_dir = './data'
        #print("Data Directory: ", os.path.abspath(data_dir))
        try:
            with open(os.path.join(data_dir, "tfidf_vectorizer.pkl"), 'rb') as f:
                self.tfidf_vectorizer = pickle.load(f)
            with open(os.path.join(data_dir, "tfidf_matrix.pkl"), 'rb') as f:
                self.tfidf_matrix = pickle.load(f)
            with open(os.path.join(data_dir, "documents.pkl"), 'rb') as f:
                self.documents = pickle.load(f)
            print("Models loaded successfully\n\n")
            
        except FileNotFoundError:
            print("Error: File not found\n\n")
            self.tfidf_vectorizer, self.tfidf_matrix, self.documents = None, None, None
            
            
    def search(self, query, top_n=10):
        
        if self.tfidf_vectorizer is None or self.tfidf_matrix is None or self.documents is None:
            print("Error: Models not loaded. Cannot perform search.")
            return []
        
        query_vec = self.tfidf_vectorizer.transform([query])
        
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-top_n:][::-1] #from -10 to -1, [::-1] reverses them to desc order
        
        results = []
        
        for i in top_indices:
            score = similarities[i]
            
            if score > 0:
                results.append({
                    "id": int(i),
                    "score": float(score),
                    "content" : self.documents[i]
                })
            
        return results
    
    
print("Initializing Search Engine")
search_engine = SearchEngine()