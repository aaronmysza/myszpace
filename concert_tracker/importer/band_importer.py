from concert_tracker.repo.setlist_api_repo import SetlistFmApiRepo


class BandImporter:
    def __init__(self):
        self.repo = SetlistFmApiRepo()

    def run(self, band):
        print(f'Searching band: {band}')
        try:
            band_details = self.get_band_details(band)
        except:
            user_input = input(f'{band} not found. Please try different name: ')
            if user_input and user_input != '':
                self.run(user_input)
            else:
                return
        print('run loader')

    def get_band_details(self, band_name):
        endpoint_url = f'{self.repo.url}/search/artists'
        querystring = {
            "artistName": band_name,
            "p": 1,
            "sort": "sortName",
        }
        response = self.repo.call_api(endpoint_url=endpoint_url, params=querystring)
        details = {
            'id': response['artist'][0]['mbid'],
            'name': response['artist'][0]['name'],
            'desc': response['artist'][0]['disambiguation'],
            'url': response['artist'][0]['url'],
        }
        return details


if __name__ == '__main__':
    importer = BandImporter()
    band = 'Protest the Hero'
    importer.run(band)
