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
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Type', 'Zone', 'URL'])

    for house_type in HOUSE_TYPES:
        type_filter_url = concatenate_url(PISOS_AD_BASE, house_type, URL_FILTER)  

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




def get_house_info(house_url):
    url = concatenate_url(PISOS_AD_BASE, house_url)  
    content = get_page_content(url)

    price = content.find('p', class_ = PRICE_CLASS)
    area = content.find('div', class_ = AREA_CLASS)
    bedrooms = content.find('div', class_ = BEDROOMS_CLASS)
    parking = content.find('p', class_ = PARKING_CLASS)
    features_lst = content.find_all('li', class_= FEATURES_CLASS)


    pass


house_url = "/venda/casa-adossada-3-habitacions-2-banys-arinsal/22747"

url = concatenate_url(PISOS_AD_BASE, house_url)  
content = get_page_content(url)
html_content = content.prettify()
#with open('example.html', 'w', encoding='utf-8') as file:
#    file.write(html_content)