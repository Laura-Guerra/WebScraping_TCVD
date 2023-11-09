import csv
import re

import requests
from bs4 import BeautifulSoup as bs4
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from constants import *
from utils_files import *
from utils_scraping import *
from utils_url import *

#get_house_urls()
df = read_element_in_csv(filename=OUTPUT_FILE)

result  =pd.DataFrame(generate_df(df))
result.to_csv(DEF_OUTPUT_FILE, index=False, encoding='utf-8-sig')

