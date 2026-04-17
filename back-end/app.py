from flask import Flask, jsonify, render_template
from get_weather import getUserLocation, getCurrentWeather
from get_music import get_songs

app = Flask(__name__)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("soundtemp.html")
@app.route("/recommend", methods=["GET"])
def recommend():
    try:
        # 1. Get user location
        location = getUserLocation()

        # 2. Get weather
        weather_data = getCurrentWeather(location["lat"], location["lon"])

        # 3. Extract mood (use weather_desc or weather)
        mood = weather_data["weather"].lower()

        # 4. Get songs
        songs = get_songs(mood)

        return jsonify({
            "weather": weather_data,
            "songs": songs
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)