import pandas as pd
import numpy as np
import math
import pickle
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def extract_features(url):
    """Converts a URL string into a list of 7 mathematical features."""
    try:
        url_str = str(url)
        hostname = urlparse(url_str).netloc
        
        # 1. Structural Features
        length = len(url_str)
        dots = url_str.count('.')
        hyphens = url_str.count('-')
        is_https = 1 if url_str.startswith('https') else 0
        
        # 2. Context Features (Keywords)
        keywords = ['login', 'verify', 'secure', 'update', 'banking', 'paypa1', 'signin', 'account']
        keyword_count = sum(1 for word in keywords if word in url_str.lower())
        
        # 3. Complexity Features
        subdomains = hostname.count('.')
        # Entropy calculation (detects 'gibberish' or random strings)
        prob = [float(url_str.count(c)) / len(url_str) for c in dict.fromkeys(list(url_str))]
        entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
        
        return [length, dots, hyphens, is_https, keyword_count, subdomains, entropy]
    except:
        return [0, 0, 0, 0, 0, 0, 0]

def train_model():
    print("📂 Loading dataset...")
    df = pd.read_csv('urldata.csv')
    
    # --- DATA CLEANING & MAPPING ---
    # Convert 'phishing' strings to 1, and everything else (benign, etc.) to 0
    print("🔄 Mapping labels (phishing -> 1, others -> 0)...")
    df['label'] = df['type'].map(lambda x: 1 if str(x).lower() == 'phishing' else 0)
    
    print("🧪 Extracting upgraded features (Processing 400k+ rows)...")
    # This creates the numerical input for the AI
    X = np.array([extract_features(u) for u in df['url']])
    y = df['label'].values
    
    # Split data: 80% for learning, 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("🧠 Training the Random Forest Brain...")
    model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1) # n_jobs=-1 makes it faster
    model.fit(X_train, y_train)
    
    print("\n📊 TRAINING REPORT:")
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    
    # Save the updated brain
    with open('sentinel_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("\n✅ SUCCESS: sentinel_model.pkl is now upgraded with 7 features.")

if __name__ == "__main__":
    train_model()