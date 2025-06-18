# Queries: Funciones para acceder a la base de datos
from models import db, User, Artist, Album, Song

def get_all_users():
    return User.query.all()

def get_artist_by_id(artist_id: int) -> Artist | None: 
    return Artist.query.get(artist_id)

def add_new_user(username, firstname, lastname, email, password, is_active=True):
    new_user = User(
        username=username,
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
        is_active=is_active
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user