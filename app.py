from flask import Flask, jsonify, request
from models import Music, Artist, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://class:group1234@localhost/music_artist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Music API!"

@app.route('/music', methods=['GET'])
def get_music():
    music_items = Music.query.all()
    return jsonify([music_item.music_serializer() for music_item in music_items])

@app.route('/music', methods=['POST'])
def create_music():
    data = request.get_json()
    new_music = Music(
        title=data.get('title'),
        artist_id=data.get('artist_id'),  
        album_image=data.get('album_image'),
        album_link=data.get('album_link')
    )
    db.session.add(new_music)
    db.session.commit()
    return jsonify(new_music.music_serializer()), 201

@app.route('/artists', methods=['GET'])
def get_artists():
    artist_items = Artist.query.all()
    return jsonify([artist.artist_serializer() for artist in artist_items])

@app.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    new_artist = Artist(
        name=data.get('name'),
        genre=data.get('genre'),  
        bio=data.get('bio')       
    )
    db.session.add(new_artist)
    db.session.commit()
    return jsonify(new_artist.artist_serializer()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(port=5000, debug=True)
