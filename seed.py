from models import Music, Artist, db
from app import app

with app.app_context():
    artist1 = Artist(name="Testing Artist", genre="Pop", bio="A popular music artist.")
    artist2 = Artist(name="Testing Artist 2", genre="Rock", bio="A rock music sensation.")

    db.session.add(artist1)
    db.session.add(artist2)

    db.session.commit()

    music1 = Music(title="test", artist_id=artist1.id,
                   album_image="testing", album_link="testing")
    music2 = Music(title="test2", artist_id=artist2.id,
                   album_image="testing2", album_link="testing2")

    db.session.add(music1)
    db.session.add(music2)

    db.session.commit()

    print("Seeding completed!")
