import os
import pandas as pd
import numpy as np
from datetime import date, timedelta
from tqdm import tqdm
from API import API
from imdb import *

api = API()




### Update movies

movies = []


links = pd.read_csv('../ml-latest-small/links.csv')
ratings = pd.read_csv('../ml-latest-small/ratings.csv')

def update_movies(API, movies_id):

    for i in tqdm(range(len(movies_id))):
        movie_id = movies_id[i]
        movie_details = API.get_movie_details(movie_id=movie_id)

        movie_credits = API.get_movie_credits(movie_id=movie_id)

        imdbId = str(list(links[links.tmdbId==movie_id].imdbId)[0]).zfill(7)

        imdb_rating, imdb_number_of_votes, imdb_budget, imdb_gross = get_all_data(imdbId)

        ml_rating = links.where(links.tmdbId.isin([movie_id])).merge(ratings, on='movieId').groupby('tmdbId').mean().rating.values[0]

        _movie = {
            'MovieID': movie_id,
            'TMDBRating': movie_details['vote_average'],
            'IMDBRating': imdb_rating,
            'MovieLensRating': ml_rating,
            'Revenue': movie_details['revenue'] if movie_details['revenue']  != 0  else imdb_gross,
            'Budget': movie_details['budget'] if movie_details['budget'] != 0 else imdb_budget,
            'Popularity': movie_details['popularity'],
            'NumberOfCrewMembers': len(movie_credits['crew']),
            'NumberOfActors': len(movie_credits['cast']),
            'RuntimeInMinutes': movie_details['runtime'],
            'CountryCode': movie_details['production_countries'][0]['iso_3166_1'] if len(movie_details['production_countries']) > 0 else None,
            'UpdateDate': date.today() # + timedelta(days=1)
            # dodawanie tego samego dnia update'a nic nie wrzuca do bazy (to samo id i to samo UpdateDateID)
        }
        movies.append(_movie)

    # after going after all movie ids
    os.makedirs('./UpdateData', exist_ok=True)
    
    pd.DataFrame(movies).to_csv(f'./UpdateData/movies.csv', index=False)


try:
    movies_id = list(pd.read_csv('./UpdateData/currentMovieID.csv', header=None)[0])
except:
    movies_id = []


update_movies(api, movies_id)