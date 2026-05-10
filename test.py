from app.services.recommendation import recommend_movies

recs = recommend_movies(3)

print("Recomendações:", recs)