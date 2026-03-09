import json
import logging
from pathlib import Path
import yt_dlp

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data" / "videos.json"
DOWNLOAD_DIR = BASE_DIR / "downloads"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)
DOWNLOAD_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def load_urls():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return data.get("videos", [])
    except Exception:
        logger.exception("Failed to load videos.json")
        return []


def download_video(url: str):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",  # select best video + best audio
            "outtmpl": str(DOWNLOAD_DIR / "%(title)s/%(title)s.%(ext)s"),
            "noplaylist": True,
            "merge_output_format": "mp4",  # merge into mp4 if video+audio separate
            "quiet": False,  # set True to silence yt-dlp output
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Downloading: {url}")
            ydl.download([url])

    except Exception:
        logger.exception(f"Failed to download video: {url}")


def main():
    urls = load_urls()

    if not urls:
        logger.warning("No URLs found in videos.json")
        return

    for url in urls:
        download_video(url)

    logger.info("All downloads completed.")


if __name__ == "__main__":
    main()
