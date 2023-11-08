from bs4 import BeautifulSoup as bs4
from datetime import datetime
import time
import csv
import requests

from constants import QUADRANTS, DATES, AIRBNB_URL, CARD_CLASS, DETAIL_URLS_FILE

def build_parameter(key, value):
    """Constructs a URL parameter."""
    return f'&{key}={value}'


def build_quadrants_param(quadrant):
    """Generates the geographic parameters for a URL."""
    keys = ['ne_lat', 'ne_lng', 'sw_lat', 'sw_lng']
    return ''.join([build_parameter(key, value) for key, value in zip(keys, quadrant)])


def build_date_param(dates):
    """Generates the date parameters for a URL."""
    keys = ['checkin', 'checkout']
    return ''.join([build_parameter(key, value) for key, value in zip(keys, dates)])


def get_detail_urls_from_page(url):
    """Extracts listing URLs from a page"""
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception(f"Error fetching page: {url}, status code: {page.status_code}")
    content = bs4(page.content, 'html.parser')
    productDivs = content.find_all('a', attrs={'class' : CARD_CLASS})
    return [a['href'] for a in productDivs if 'href' in a.attrs]


def build_urls(listings_per_page=18, pages_per_location=15):
    """Generate search URLs with quadrant indices."""
    urls = []
    for offset in range(0, listings_per_page * pages_per_location, listings_per_page):
        for quadrant_index, quadrant in enumerate(QUADRANTS):
            for date in DATES:
                print(f'Offset {offset}, Quadrant: {quadrant_index + 1}, Date: {date} \n')
                geo_params = build_quadrants_param(quadrant)
                date_params = build_date_param(date)
                search_url = f'{AIRBNB_URL}&items_offset={offset}{geo_params}{date_params}'
                urls.append((search_url, quadrant_index))
    return urls


def initialize_csv(filepath=DETAIL_URLS_FILE):
    """Initialize the CSV file with headers if it doesn't exist."""
    try:
        with open(filepath, 'x', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['detail_url', 'quadrant_index', 'timestamp'])
            writer.writeheader()
    except FileExistsError:
        pass


def scrape_detail_urls(urls_with_quadrants, filepath=DETAIL_URLS_FILE):
    total_urls = len(urls_with_quadrants)
    scraped_count = 0

    for url, quadrant_index in urls_with_quadrants:
        try:
            detail_urls = get_detail_urls_from_page(url)
            with open(filepath, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['detail_url', 'quadrant_index', 'timestamp'])
                for detail_url in detail_urls:
                    data = {
                        'detail_url': detail_url,
                        'quadrant_index': quadrant_index,
                        'timestamp': datetime.now().isoformat()
                    }
                    writer.writerow(data)
            scraped_count += 1
            print(f"Scraped {scraped_count} of {total_urls} pages")
        except Exception as e:
            print(f"Failed to scrape {url}. Error: {e}")

        time.sleep(1)

    print("Scraping completed.")


urls_with_quadrants  = build_urls()
scrape_detail_urls(urls_with_quadrants)

