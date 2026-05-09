from app.services.recommendation import recommend_movies

recs = recommend_movies(1)

print("Recomendações:", recs)