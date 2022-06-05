import os
import pandas as pd
import numpy as np
from datetime import date
from tqdm import tqdm
from API import API
from imdb import *

api = API()




### Update people

people = []


def update_people(API, people_id):

    for i in tqdm(range(len(people_id))):
        person_id = people_id[i]
        person_details = API.get_person_details(person_id)

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

    # after going after all movie ids
    os.makedirs('./UpdatePeopleData', exist_ok=True)
    
    pd.DataFrame(people).to_csv(f'./UpdatePeopleData/people.csv', index=False)


try:
    people_id = list(pd.read_csv('./UpdatePeopleData/currentPeopleID.csv', header=None)[0])
except:
    people_id = []


update_people(api, people_id)