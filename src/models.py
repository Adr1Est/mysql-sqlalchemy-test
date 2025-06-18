# Modelos de SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey
from typing import List, Optional

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)

    favorite_artists: Mapped[List["Artist"]] = relationship(
        "Artist", secondary="fav_artists", back_populates="fans"
    )
    
    def serialize(self):
        return{
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }

class Artist(db.Model):
    __tablename__ = 'artist'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    listeners: Mapped[Optional[int]] = mapped_column(Integer)
    image: Mapped[Optional[str]] = mapped_column(String(255))
    genre: Mapped[str] = mapped_column(String(120), nullable=False)

    albums: Mapped[List["Album"]] = relationship(
        "Album", back_populates="artist", cascade="all, delete-orphan"
    )
    fans: Mapped[List["User"]] = relationship(
        "User", secondary="fav_artists", back_populates="favorite_artists"
    )

class Album(db.Model):
    __tablename__ = 'album'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    image: Mapped[Optional[str]] = mapped_column(String(255))
    artist_id: Mapped[Optional[int]] = mapped_column(ForeignKey('artist.id', ondelete="CASCADE"))

    artist: Mapped["Artist"] = relationship(back_populates="albums")
    songs: Mapped[List["Song"]] = relationship(
        "Song", back_populates="album", cascade="all, delete-orphan"
    )

class Song(db.Model):
    __tablename__ = 'song'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    album_id: Mapped[Optional[int]] = mapped_column(ForeignKey('album.id', ondelete="CASCADE"))
    duration: Mapped[int] = mapped_column(nullable=False)
    preview: Mapped[Optional[str]] = mapped_column(String(255))

    album: Mapped["Album"] = relationship(back_populates="songs")

class FavArtists(db.Model):
    __tablename__ = 'fav_artists'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.id', ondelete="CASCADE"), primary_key=True)