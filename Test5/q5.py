import sqlite3


# -----------------------------------
# 1. Movie Class
# -----------------------------------

class Movie:
    def __init__(self, movie_id, title, genre, rating, watch_count):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch_count = watch_count

    def display(self):
        print(
            self.movie_id,
            self.title,
            self.genre,
            self.rating,
            self.watch_count
        )


# -----------------------------------
# 2. Connect to SQLite Database
# -----------------------------------

conn = sqlite3.connect("movies.db")

cursor = conn.cursor()


# -----------------------------------
# 3. Create Movies Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    rating REAL,
    watch_count INTEGER
)
""")


# -----------------------------------
# 4. Insert Sample Movies
# -----------------------------------

movies = [
    (101, "Inception", "Sci-Fi", 8.8, 9500),
    (102, "Interstellar", "Sci-Fi", 8.7, 12000),
    (103, "The Dark Knight", "Action", 9.0, 15000),
    (104, "Avengers", "Action", 8.0, 18000),
    (105, "Titanic", "Romance", 7.9, 20000),
    (106, "The Notebook", "Romance", 7.8, 8000),
    (107, "The Conjuring", "Horror", 7.5, 10000),
    (108, "Get Out", "Horror", 7.7, 9000),
    (109, "Toy Story", "Animation", 8.3, 11000),
    (110, "Coco", "Animation", 8.4, 13000),
    (111, "Gladiator", "Action", 8.5, 8500),
    (112, "Avatar", "Sci-Fi", 7.9, 17000)
]

cursor.executemany("""
INSERT OR IGNORE INTO movies
(movie_id, title, genre, rating, watch_count)
VALUES (?, ?, ?, ?, ?)
""", movies)

conn.commit()


# -----------------------------------
# 5. Fetch All Movies
# -----------------------------------

cursor.execute("SELECT * FROM movies")

rows = cursor.fetchall()


# -----------------------------------
# 6. Convert Rows into Movie Objects
# -----------------------------------

movie_objects = []

for row in rows:

    movie = Movie(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4]
    )

    movie_objects.append(movie)


print("\nAll Movies:")

for movie in movie_objects:
    movie.display()


# -----------------------------------
# 7. Sort Movies by Rating
# -----------------------------------

movies_by_rating = sorted(
    movie_objects,
    key=lambda movie: movie.rating,
    reverse=True
)

print("\nMovies sorted by Rating:")

for movie in movies_by_rating:
    movie.display()


# -----------------------------------
# 8. Search Movie using Movie ID
# -----------------------------------

movie_id = int(
    input("\nEnter Movie ID to search: ")
)

found_movie = None

for movie in movie_objects:

    if movie.movie_id == movie_id:
        found_movie = movie
        break


if found_movie:

    print("\nMovie Found:")
    found_movie.display()

else:

    print("\nMovie not found.")


# -----------------------------------
# 9. Display Top 10 Highest Rated
# -----------------------------------

print("\nTop 10 Highest-Rated Movies:")

top_10 = movies_by_rating[:10]

for movie in top_10:
    movie.display()


# -----------------------------------
# 10. Most Watched Movie in Each Genre
# Using Dictionary
# -----------------------------------

most_watched = {}

for movie in movie_objects:

    if movie.genre not in most_watched:

        most_watched[movie.genre] = movie

    else:

        if movie.watch_count > most_watched[movie.genre].watch_count:

            most_watched[movie.genre] = movie


print("\nMost Watched Movie in Each Genre:")

for genre, movie in most_watched.items():

    print("\nGenre:", genre)
    movie.display()


# -----------------------------------
# 11. SQL GROUP BY
# -----------------------------------

print("\nMaximum Watch Count in Each Genre:")

cursor.execute("""
SELECT genre, MAX(watch_count)
FROM movies
GROUP BY genre
""")

genre_results = cursor.fetchall()

for row in genre_results:
    print(row[0], row[1])


# -----------------------------------
# 12. Close Database
# -----------------------------------

conn.close()