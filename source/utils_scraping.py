import csv
import re

import requests
from bs4 import BeautifulSoup as bs4
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from constants import *
from utils_files import write_element_in_csv
from utils_url import concatenate_url


def get_page_content(url):
    """
    Fetches the content of a webpage at the specified URL.

    Args:
    url (str): The URL of the webpage to fetch.

    Returns:
    BeautifulSoup object: Parsed HTML content of the page.

    Raises:
    Exception: If the request to the URL fails or returns a non-200 status code.
    """
    headers = {
        'User-Agent': BS4_USER_AGENT
    }
    page = requests.get(url, headers=headers)
    if page.status_code != 200:
        raise Exception(f"Error fetching page: {url}, status code: {page.status_code}")
    
    content = bs4(page.content, 'html.parser')
    return content


def print_selenium_user_agent():
    """
    Prints the User-Agent string used by the Selenium WebDriver session.

    Notes:
    - Ensure the Chrome WebDriver is correctly set up in your environment.
    - The WebDriver is closed after retrieving the User-Agent.
    """
    driver = webdriver.Chrome()

    try:
        driver.get("http://httpbin.org/user-agent")

        user_agent_element = driver.find_element(By.TAG_NAME, "body")
        user_agent_text = user_agent_element.text

        print("Selenium User-Agent:", user_agent_text)
    finally:
        driver.quit()


def get_zone_urls():
    """
    Retrieves URLs from a predefined webpage using Selenium.

    Returns:
    list: A list of URLs found on the page.

    Notes:
    - Utilizes Chrome WebDriver for scraping.
    - Waits for elements to load before extracting URLs.
    - Handles timeouts with a message and closes the driver.
    """
    driver = webdriver.Chrome()
    driver.get(PISOS_AD_BASE)

    urls = []

    try:
        elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.btn.mapa__btn[href]")))
        urls = [element.get_attribute("href") for element in elements]

    except TimeoutException:
        print("Timeout occurred while waiting for elements to be visible")
    finally:
        driver.quit()
    
    return urls


def get_house_id(url):
    """
    Extracts the house ID from a given URL.

    Args:
    url (str): The URL containing the house ID.

    Returns:
    str: The extracted house ID.
    """
    return url.split("/")[-1]


def get_house_urls(zone_urls):
    """
    Processes a list of zone URLs to fetch house URLs and writes them to a CSV file.

    Args:
    zone_urls (list): List of URLs representing different zones.

    Notes:
    - Iterates over predefined properties types and zone URLs.
    - Extracts house URLs from each page and writes to a CSV file.
    """
    with open(URLS_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Type', 'Zone', 'URL'])
 
    for url in zone_urls:
        page_num = 1
        while True:  # Aquest bucle s'executa fins que no troba mes ancors
            zone = url.split("/")[-1]
            house_type = url.split('/')[3]
            
            print(f'zone: {zone}, type: {house_type}, page num: {page_num}')
            zone_page_url = f'{url}?page={page_num}'

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
    """
    Extracts house information from a given URL.

    Args:
    house_url (str): The URL of the house listing.

    Returns:
    tuple: Contains price, area, bedrooms, parking, list of features, and agency info.
    """
    url = concatenate_url(PISOS_AD_BASE, house_url)  
    content = get_page_content(url)

    price = content.find('p', class_ = PRICE_CLASS).text.strip()
    area = content.find('div', class_ = AREA_CLASS).text.strip()
    bedrooms = content.find('div', class_ = BEDROOMS_CLASS).text.strip()
    parking = content.find('div', class_ = PARKING_CLASS).text.strip()
    features_lst = content.find_all('li', class_= FEATURES_CLASS)
    try:
      immo = content.find('ul', class_ = IMMO_CLASS).find('strong').text.strip()
    except:
      immo = ''

    return  price, area, bedrooms, parking, features_lst, immo


def iterator(row):
    """
    Processes a single row of a DataFrame to extract house information.

    Args:
    row (pd.Series): A row from a DataFrame containing house listing details.

    Returns:
    dict: A dictionary containing extracted house information and additional details.
    """
    house_info_df = get_house_info(row['URL'])
    price, area, bedrooms, parking, features_lst, immo = get_house_info(row['URL'])
    result_dict = {
                    'Price': price,
                    'Area': area,
                    'Bedrooms': bedrooms,
                    'Parking': parking,
                    'Features': ', '.join(feature.text.strip() for feature in features_lst),
                    'Agency': immo,
                    'Id': row['ID'],
                    'Type': row['Type'],
                    'Zone': row['Zone'],
                    'URL': row['URL'],
                    'Timestamp': datetime.now()
                    }
    print(price)
    return result_dict
      
  
def generate_df(df):
    """
    Generates a list of dictionaries containing house information from a DataFrame.

    Args:
    df (pd.DataFrame): DataFrame containing URLs and details of house listings.

    Returns:
    list: A list of dictionaries, each containing information about a house listing.

    Notes:
    - Uses a ThreadPoolExecutor for concurrent processing.
    - Handles exceptions during data retrieval.
    """
    result_data = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(iterator, row) for _, row in df.iterrows()]
        for future in futures:
          try:
            result_data.append(future.result())
          except Exception as e:
            print(f"An exception occurred: {e}")

    return result_data


