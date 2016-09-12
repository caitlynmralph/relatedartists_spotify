# Data Mining Assignment 1
# Uses Spotify API to get user's top played artists and find related artists for each of those artists
# Writes data to spotify_data.csv file
# Code help from https://spotipy.readthedocs.io/en/latest/#
#         and
#            https://github.com/plamere/spotipy

import spotipy

my_artists = []
token = 'BQBwdy3CqQsMvIbBccjsFkg19SRXNVHsrbkTupa1WryEIqgXvDfQDD3-fK-ac8EcP5M_35kTc63jum6G6YQ5T1XeXmazVmnt7SxaFnAndQ40OkV6Nvu1n25lAiOO1qOsIHJlflOh37B8DsYy1LdiljunPJL1w3vIzy6slQ'

sp = spotipy.Spotify(auth=token)
sp.trace = False
times = ['short_term', 'medium_term', 'long_term']
for time in times:
    results = sp.current_user_top_artists(time_range=time, limit=50)
    for i, item in enumerate(results['items']):
        if item not in my_artists:
            my_artists.append(item['name'])

uris = []
for x in range(0,len(my_artists)):
    artist_name = my_artists[x]
    result = sp.search(q='artist:' + artist_name, type='artist')
    uri = result['artists']['items'][0]['uri']
    uris.append(uri)

data = []
for z in range(0,len(uris)):
    birdy_uri = uris[z]

    results = sp.artist_related_artists(birdy_uri)
    artist_data = results['artists']
    related_artists = []

    for i in range(0,len(artist_data)):
        related_artists.append(artist_data[i]['name'])

    data.append(related_artists)

f = open("spotify_data.csv", "w")
for item in data:
    try:
        if (len(item) > 0):
            for artist in item:
                print artist
                f.write(artist + ",")
        f.write("\n")
    except UnicodeEncodeError:
        continue

f.close()