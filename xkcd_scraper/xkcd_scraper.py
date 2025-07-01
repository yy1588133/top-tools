import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import schedule
import time
import logging

# Set up logging to track script execution and errors
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Directory to save comics
COMICS_DIR = "comics"


def ensure_comics_dir():
    """Ensure the directory for saving comics exists."""
    if not os.path.exists(COMICS_DIR):
        os.makedirs(COMICS_DIR)
        logger.info(f"Created directory {COMICS_DIR} for saving comics.")


def fetch_latest_xkcd_comic():
    """Fetch and save the latest XKCD comic."""
    try:
        # URL of the XKCD homepage
        url = "https://xkcd.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Make HTTP GET request to fetch the page content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        logger.info("Successfully fetched XKCD homepage.")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the comic image element
        comic_div = soup.find("div", id="comic")
        if not comic_div:
            logger.error("Could not find comic div on the page.")
            return

        comic_img = comic_div.find("img")
        if not comic_img:
            logger.error("Could not find comic image in the comic div.")
            return

        # Extract the image URL
        img_url = comic_img["src"]
        if not img_url.startswith("http"):
            img_url = "https:" + img_url

        # Use a static filename for the latest comic
        filename = "latest_xkcd.jpg"
        filepath = os.path.join(COMICS_DIR, filename)

        # Download the comic image
        logger.info(f"Downloading comic from {img_url}")
        img_response = requests.get(img_url, timeout=10)
        img_response.raise_for_status()

        # Save the image
        with open(filepath, "wb") as f:
            f.write(img_response.content)

        logger.info(f"Successfully saved comic to {filepath}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching comic: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


def main():
    """Main function to initialize and run the scraper."""
    logger.info("Starting XKCD Scraper...")
    ensure_comics_dir()

    # Run the scraper immediately and exit
    fetch_latest_xkcd_comic()
    logger.info("Finished fetching the latest XKCD comic. Exiting script.")


if __name__ == "__main__":
    main()
