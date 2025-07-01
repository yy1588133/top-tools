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

# Directory to save comics, relative to the script's location
import os

COMICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "comics")


def ensure_comics_dir():
    """Ensure the directory for saving comics exists."""
    if not os.path.exists(COMICS_DIR):
        os.makedirs(COMICS_DIR)
        logger.info(f"Created directory {COMICS_DIR} for saving comics.")


def fetch_latest_xkcd_comic():
    """Fetch and save the latest XKCD comic and its explanation from explainxkcd.com."""
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

        # Extract comic number from the page title or meta information
        comic_number = ""
        title_tag = soup.find("div", id="ctitle")
        if title_tag:
            title_text = title_tag.text
            # Check if title contains the comic number
            import re

            match = re.search(r"#(\d+)", title_text)
            if match:
                comic_number = match.group(1)
        if not comic_number:
            # Fallback to URL path or other indicators
            prev_link = soup.find("a", rel="prev")
            if prev_link and "href" in prev_link.attrs:
                prev_href = prev_link["href"]
                match = re.search(r"/(\d+)/", prev_href)
                if match:
                    prev_number = int(match.group(1))
                    comic_number = str(prev_number + 1)
        if not comic_number.isdigit():
            logger.error("Could not extract comic number from page.")
            return

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

        # Fetch explanation from explainxkcd.com
        explanation_url = f"https://www.explainxkcd.com/wiki/index.php/{comic_number}"
        logger.info(f"Fetching explanation from {explanation_url}")
        explanation_response = requests.get(
            explanation_url, headers=headers, timeout=10
        )
        explanation_response.raise_for_status()

        explanation_soup = BeautifulSoup(explanation_response.text, "html.parser")
        explanation_section = explanation_soup.find("span", id="Explanation")
        if not explanation_section:
            logger.error("Could not find Explanation section on the page.")
            return

        # Extract text from the Explanation section
        explanation_text = ""
        current_element = explanation_section.find_parent()
        while current_element and current_element.name != "span":
            if current_element.name in ["p", "div"]:
                explanation_text += current_element.get_text(strip=True) + "\n\n"
            current_element = current_element.find_next_sibling()
            if current_element and current_element.find("span", id="Transcript"):
                break

        # Save the explanation text
        explanation_filename = "latest_xkcd_explanation.txt"
        explanation_filepath = os.path.join(COMICS_DIR, explanation_filename)
        with open(explanation_filepath, "w", encoding="utf-8") as f:
            f.write(explanation_text)

        logger.info(f"Successfully saved explanation to {explanation_filepath}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching comic or explanation: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


def main():
    """Main function to initialize and run the scraper."""
    logger.info("Starting XKCD Scraper...")
    ensure_comics_dir()

    # Run the scraper immediately and exit
    fetch_latest_xkcd_comic()
    logger.info(
        "Finished fetching the latest XKCD comic and explanation. Exiting script."
    )


if __name__ == "__main__":
    main()
