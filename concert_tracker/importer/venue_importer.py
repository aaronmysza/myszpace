from concert_tracker.repo.setlist_api_repo import SetlistFmApiRepo


class VenueImporter:
    def __init__(self):
        self.repo = SetlistFmApiRepo()

    def run(self, venue, city, state):
        print(f'Searching venue: {venue}')
        try:
            venue_details = self.get_venue_details(venue, city, state)
        except:
            user_input = input(f'{venue} not found. Please try different name: ')
            if user_input and user_input != '':
                self.run(user_input)
            else:
                return
        print('run loader')

    def get_venue_details(self, venue, city, state):
        endpoint_url = f'{self.repo.url}/search/venues'
        querystring = {
            "name": venue,
            "cityName": city,
            "state": state,
            "p": 1,
            "sort": "sortName",
        }
        response = self.repo.call_api(endpoint_url=endpoint_url, params=querystring)
        details = {
            'id': response['venue'][0]['id'],
            'name': response['artist'][0]['name'],
            'url': response['artist'][0]['url'],
        }
        return details


if __name__ == '__main__':
    importer = VenueImporter()
    venue = 'The Phoenix'
    city = 'Toronto'
    state = 'Ontario'
    importer.run(venue, city, state)
