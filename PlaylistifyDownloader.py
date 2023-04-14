import os
import spotipy
from youtubesearchpython import VideosSearch
import yt_dlp as youtube_dl
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, redirect, render_template_string
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

if not os.path.exists("musicas"):
    os.makedirs("musicas")

app = Flask(__name__)

# Use as credenciais do arquivo de configuração.
os.environ["SPOTIPY_CLIENT_ID"] = "86127ed04e244c3290f86a03622bf340"
os.environ["SPOTIPY_CLIENT_SECRET"] = "2692928c53ab4d6389a10fd80759c8df"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
music_titles = []

# ... (funções download_song_with_youtube_dl e download_songs permanecem inalteradas)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        global playlist_id
        playlist_url = request.form['playlist_url']
        playlist_id = playlist_url.split('/')[-1]
        auth_url = sp.auth_manager.get_authorize_url()
        return redirect(auth_url)

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Downloader de Playlist</title>
    </head>
    <body>
        <h1>Downloader de Playlist do Spotify</h1>
        <form method="post">
            <label for="playlist_url">URL da Playlist:</label>
            <input type="text" id="playlist_url" name="playlist_url" required>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    ''')
def search_youtube(query):
    videos_search = VideosSearch(query, limit=1)
    results = videos_search.result()
    if results['result']:
        return results['result'][0]['link']
    return None
# ... (a rota /callback permanece inalterada)
def download_song_with_youtube_dl(title, output_path=""):
    try:
        print(f'Baixando: {title}')
        video_url = search_youtube(title + " YouTube")

        if video_url is None:
            print(f"Não foi possível encontrar o vídeo para {title}")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f"musicas/{title}.%(ext)s",
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}
            ],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        print(f"Erro ao baixar {title}: {e}")

def download_songs(music_titles):
    for title in music_titles:
        download_song_with_youtube_dl(title)

@app.route('/')
def index():
    auth_url = sp.auth_manager.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    sp.auth_manager.get_access_token(request.args.get('code'))
    results = sp.playlist_tracks(playlist_id)

    for idx, item in enumerate(results['items']):
        track = item['track']
        music_titles.append(f"{track['artists'][0]['name']} - {track['name']}")

    download_songs(music_titles)

    return "Músicas baixadas com sucesso! Confira a pasta onde o script está localizado para os arquivos MP3."


if __name__ == '__main__':
    app.run(port=8080)
