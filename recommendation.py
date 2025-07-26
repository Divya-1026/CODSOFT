import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'title': [
        'The Max', 'Googly', 'Yajamana', 'Anjaniputra',
        'The Notebook', 'Titanic', 'Avengers', 'Batman Begins'
    ],
    'genre': [
        'action sci-fi', 'action thriller', 'action sci-fi', 'sci-fi drama',
        'romance drama', 'romance drama', 'action superhero', 'action drama'
    ]
}

df = pd.DataFrame(data)
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])
similarity = cosine_similarity(genre_matrix)

def recommend_movie(movie_title):
    movie_title = movie_title.strip().lower()
    titles_lower = df['title'].str.lower()

    if movie_title not in titles_lower.values:
        print("Movie not found in database.")
        return

    idx = titles_lower[titles_lower == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nBecause you watched \"{df['title'][idx]}\", you might also like:")
    for i in scores[1:4]:
        print(" -", df['title'][i[0]])

user_input = input("Enter a movie title: ")
recommend_movie(user_input)