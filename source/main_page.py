from bs4 import BeautifulSoup as bs4
import requests


# (nelat, nelong, swlat, swlong )
quadrants = [(41.44499 ,  2.16561, 41.41053333333327, 2.12304),
             (41.44499, 2.20819, 41.41053333333327, 2.165615),
             (41.41053333333327, 2.165615, 41.38867666666667 , 2.12304),
             (41.41053333333327,  2.20819, 41,38867666666667, 2,165615),
             (41.38867666666667, 2.165615, 41.36052, 2.12304),
             (41.38867666666667, 2.12304, 41.36052, 2.165615)]

dates = [('2023-11-13', '2023-11-15'),
         ('2023-11-17', '2023-11-19'),
         ('2023-12-08', '2023-12-10')]




def build_urls(url, listings_per_page=18, pages_per_location=15):
    """Builds links for all search pages for a given location"""
    
    url_list = []

    for i in range(pages_per_location):
        offset = listings_per_page * i
        url_pagination = url + f'&items_offset={offset}'

        for quadrant in quadrants:
            url_def = url_pagination + add_quadrants(quadrant)
            
            for date in dates:
                url_def = url_def + add_date(date)
        
        url_list.append(url_pagination)

       
    return url_list


def add_quadrants(quadrant):
     
     parameter = '&nelat=' + quadrant[0] + '&nelong=' + quadrant[1] + '&swlat=' + quadrant[2] + 'swlong' + quadrant[3]
     return parameter


def add_date(dates):
    parameter = '&checkin=' + dates[0] + '&checkout=' + dates[1]
    return parameter



def get_detailed_url(url):

    detailed_url_list = []
    page = requests.get(url)
    content = bs4(page.content)
    productDivs = content.find_all('a', attrs={'class' : 'l1ovpqvx bn2bl2p dir dir-ltr'})
    for a in productDivs:
        detailed_url_list.append(a['href'])

    return detailed_url_list

