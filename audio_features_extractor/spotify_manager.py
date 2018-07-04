# -*- coding: utf-8 -*-
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyManager(object):
    def __init__(self, spotify_client_id, spotify_client_secret):
        self.client_id = spotify_client_id
        self.client_secret = spotify_client_secret
        self.spotify = None

    def get_token(self):
        print('Getting Spotify client credentials and token...')
        sp_oauth = SpotifyClientCredentials(self.client_id, self.client_secret)
        access_token = sp_oauth.get_access_token()
        self.spotify = spotipy.Spotify(auth=access_token)

    def add_data_and_features_to_track_list(self, track_list):
        track_list_ids = []
        # Get all ids first to make less number of requests
        [track_list_ids.append(track['spotify_id']) for track in track_list]

        max_tracks_per_request = 50  # Max per request (Spotify API)
        current_min_index = 0
        spotify_tracks = []
        spotify_audio_features = []

        self.get_token()
        while current_min_index < len(track_list_ids):
            # 50 tracks by 50 tracks
            if current_min_index + max_tracks_per_request < len(track_list_ids):
                max_index = current_min_index + max_tracks_per_request
            else:
                max_index = len(track_list_ids)

            # To make sure the request is done and the connection is not lost
            request_done = False
            while not request_done:
                try:
                    # Get data and features from Spotify using a list of Spotify IDs
                    print('Getting Spotify data for 50-tracks batch from track list...')
                    track_results = self.spotify.tracks(
                        track_list_ids[current_min_index:max_index]
                    )
                    spotify_tracks += track_results['tracks']
                    print('Getting Spotify audio features for 50-tracks batch from track list...')
                    spotify_audio_features += self.spotify.audio_features(
                        track_list_ids[current_min_index:max_index]
                    )
                    request_done = True
                except:
                    time.sleep(1)
                    self.get_token()

            # Increase the index for next iteration
            current_min_index += max_tracks_per_request

        # Add relevant data and features to existing track list
        print('Adding Spotify data and audio features to track list...')
        for i, track in enumerate(track_list):
            track['popularity'] = spotify_tracks[i]['popularity']
            track['duration_ms'] = spotify_tracks[i]['duration_ms']
            track['preview_url'] = spotify_tracks[i]['preview_url']
            track['acousticness'] = spotify_audio_features[i]['acousticness']
            track['danceability'] = spotify_audio_features[i]['danceability']
            track['energy'] = spotify_audio_features[i]['energy']
            track['instrumentalness'] = spotify_audio_features[i]['instrumentalness']
            track['mode'] = spotify_audio_features[i]['mode']
            track['tempo'] = spotify_audio_features[i]['tempo']
            track['valence'] = spotify_audio_features[i]['valence']

        return track_list

