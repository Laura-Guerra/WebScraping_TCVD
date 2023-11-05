from bs4 import BeautifulSoup as bs4
import requests

from constants import QUADRANTS, DATES, AIRBNN_URL, CARD_CLASS

def build_parameter(key, value):
    """Constructs a URL parameter."""
    return f'&{key}={value}'


def add_quadrants_param(quadrant):
    """Generates the geographic parameters for a URL."""
    keys = ['nelat', 'nelong', 'swlat', 'swlong']
    return ''.join([build_parameter(key, value) for key, value in zip(keys, quadrant)])


def add_date_param(dates):
    """Generates the date parameters for a URL."""
    keys = ['checkin', 'checkout']
    return ''.join([build_parameter(key, value) for key, value in zip(keys, dates)])


def get_detail_urls_from_page(url):
    """Extracts listing URLs from a page"""
    content = requests.get(url)
    soup = bs4(content, 'html.parser')
    return [a['href'] for a in soup.find_all('a', class_=CARD_CLASS)]


def build_urls(url, listings_per_page=18, pages_per_location=15):
    """Builds a list of URLs for all search pages for a given location and date range."""
    url_list = []

    for offset in range(0, listings_per_page * pages_per_location, listings_per_page):
        for quadrant in QUADRANTS:
            for date in DATES:
                parameters = add_quadrants_param(quadrant) + add_date_param(date)
                final_url = f'{url}&items_offset={offset}{parameters}'
                url_list.append(final_url)

    return url_list

