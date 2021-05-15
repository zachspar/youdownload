# YouDownload

Download audio and video from YouTube. I made this because I was fed up with all the advertisements when attepting to download  songs from YouTube. This package creates a local web application that allows you to paste a Youtube url into the UI to extract the audio from a Youtube video. Once an MP3 file is generated, you will be able to download it directly to your local machine. It uses `youtube-dl` as a backend.

## Live website :)
Check out the website (give it a minute to load LOL it runs on a free server!!) :: [YouDownload.com](https://youdownload-zs.herokuapp.com)
Just go find a song you like on YouTube, copy the link, paste the link [here](https://youdownload-zs.herokuapp.com), and download the exact same quality music you get from the video :)

## Setup and Installation
1. Make sure that `pwd` is your project root = `youdownload`
2. Create a virtual environment with the package installed as well as all the dependencies needed for the project
   - `python3 -m venv env`
   - `source env/bin/activate`
   - `pip install --upgrade pip`
   - `pip install -r requirements.txt`
3. Change execution mode of `server.sh` script
    - run `chmod +x server.sh`
    - run `./server.sh`
    - navigate to `localhost:5000` on your web browser
4. Copy and paste a Youtube url into the UI
5. View your downloaded music within the project directory `$CWD/www/yd/songs/mp3`
