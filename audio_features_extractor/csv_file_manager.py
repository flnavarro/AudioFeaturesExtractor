import csv


class CsvFileManager(object):

    def __init__(self, path, input_name, delimiter, output_name):
        self.path = path
        self.input_name = input_name
        self.delimiter = delimiter
        self.output_name = output_name

    def get_tracks_from_input_file(self):
        tracks = []
        input_file_path = self.path + self.input_name

        # Open input csv file and create a list of tracks
        with open(input_file_path) as csvfile:
            print('Reading input csv file...')
            reader = csv.DictReader(csvfile, delimiter=self.delimiter)

            for row in reader:
                tracks.append(
                    {
                        'artist': row['artist'],
                        'title': row['title'],
                        'year': row['year'],
                        'spotify_id': row['id'],
                        'genre': row['genre'],
                        'language': row['language']
                    }
                )
        return tracks

    def save_output_file_from_track_list(self, tracks):
        output_file_path = self.path + self.output_name

        # Receive a list of tracks and save it into the output csv file
        with open(output_file_path, 'w') as csvfile:
            print('Saving output csv file...')

            fieldnames = [
                'artist', 'title', 'year', 'id', 'popularity',
                'acousticness', 'danceability', 'energy', 'instrumentalness',
                'mode', 'tempo', 'valence', 'duration_ms', 'preview_url',
                'genre', 'language'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=self.delimiter)

            writer.writeheader()
            for track in tracks:
                writer.writerow({
                    'artist': track['artist'],
                    'title': track['title'],
                    'year': track['year'],
                    'id': track['spotify_id'],
                    'popularity': track['popularity'],
                    'acousticness': track['acousticness'],
                    'danceability': track['danceability'],
                    'energy': track['energy'],
                    'instrumentalness': track['instrumentalness'],
                    'mode': track['mode'],
                    'tempo': track['tempo'],
                    'valence': track['valence'],
                    'duration_ms': track['duration_ms'],
                    'preview_url': track['preview_url'],
                    'genre': track['genre'],
                    'language': track['language']
                })
