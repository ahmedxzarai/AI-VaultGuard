import pickle
import math
from urllib.parse import urlparse

class AISentinel:
    def __init__(self, model_path='sentinel_model.pkl'):
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
            print("🧠 AI Sentinel: Upgraded Brain Loaded.")
        except FileNotFoundError:
            self.model = None
            print("⚠️ Warning: sentinel_model.pkl not found.")

    def extract_features(self, url):
        """Must match the training features exactly!"""
        try:
            hostname = urlparse(url).netloc
            length = len(url)
            dots = url.count('.')
            hyphens = url.count('-')
            is_https = 1 if url.startswith('https') else 0
            
            keywords = ['login', 'verify', 'secure', 'update', 'banking', 'paypa1', 'signin', 'account']
            keyword_count = sum(1 for word in keywords if word in url.lower())
            
            subdomains = hostname.count('.')
            prob = [float(url.count(c)) / len(url) for c in dict.fromkeys(list(url))]
            entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
            
            return [length, dots, hyphens, is_https, keyword_count, subdomains, entropy]
        except:
            return [0, 0, 0, 0, 0, 0, 0]

    def analyze_url(self, url):
        if self.model is None:
            return 0.0
        
        features = [self.extract_features(url)]
        # Get the probability of it being "Class 1" (Phishing)
        prediction_prob = self.model.predict_proba(features)[0][1]
        return prediction_prob