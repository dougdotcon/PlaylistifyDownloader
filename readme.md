# PlaylistifyDownloader

Baixe playlists do Spotify em formato MP3 usando o seguinte script do Python.

## Requisito

- Python 3.8+
- ffmpeg-master-latest-win64-gpl-shared

## Instalação

Instale as dependências necessárias:

```bash
pip install Flask spotipy youtubesearchpython yt-dlp

## Configurar as credenciais do Spotify
Este script requer credenciais do Spotify. Para obtê-las, siga esses passos:
Acesse https://developer.spotify

# Playlist Downloader

Baixe playlists do Spotify em formato MP3 usando o seguinte script do Python.

## Requisitos

- Python 3.8+
- ffmpeg-master-latest-win64-gpl-shared

## Instalação

Instale as dependências necessárias:

```bash
pip install Flask spotipy youtubesearchpython yt-dlp

## Configurar as credenciais do Spotify
Este script requer credenciais do Spotify. Para obtê-las, siga esses passos:

Acesse https://developer.spotify.com/dashboard/login e faça login com sua conta do Spotify.
Crie um novo aplicativo e copie o "Client ID" e o "Client Secret".
Coloque suas credenciais na variável no arquivo de configuração.
python
Copiar código

# config.py
SPOTIPY_CLIENT_ID = 'seu_client_id'
SPOTIPY_CLIENT_SECRET = 'seu_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080/callback'

## Utilização
Executar app.py.
Acesse http://localhost:8080 em seu navegador.
Cole a URL da playlist do Spotify e pressione o botão "Enviar".
As músicas serão baixadas como arquivos MP3 na pasta onde o script está localizado.
Atenção
O uso deste script pode violar os termos de serviço do Spotify e do YouTube. Utilize por sua própria conta e risco.


Caso precise de mais informações ou instruções, confira abaixo:

## Troubleshooting
Caso encontre problemas no script, siga estas etapas:

Verifique se você instalou todas as dependências corretamente.
Verifique se seu arquivo de configuração contém as credenciais do Spotify corretas e válidas.
Certifique-se de criar a aplicação corretamente no painel do desenvolvedor do Spotify.
Verifique se ffmpeg-master-latest-win64-gpl-shared foi devidamente instalado.
Contribuindo
Caso deseje contribuir para o projeto, sinta-se à vontade para realizar um fork ou enviar uma Pull Request com suas melhorias e correções.

License
Este projeto está disponível sob a licença MIT License.
