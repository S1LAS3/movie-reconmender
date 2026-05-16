from connection import engine, Base
from models import user, movie, ratsing

Base.metadata.create_all(bind=engine)