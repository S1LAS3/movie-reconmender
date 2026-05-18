# codigo para criação de tabelas no postgres
import os
import sys

# Descobre o caminho da raiz do projeto e avisa o Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# importa as coisas necessarias
# base e engine das bibliotecas
from app.database.connection import engine, Base

# modelos de tabelas
from app.models import user, movie, rating

Base.metadata.create_all(bind=engine)