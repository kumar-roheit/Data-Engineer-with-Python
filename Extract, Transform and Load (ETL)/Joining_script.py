# Task 1: Take the mean rating per film_id, and assign the result to ratings_per_film_df.
ratings_per_film_df = rating_df.groupBy('film_id').mean('film_id')

# Task 2: Join the tables film_df and ratings_per_film_df
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    film_df.film_id==ratings_per_film_df.film_id
)

# Task 3: Display the 5 first results
print(film_df_with_ratings.show(5))
