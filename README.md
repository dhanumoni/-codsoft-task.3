# -codsoft-task.3
🎯 What is a Recommendation System?

A recommendation system is a tool that helps users find items they might like — such as movies, books, songs, or products — based on data like:

What they liked before

What similar users liked

Or item similarities (e.g., same genre, same author)



---

🔍 Types of Recommendation Systems

1. Content-Based Filtering

Recommends items similar to what the user liked.

Based on item features like genre, description, etc.

Example: If you liked "Iron Man", it may suggest "Avengers" (same genre/actor).


2. Collaborative Filtering

Recommends items based on similar users' behavior.

Example: "Users who watched X also liked Y".

It doesn't need item features — just user-item interactions (e.g., ratings).



---

✅ Simple Example – Content-Based Movie Recommendation (Python)

Let’s create a basic content-based movie recommender.

# Simple content-based recommendation system

# Sample movie data
movies = {
    'Iron Man': ['Action', 'Adventure', 'Sci-Fi'],
    'Avengers': ['Action', 'Adventure', 'Sci-Fi'],
    'Titanic': ['Romance', 'Drama'],
    'Notebook': ['Romance', 'Drama'],
    'John Wick': ['Action', 'Thriller'],
    'La La Land': ['Romance', 'Musical']
}

# Function to recommend movies
def recommend(user_likes):
    recommendations = {}
    for movie, genres in movies.items():
        score = len(set(user_likes).intersection(genres))
        if score > 0:
            recommendations[movie] = score

    # Sort by highest score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_recommendations]

# User input (what genres they like)
user_preferences = ['Romance', 'Drama']

# Get recommendations
suggestions = recommend(user_preferences)

print("Recommended Movies:")
for movie in suggestions:
    print("-", movie)

🧠 How it works:

The system checks which movie genres match the user’s preferences.

It counts the number of matching genres.

Then, it recommends movies with the highest match.



---

🧩 Collaborative Filtering (Concept Only)

Imagine this table:

User	Liked "Titanic"	Liked "Iron Man"	Liked "Notebook"

A	✅	❌	✅
B	✅	✅	❌


If you’re User C, and you liked "Titanic", we look at similar users (A and B).

Since User A also liked "Notebook", we can recommend "Notebook" to User C.


👉 You can implement this using pandas + cosine similarity or with scikit-learn.


---

📌 Summary

Method	Based On	Needs Item Features?	Good For

Content-Based	Item similarity	✅ Yes	Niche items
Collaborative	User behavior	❌ No	Popular items, community-based



---

Would you like an example of collaborative filtering using a real dataset (like MovieLens) with Python and pandas?
