movies = [
    {"title": "Inception", "genres": ["Sci-Fi", "Thriller"]},
    {"title": "Titanic", "genres": ["Romance", "Drama"]},
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Avengers: fire", "genres": ["Action", "Sci-Fi"]},
    {"title": "The Notebook", "genres": ["Romance", "Drama"]},
    {"title": "Interstellar", "genres": ["Sci-Fi", "Adventure", "Drama"]},
    {"title": "The mersal", "genres": ["Crime", "Drama"]},
]
user_preferences = ["Sci-Fi", "Action"]
def get_similarity_score(movie_genres, user_genres):
    return len(set(movie_genres) & set(user_genres))
def recommend_movies(movies, user_preferences, top_n=3):
    scored_movies = []
    for movie in movies:
        score = get_similarity_score(movie["genres"], user_preferences)
        scored_movies.append((movie["title"], score))
    scored_movies.sort(key=lambda x: x[1], reverse=True)
    recommendations = [title for title, score in scored_movies if score > 0][:top_n]

    return recommendations
recommended = recommend_movies(movies, user_preferences)
print("Recommended Movies:")
for movie in recommended:
    print(f"- {movie}")
