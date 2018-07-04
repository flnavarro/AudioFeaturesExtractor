# -*- coding: utf-8 -*-
import argparse

from csv_file_manager import CsvFileManager
from spotify_manager import SpotifyManager


class AudioFeaturesExtractor(object):

    def __init__(self, folder_path, filename_input, delimiter_input, filename_output, client_id, client_secret):
        self.csv_manager = CsvFileManager(folder_path, filename_input, delimiter_input, filename_output)
        self.spotify_manager = SpotifyManager(client_id, client_secret)

    def extract_features(self):
        csv_track_list = self.csv_manager.get_tracks_from_input_file()
        track_list = self.spotify_manager.add_data_and_features_to_track_list(csv_track_list)
        self.csv_manager.save_output_file_from_track_list(track_list)


class InputParser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Get audio features & track data for a csv list.")
        self.path = ''
        self.input_filename = ''
        self.input_delimiter = ''
        self.output_filename = ''
        self.spotify_client_id = ''
        self.spotify_client_secret = ''

    def add_arguments(self):
        self.parser.add_argument('-path', action='store', dest='path', required=True,
                                 help='Path where input csv file is read and output csv file will be stored.')
        self.parser.add_argument('-input_filename', action='store', dest='input_filename', required=True,
                                 help='Input csv filename (including extension).')
        self.parser.add_argument('-input_delimiter', action='store', dest='input_delimiter', required=True,
                                 help="Csv delimiter for input file: specify 'comma' or 'semicolon'.")
        self.parser.add_argument('-output_filename', action='store', dest='output_filename', required=True,
                                 help='Output csv filename (including extension).')
        self.parser.add_argument('-spotify_client_id', action='store', dest='spotify_client_id', required=True,
                                 help='Specify your Spotify Client ID.')
        self.parser.add_argument('-spotify_client_secret', action='store', dest='spotify_client_secret', required=True,
                                 help='Specify your Spotify Client Secret.')

    def parse_input(self):
        self.add_arguments()
        args = self.parser.parse_args()
        self.path = args.path
        if self.path[:-1] != '/':
            self.path += '/'
        self.input_filename = args.input_filename
        if args.input_delimiter == 'comma':
            self.input_delimiter = ','
        else:
            self.input_delimiter = ';'
        self.output_filename = args.output_filename
        self.spotify_client_id = args.spotify_client_id
        self.spotify_client_secret = args.spotify_client_secret


args_input = True

if args_input:
    input_parser = InputParser()
    input_parser.parse_input()
    path = input_parser.path
    input_filename = input_parser.input_filename
    input_delimiter = input_parser.input_delimiter
    output_filename = input_parser.output_filename
    spotify_client_id = input_parser.spotify_client_id
    spotify_client_secret = input_parser.spotify_client_secret
else:
    path = '/Users/username/Desktop/AudioFeaturesExtractor/'
    input_filename = 'input_list_example.csv'
    input_delimiter = ';'
    output_filename = 'tracks_with_features.csv'
    spotify_client_id = ''
    spotify_client_secret = ''

extractor = AudioFeaturesExtractor(
        path, input_filename, input_delimiter, output_filename, spotify_client_id, spotify_client_secret
    )
extractor.extract_features()
