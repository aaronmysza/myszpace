from concert_tracker.importer.setlist_fm_importer import SetlistFmImporter


class BandImporter(SetlistFmImporter):
    def __init__(self):
        super().__init__()
        self.search_field = 'artist'
        self.endpoint_url = f'{self.repo.url}/search/artists'
        self.query_filters = {
            "artistName": ''
        }


if __name__ == '__main__':
    importer = BandImporter()
    band = 'Protest the Hero'
    importer.run(band)
