import requests
from config.settings import API_KEY

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {API_KEY}'}

    def get_data(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
