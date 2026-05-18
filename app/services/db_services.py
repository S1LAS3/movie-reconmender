from app.database.connection import SessionLocal
from app.models.user import User
from app.models.movie import Movie
from app.models.rating import Rating

def get_session():
    return SessionLocal()



def create_user(name):
    session = get_session()

    user = User(name=name)
    session.add(user)
    session.commit()

    session.close()

def create_movie(title,genre):
    session = get_session()

    movie = Movie(title = title, genre = genre)
    session.add(movie)
    session.commit()

    session.close() 

def add_rating(user_id, movie_id, rating_value):
    session = get_session()

    rating = Rating(
        User_id = user_id,
        Movie_id = movie_id,
        rating = rating_value
    )

    session.add(rating)
    session.commit()
    session.close()


def get_users():
    session = get_session()
    users = session.query(User).all()
    session.close()
    return users

def get_movies():
    session = get_session()
    movies = session.query(Movie).all()
    session.close()
    return movies