from flask import Flask, request, jsonify, render_template
import sqlite3
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

OMDB_API_KEY = os.getenv('OMDB_API_KEY')

def init_db():
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS watchlist
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         imdb_id TEXT NOT NULL,
         poster TEXT,
         added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'No search query provided'}), 400
    
    params = {
        'apikey': OMDB_API_KEY,
        's': query,
        'type': 'movie'
    }
    
    response = requests.get("http://www.omdbapi.com/", params=params)
    return jsonify(response.json())

@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('SELECT * FROM watchlist ORDER BY added_date DESC')
    movies = [{'id': row[0], 'title': row[1], 'imdb_id': row[2], 'poster': row[3], 'added_date': row[4]} 
              for row in c.fetchall()]
    conn.close()
    return jsonify(movies)

@app.route('/api/watchlist', methods=['POST'])
def add_to_watchlist():
    data = request.json
    if not all(k in data for k in ('title', 'imdb_id', 'poster')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('INSERT INTO watchlist (title, imdb_id, poster) VALUES (?, ?, ?)',
              (data['title'], data['imdb_id'], data['poster']))
    conn.commit()
    movie_id = c.lastrowid
    conn.close()
    
    return jsonify({'id': movie_id, 'message': 'Movie added successfully'}), 201

@app.route('/api/watchlist/<int:movie_id>', methods=['DELETE'])
def remove_from_watchlist(movie_id):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('DELETE FROM watchlist WHERE id = ?', (movie_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Movie removed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
