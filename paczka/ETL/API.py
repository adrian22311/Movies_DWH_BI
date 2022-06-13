import requests
import os
from dotenv import load_dotenv
import time

class API:

    def __init__(self):
        
        load_dotenv() 

        self.url_prefix = "https://api.themoviedb.org/3/"
        self.url_suffix = f"?api_key={os.getenv('API_KEY')}&language=pl-PL"

        self.calls_count = 0

    def api_call(self, url):
        if (self.calls_count + 1) % 20 == 0: 
            # print('Calls count: ', self.calls_count, ". Sleeping")
            time.sleep(2)
        req = requests.get(url)
        
        self.calls_count += 1

        if req.status_code == 200:
            result = req.json()
        else:
            result = None
            print(req.status_code)
            print(req.reason)

        return result
    
    def get_movie_details(self, movie_id):
        url = self.url_prefix + f'movie/{movie_id}' + self.url_suffix

        results = self.api_call(url)
        
        # TODO: select only what we need, 

        return results
    
    def get_movie_credits(self, movie_id):
        url = self.url_prefix + f'movie/{movie_id}/credits' + self.url_suffix

        results = self.api_call(url)

        # TODO: select only what we need, 

        return results

    def get_person_details(self, person_id):
        url = self.url_prefix + f'person/{person_id}' + self.url_suffix

        results = self.api_call(url)

        # TODO: select only what we need

        return results

