from abc import ABC
from concert_tracker.repo.setlist_api_repo import SetlistFmApiRepo


class SetlistFmImporter(ABC):
    def __init__(self):
        self.repo = SetlistFmApiRepo()
        self.search_field = ''
        self.endpoint_url = ''
        # self.query_filterspi = dict()
        self.extract_field_mapping = {
            'mbid': 'id',
            'name': 'name',
            'desc': 'disambiguation',
            'url': 'url',
        }

    # TODO: sort out setting filters & calling api
    # TODO: set up GitHub repo
    @property
    def query_filters(self):
        return dict()

    def run(self, band):
        print(f'Searching {self.search_field}: {band}')
        try:
            response = self.get_api_response()
            details = self.extract_fields(response)
        except:
            user_input = input(f'{band} not found. Please try different name: ')
            if user_input and user_input != '':
                self.run(user_input)
            else:
                return
        print('run loader')

    def get_api_response(self, band_name):
        querystring = {
            "artistName": band_name,
            "p": 1,
            "sort": "sortName",
        }
        response = self.repo.call_api(endpoint_url=self.endpoint_url, params=querystring)
        return response

    def extract_fields(self, response):
        extract_dict = dict()
        for field, mapping in self.extract_field_mapping:
            extract_dict[mapping] = response[self.search_field][0][field]
        return extract_dict

