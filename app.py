# app.py (Updated)
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Curated list of 200+ common Hindi words in English (Expandable to 2000)
islamic_words = [

    "Zaid Bin Haris",


]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(islamic_words).capitalize())

if __name__ == '__main__':
    app.run(debug=True)
