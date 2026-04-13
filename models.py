from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Tabela de asssociaçao: muitos para muitos entre playlist e sons
playlist_song = db.Table('playlist_song', 
                         db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
                         db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
                         )
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento
    songs = db.relationship('song', backref='owner', lazy=True)
    playlist = db.relationship('Playlist', backref='owner', lazy=True)

    def to_dict(self): 
        return {
            "id": self.id, "title": self.title, "artist": self.artist,
            "album": self.album, "duration": self.duration,
            "genre": self.genre, "url": self.url,
            "added_by": self.owner.username
        }
    










