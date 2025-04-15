from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('books.csv')
df['description'] = df['description'].fillna('')

# TF-IDF vectorizer on book descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    mood = request.form['mood']
    mood_vec = tfidf.transform([mood])
    sim_scores = cosine_similarity(mood_vec, tfidf_matrix).flatten()
    top_indices = sim_scores.argsort()[-5:][::-1]
    recommendations = df.iloc[top_indices][['title', 'authors']].to_dict(orient='records')

    result_html = '<h2>Top Book Suggestions for your Mood:</h2><ul>'
    for book in recommendations:
        result_html += f"<li><strong>{book['title']}</strong> by {book['authors']}</li>"
    result_html += '</ul><br><a href="/">Back</a>'
    return result_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
