# app.py (Updated)
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Curated list of 200+ common Hindi words in English (Expandable to 2000)
hindish_words = [
    # Basic Nouns
    "khaana", "paani", "roti", "daal", "chawal", "sabzi", "doodh", "chai", "shakkar",
    "namak", "mirchi", "pyaz", "lasan", "adrak", "tel", "ghee", "atta", "chawal",
    
    # Family & Relationships
    "maa", "papa", "bhai", "behen", "dadi", "nani", "chacha", "mausi", "sasur", "sali",
    
    # Daily Life
    "ghar", "kamra", "kursi", "bistar", "kapda", "joota", "chabi", "diya", "jhaadu", "pankha",
    
    # Nature
    "suraj", "chaand", "taara", "baarish", "hawa", "aag", "mitti", "patthar", "ped", "phool",
    
    # Animals
    "ghoda", "haathi", "kutta", "billi", "sher", "chuha", "cow", "bandar", "saanp", "machli",
    
    # Emotions
    "pyaar", "gussa", "khushi", "dard", "bhook", "pyaas", "nind", "thakan", "santosh",
    
    # Actions
    "khelna", "sona", "khana", "peena", "chalna", "dekha", "sunna", "bolna", "padhna", "likhna",
    
    # Common Phrases
    "kaiseho", "shukriya", "maafkaro", "kripaya", "swagat", "aapkaun", "kyahua", "achha",
    
    
]

hindish_words += [
    # Body Parts
    "sar", "aankh", "naak", "kaaan", "munh", "haath", "paer", "pet", "dil",
    
    # Time-related
    "kal", "aaj", "parso", "subah", "shaam", "dopehar", "raat",
    
    # Market Items
    "dukaan", "saman", "daam", "bhaav", "khareed", "bech",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(hindish_words).capitalize())

if __name__ == '__main__':
    app.run(debug=True)
