import csv
import re

import requests
from bs4 import BeautifulSoup as bs4

from constants import *
from utils_files import write_element_in_csv
from utils_url import concatenate_url


def get_page_content(url):
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception(f"Error fetching page: {url}, status code: {page.status_code}")
    
    content = bs4(page.content, 'html.parser')
    return content


def get_zone_urls():
    content = get_page_content(PISOS_AD_BASE)
    pass

def get_house_id(url):
    return url.split("/")[-1]

def get_house_urls():
    base_url = PISOS_AD_BASE
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Type', 'Zone', 'URL'])

    for house_type in HOUSE_TYPES:
        type_filter_url = concatenate_url(base_url, house_type, URL_FILTER)  

        for zone in ANDORRA_ZONES:
            page_num = 1
            while True:  # Aquest bucle s'executa fins que no troba mes ancors

                print(f'zone: {zone}, type: {house_type}, page num: {page_num}')
                zone_page_url = concatenate_url(type_filter_url, zone)+f'?page={page_num}'

                content = get_page_content(zone_page_url)
                ancors = content.find_all('a', attrs={'class': HOUSE_HREF_CLASS})
                
                if not ancors:
                    break
                
                house_urls = [ancor['href'] for ancor in ancors if 'href' in ancor.attrs]
                
                for house_url in house_urls:
                    house_id = get_house_id(house_url)
                    write_element_in_csv(house_id, house_type, zone, house_url)

                page_num += 1


def get_house_info():
    pass


get_house_urls()