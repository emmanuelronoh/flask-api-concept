from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=True)  
    bio = db.Column(db.Text, nullable=True)      

    # Relationship to Music
    music_items = db.relationship('Music', backref='artist_ref', lazy=True)

    def artist_serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,  
            'bio': self.bio,      
            'music': [music.music_serializer() for music in self.music_items]
        }

class Music(db.Model):
    __tablename__ = "music"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    album_image = db.Column(db.Text)
    album_link = db.Column(db.Text)

    def music_serializer(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist_id': self.artist_id,
            'album_image': self.album_image,
            'album_link': self.album_link
        }
