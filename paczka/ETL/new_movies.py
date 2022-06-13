import os
import pandas as pd
import numpy as np
from datetime import date
from tqdm import tqdm
from API import API
from imdb import *

api = API()



### Add movies (Insert)

movies = []
movieDetails = []
moviePeople = []
people = []





links = pd.read_csv('../ml-latest-small/links.csv')
ratings = pd.read_csv('../ml-latest-small/ratings.csv')


def insert_movies(API, movies_id, people_id = []):

    # genderNameEncoder = {
    #     0: 'Mezczyzna',
    #     1: 'Kobieta',
    #     2: 'Nieznana'
    # }

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
            'UpdateDate': date.today()#.strftime('%Y%m%d')
        }
        movies.append(_movie)

        _movieDetail = {
            'MovieID': movie_id,
            'MovieTitle': movie_details['original_title'],
            'OriginalLanguageCode': movie_details['original_language'], # en (need to decode) (countries?)
            'ReleaseDate': movie_details['release_date'], #.replace('-','') if movie_details['release_date'] else '99991231', # 1995-10-30 -> YYYYMMDD 19951030
            'Adult': movie_details['adult'], #'Tak' if movie_details['adult'] else 'Nie', # False / True -> 'Nie' / 'Tak'
            'PrimaryGenreName': movie_details['genres'][0]['name'] if len(movie_details['genres'])>0 else 'Nieznane',
            'SecondaryGenreName': movie_details['genres'][1]['name'] if len(movie_details['genres'])>1 else 'Nieznane',
            'MinorGenreName': movie_details['genres'][2]['name'] if len(movie_details['genres'])>2 else 'Nieznane'
        }
        movieDetails.append(_movieDetail)

        for person in movie_credits['cast'] + movie_credits['crew']:

            if person['id'] in people_id:
                continue
            else:

                person_details = API.get_person_details(person['id'])
                _person = {
                    'PersonID': person_details['id'],
                    'Name': person_details['name'],
                    'Birthday': person_details['birthday'], #.replace('-','') if person_details['birthday'] else '99991231', # 1995-10-30 -> YYYYMMDD 19951030,
                    'KnownFor': person_details['known_for_department'],
                    'Deathday': person_details['deathday'], #.replace('-','') if person_details['deathday'] else '99991231', #None
                    'Gender': person_details['gender'],#genderNameEncoder[person_details['gender']],
                    'IMDBID': person_details['imdb_id'], # None ? is that allowed? replacement?
                    'Popularity': person_details['popularity']
                }

                people.append(_person)

                people_id.append(person['id'])
                
                _moviePerson = {
                    'MovieID': movie_id,
                    'PersonID': person_details['id'],
                    'PopularityOnRelease': person['popularity'],
                    'Job': person['job'] if 'job' in person else 'Actor',
                    'Department': person['department'] if 'department' in person else 'Acting'
                }

                moviePeople.append(_moviePerson)

    # after going after all movie ids
    os.makedirs('./Data', exist_ok=True)
    
    pd.DataFrame(movies).to_csv(f'./Data/movies.csv', index=False)
    pd.DataFrame(movieDetails).to_csv(f'./Data/movieDetails.csv', index=False)
    pd.DataFrame(people).to_csv(f'./Data/people.csv', index=False)
    pd.DataFrame(moviePeople).to_csv(f'./Data/moviePeople.csv', index=False)



movies_id = list(pd.read_csv('./Data/newMovieID.csv', header=None)[0].astype(int))
try:
    people_id = list(pd.read_csv('./Data/currentPeopleID.csv', header=None)[0])
except:
    people_id = []

insert_movies(api, movies_id, people_id)