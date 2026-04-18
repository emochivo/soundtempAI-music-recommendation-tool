# SoundTempAI: Smart Music Recommendation System with Weather-Based Personalization

## Tech Stack
- Frontend: HTML + CSS
- Backend: Python
- Weather data: OpenWeather API (if we want the app to cover weather globally)
- Music data: Deezer API or Spotify API
- Database: still in consideration (e.g., Firebase, MongoDB, or SQLite)

## How to run from the Technical Aspect
1. Set up virtual environment (include in .gitignore)
2. Install requirements.txt file
3. Set up environment file (.env) - include API key

## How to run (User)
1. Clone the repository
2. Install dependencies from requirements.txt
3. Set up environment variables (e.g., API keys): make sure to create a .env file and add your own API key for OpenWeather
4. Run the backend server (e.g., `python app.py`), and access the frontend through the provided URL (e.g., `http://localhost:5000`)
5. The sample app will allow users to see their current weather and receive music recommendations based on that weather.
