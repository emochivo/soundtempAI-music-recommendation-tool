import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                            client_secret=SPOTIFY_CLIENT_SECRET))

def mood_to_query(mood):
    mapping = {
        "thunderstorm": "dark cinematic chill",
        "drizzle": "soft lo-fi chill",
        "rain": "lofi chill",
        "snow": "calm cozy acoustic",
        "mist": "soft ambient calm",
        "smoke": "dark ambient cinematic",
        "haze": "lofi mellow distant",
        "fog": "dreamy ambient chill",
        "dust": "desert ambient minimal",
        "sand": "desert ambient minimal",
        "ash": "dark cinematic tension",
        "squall": "intense electronic energy",
        "tornado": "chaotic cinematic orchestral",
        "clear": "happy upbeat pop",
        "clouds": "indie mellow relaxed",
        "default": "pop music"
    }

    return mapping.get(mood.lower(), mapping["default"])


def get_songs(mood, limit=50):

    query = mood_to_query(mood)

    songs = []
    offset = 0

    while len(songs) < limit:
        batch_limit = min(10, limit-len(songs))

        results = sp.search(
            q=query,
            type="track",
            limit=batch_limit,
            offset=offset
        )

        items = results["tracks"]["items"]

        if not items:
            break

        for item in items:
            songs.append({
                "name": item["name"],
                "artist": item["artists"][0]["name"],
                "album_cover": item["album"]["images"][0]["url"] if item["album"]["images"] else None,
                "link": item["external_urls"]["spotify"],
                "embed_url": item["external_urls"]["spotify"].replace(
                    "https://open.spotify.com/track/",
                    "https://open.spotify.com/embed/track/"
                )
            })

        offset += batch_limit

    return songs


if __name__ == "__main__":
    mood = "atmosphere"
    results = get_songs(mood)

    for song in results:
        print(f"{song['name']} - {song['artist']}")
        print(f"Link: {song['link']}")
        print("-" * 40)