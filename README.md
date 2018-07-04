# AudioFeaturesExtractor

Given a csv formatted list of tracks as an input, this script creates an output with additional track data and audio features from Spotify. Input file needs to contain 6 fields: *artist, title, year, id, genre, language*. The file *input_list_example.csv* from *examples* folder in this repository shows an example of the input allowed by the script.

The output file will contain 16 fields *(artist, title, year, id, popularity, acousticness, danceability, energy, instrumentalness, mode, tempo, valence, duration_ms, preview_url, genre, language)* for each of the tracks from the input file.


Example of use with args input:  
<sup>
python main.py -path /Users/username/Desktop/AudioFeaturesExtractor/  
-input_filename input_list_example.csv -input_delimiter semicolon -output_filename output_tracks.csv  
-spotify_client_id SPOTIFY_CLIENT_ID -spotify_client_secret SPOTIFY_CLIENT_SECRET
</sup>

**-path**  
Path where input csv file is read and output csv file will be stored.

**-input_filename**  
Input csv filename (including extension).

**-input_delimiter**  
Csv delimiter for input file: specify 'comma' or 'semicolon'.

**-output_filename**  
Output csv filename (including extension).

**-spotify_client_id**  
Specify your Spotify Client ID.

**-spotify_client_secret**  
Specify your Spotify Client Secret.
