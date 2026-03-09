# Video Downloader (yt-dlp + uv + Conda)

Download multiple videos from a JSON file.

Each video is stored in a folder named after the video title.

Example:

downloads/
 ├── Video Title/
 │    └── Video Title.mp4

------------------------------------

SETUP

Create environment

conda create -n video-downloader python=3.12 -y
conda activate video-downloader

Install uv

pip install uv

Install project dependencies

uv pip install -e .

------------------------------------

RUN

python src/downloader/main.py

OR

download-videos

------------------------------------

ADD VIDEOS

Edit:

data/videos.json

Example:

{
  "videos": [
    "https://youtube.com/watch?v=VIDEO_ID"
  ]
}

------------------------------------

LOGS

All logs are stored in:

logs/app.log
