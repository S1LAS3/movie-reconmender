# app/services/recommendation.py

# Lista de filmes
movies = [
    {"id": 1, "title": "Matrix", "genre": "acao"},
    {"id": 2, "title": "Interestelar", "genre": "ficcao"},
    {"id": 3, "title": "Vingadores", "genre": "acao"},
    {"id": 4, "title": "Toy Story", "genre": "animacao"},
]

# Usuários
users = [
    {"id": 1, "name": "Silas"},
    {"id": 2, "name": "João"},
]

# Avaliações
ratings = [
    {"user_id": 1, "movie_id": 4, "rating": 5},
    {"user_id": 1, "movie_id": 3, "rating": 4},
    {"user_id": 2, "movie_id": 2, "rating": 5},
]

#função para percorrer a lista de avaliações (ratings) e retorna somente as que foram feitas pelo usuario aparti de seu user_id
def get_user_ratings(user_id):
    return [r for r in ratings if r["user_id"] == user_id and r["rating" >= 4]]



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

    return max (genres, key = genres.get)


#retorna uma lista de filmes ja assistidos pelo usuario
def get_watched_movies(user_id):
    return{r["movie_id"] for r in ratings if r["user_id"] == user_id}


def recommend_movies(user_id):
    top_genre = get_top_genres(user_id)

    if not top_genre:
        return[]
    
    watched = get_watched_movies(user_id)

    recommendations = []

    for movie in movies:
        if movie["genre"] == top_genre and movie["id"] not in watched:
            recommendations.append

    return recommendations


