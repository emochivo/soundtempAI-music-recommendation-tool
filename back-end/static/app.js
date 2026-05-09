let currentSong = null;

async function loadData() {
  try {
    const response = await fetch("/recommend");
    const data = await response.json();

    // Weather
    document.getElementById("weather").innerHTML = `
      <p>${data.weather.city}, ${data.weather.country}</p>
      <p>${data.weather.weather}</p>
      <p>${data.weather.temperature}°F</p>
    `;

    // First song (recommended)
    const firstSong = data.songs[0];
    currentSong = firstSong;

    document.getElementById("playlist").innerHTML = `
      <p>${firstSong.name} - ${firstSong.artist}</p>
    `;

    updatePlayer(firstSong);

    // More songs
    const container = document.getElementById("more-playlists");
    container.innerHTML = "";

    data.songs.forEach(song => {
      const div = document.createElement("div");
      div.className = "playlist-item";

      div.innerHTML = `
        <img src="${song.album_cover}">
        <p>${song.name}</p>
        <small>${song.artist}</small>
      `;

      div.onclick = () => selectSong(song);

      container.appendChild(div);
    });

  } catch (err) {
    console.error(err);
  }
}

function selectSong(song) {
  currentSong = song;
  updatePlayer(song);
}

function updatePlayer(song) {
  document.getElementById("album-art").style.backgroundImage = `url(${song.album_cover})`;
  document.getElementById("song-title").innerText = song.name;
  document.getElementById("song-artist").innerText = song.artist;

  document.getElementById("spotify-player").src = song.embed_url;
  document.getElementById("spotify-link").href = song.link;
}

function scrollSongs(direction) {
  const container = document.getElementById("more-playlists");
  container.scrollBy({
    left: direction * 350,
    behavior: "smooth"
  });
}

// run on page load
window.onload = loadData;