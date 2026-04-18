import requests

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


def get_songs(mood, limit=10):
    query = mood_to_query(mood)

    url = "https://api.deezer.com/search"

    params = {
        "q": query,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    songs = []

    for item in data.get("data", []):
        songs.append({
            "name": item["title"],
            "artist": item["artist"]["name"],
            "preview": item["preview"],
            "album_cover": item["album"]["cover"]
        })

    return songs


if __name__ == "__main__":
    mood = "atmosphere"
    results = get_songs(mood)

    for song in results:
        print(f"{song['name']} - {song['artist']}")
        print(f"Link: {song['link']}")
        print("-" * 40)
