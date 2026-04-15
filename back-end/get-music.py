import requests

def mood_to_query(mood):
    mapping = {
        "sunny": "happy pop",
        "rainy": "lofi chill",
        "cloudy": "indie mellow",
        "stormy": "dark ambient",
        "cold": "acoustic soft",
        "hot": "summer vibes",
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
            "link": item["link"],         # Deezer track page
            "album_cover": item["album"]["cover"]
        })

    return songs


if __name__ == "__main__":
    mood = "sunny"
    results = get_songs(mood)

    for song in results:
        print(f"{song['name']} - {song['artist']}")
        print(f"Link: {song['link']}")
        print("-" * 40)
