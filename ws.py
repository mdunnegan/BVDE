import sqlite3
import json
from flask import Flask

connection = sqlite3.connect('bvde.db')
app = Flask(__name__)

@app.route('/songsByName/<string:name>', methods = ['GET'])
def getSongsByName(name):
  with sqlite3.connect("bvde.db") as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    rows = cursor.execute("select songs.title, songs.artist, songs.duration, genres.name as genre from songs join genres on songs.genre = genres.id where upper(songs.title) = '" + name.upper() + "'").fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route('/songsByArtist/<string:artist>', methods = ['GET'])
def getSongsByArtist(artist):
  with sqlite3.connect("bvde.db") as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    rows = cursor.execute("select songs.title, songs.artist, songs.duration, genres.name as genre from songs join genres on songs.genre = genres.id where upper(songs.artist) = '" + artist.upper() + "'").fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route('/songsByGenre/<string:genre>', methods = ['GET'])
def getSongsByGenre(genre):
  with sqlite3.connect("bvde.db") as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    rows = cursor.execute("select songs.title, songs.artist, songs.duration, genres.name as genre from songs join genres on songs.genre = genres.id where upper(genres.name) = '" + genre.upper() + "'").fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route('/songsByLength/<int:min>/<int:max>', methods = ['GET'])
def getSongsByLength(min, max):
  with sqlite3.connect("bvde.db") as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    rows = cursor.execute("select songs.title, songs.artist, songs.duration, genres.name as genre from songs join genres on songs.genre = genres.id where songs.duration >= " + str(min) + " and songs.duration <= " + str(max)).fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route('/genres', methods = ['GET'])
def getGenres():
  with sqlite3.connect("bvde.db") as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    rows = cursor.execute("select genres.name as genres, count(songs.title) as count, sum(duration) as total_duration from songs join genres on songs.genre = genres.id group by genres.name").fetchall()
    return json.dumps([dict(ix) for ix in rows])

if __name__ == '__main__':
    app.run(debug=True)

