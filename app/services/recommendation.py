# app/services/recommendation.py

# Lista de filmes expandida
# app/services/recommendation.py

movies = [
    {"id": 1, "title": "Matrix", "genre": "acao"},
    {"id": 2, "title": "Interestelar", "genre": "ficcao"},
    {"id": 3, "title": "Vingadores", "genre": "acao"},
    {"id": 4, "title": "Toy Story", "genre": "animacao"},
    {"id": 5, "title": "O Poderoso Chefão", "genre": "drama"},
    {"id": 6, "title": "Invocação do Mal", "genre": "terror"},
    {"id": 7, "title": "Shrek", "genre": "animacao"},
    {"id": 8, "title": "Blade Runner 2049", "genre": "ficcao"},
    {"id": 9, "title": "Batman: O Cavaleiro das Trevas", "genre": "acao"},
    {"id": 10, "title": "Parasita", "genre": "drama"},
    # --- Novos Elementos ---
    {"id": 11, "title": "Duna", "genre": "ficcao"},
    {"id": 12, "title": "Pulp Fiction", "genre": "crime"},
    {"id": 13, "title": "O Iluminado", "genre": "terror"},
    {"id": 14, "title": "Se Beber, Não Case!", "genre": "comedia"},
    {"id": 15, "title": "La La Land", "genre": "musical"},
    {"id": 16, "title": "Spider-Man: No Way Home", "genre": "acao"},
    {"id": 17, "title": "A Viagem de Chihiro", "genre": "animacao"},
    {"id": 18, "title": "Clube da Luta", "genre": "drama"},
    {"id": 19, "title": "O Silêncio dos Inocentes", "genre": "suspense"},
    {"id": 20, "title": "De Volta para o Futuro", "genre": "ficcao"},
    {"id": 21, "title": "Superbad", "genre": "comedia"},
    {"id": 22, "title": "O Rei Leão", "genre": "animacao"},
    {"id": 23, "title": "Mad Max: Estrada da Fúria", "genre": "acao"},
    {"id": 24, "title": "Garota Exemplar", "genre": "suspense"},
    {"id": 25, "title": "Upgrade", "genre": "ficcao"}
]

# Usuários com perfis distintos
users = [
    {"id": 1, "name": "Silas"},
    {"id": 2, "name": "João"},
    {"id": 3, "name": "Maria"},
    {"id": 4, "name": "Fernanda"},
    {"id": 5, "name": "Lucas"},
]

# Avaliações (Ratings de 1 a 5)
ratings = [
    # Silas gosta de Ação e Ficção
    {"user_id": 1, "movie_id": 1, "rating": 5},
    {"user_id": 1, "movie_id": 3, "rating": 4},
    {"user_id": 1, "movie_id": 9, "rating": 5},
    {"user_id": 1, "movie_id": 2, "rating": 4},
    
    # João foca em Ficção e Drama
    {"user_id": 2, "movie_id": 2, "rating": 5},
    {"user_id": 2, "movie_id": 8, "rating": 4},
    {"user_id": 2, "movie_id": 10, "rating": 5},
    
    # Maria gosta de Animação
    {"user_id": 3, "movie_id": 4, "rating": 5},
    {"user_id": 3, "movie_id": 7, "rating": 5},
    {"user_id": 3, "movie_id": 1, "rating": 2}, # Não curte muito ação
    
    # Fernanda gosta de Drama e Terror
    {"user_id": 4, "movie_id": 5, "rating": 5},
    {"user_id": 4, "movie_id": 10, "rating": 4},
    {"user_id": 4, "movie_id": 6, "rating": 5},
    
    # Lucas é fã de Ação, mas odiou um filme específico
    {"user_id": 5, "movie_id": 1, "rating": 4},
    {"user_id": 5, "movie_id": 3, "rating": 2}, # Rating baixo para testar filtros
    {"user_id": 5, "movie_id": 9, "rating": 5},
]


#função para percorrer a lista de avaliações (ratings) e retorna somente as que foram feitas pelo usuario aparti de seu user_id
def get_user_ratings(user_id):
    return [r for r in ratings if r["user_id"] == user_id and r["rating"] >= 4]



#função recebe o id do usuario e retorna quais são e quantas são as avaliações de cada genero feitas pelo usuadrio
def get_favorite_genres(user_id):
    user_ratings = get_user_ratings(user_id)
    genre_cont = {}

    for r in user_ratings:
        movie = next(m for m in movies if m["id"] == r["movie_id"])
        genre = movie["genre"]

        if genre not in genre_cont:
            genre_cont[genre] = 0

        genre_cont[genre] += 1
    
    return genre_cont


#função que recebe o id do usuario o genero com mais avaliações
def get_top_genres(user_id):
    genres = get_favorite_genres(user_id)

    if not genres:
        return None

    top_2 = sorted(genres, key = genres.get, reverse=True)[:2]

    return top_2



#retorna uma lista de filmes ja assistidos pelo usuario
def get_watched_movies(user_id):
    return{r["movie_id"] for r in ratings if r["user_id"] == user_id}


#retorna filmes recomendados pelo genero que o usuario mais deu curtidas
def recommend_movies(user_id):
    top_genre = get_top_genres(user_id)

#caso a lista estiver vazia
    if not top_genre:
        return[]     
      
    watched = get_watched_movies(user_id)
    recommendations = []

#caso a lista tiver um elemento
    if len(top_genre) < 2:
        for movie in movies:
            if movie["genre"] == top_genre[0] and movie["id"] not in watched:
                recommendations.append(movie["title"])

#caso a lista tiver dois elementos
    else:
        for movie in movies:
            if (movie["genre"] == top_genre[0] or movie["genre"] == top_genre[1]) and movie["id"] not in watched:
                recommendations.append(movie["title"])





    return recommendations



