from bs4 import BeautifulSoup as bs4
import requests


# (nelat, nelong, swlat, swlong )
quadrants = [(41.44499 ,  2.16561, 41.41053333333327, 2.12304),
             (41.44499, 2.20819, 41.41053333333327, 2.165615),
             (41.41053333333327, 2.165615, 41.38867666666667 , 2.12304),
             (41.41053333333327,  2.20819, 41,38867666666667, 2,165615),
             (41.38867666666667, 2.165615, 41.36052, 2.12304),
             (41.38867666666667, 2.12304, 41.36052, 2.165615)]


def build_urls(url, listings_per_page=20, pages_per_location=15):
    """Builds links for all search pages for a given location"""
    
    url_list = []
    for i in range(pages_per_location):
        offset = listings_per_page * i
        url_pagination = url + f'&items_offset={offset}'
        url_list.append(url_pagination)
       
    return url_list