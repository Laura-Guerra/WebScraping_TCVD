
# Codi sense refactor final

"""
def add_quadrants(quadrant):
     parameter = f'&nelat={quadrant[0]}' + f'&nelong={quadrant[1]}' + f'&swlat={quadrant[2]}' + f'&swlong{quadrant[3]}'
     return parameter


def add_date(dates):
    parameter = '&checkin=' + dates[0] + '&checkout=' + dates[1]
    return parameter


def get_detailed_url(url):

    detailed_url_list = []
    page = requests.get(url)
    content = bs4(page.content)
    productDivs = content.find_all('a', attrs={'class' : CARD_CLASS})
    for a in productDivs:
        detailed_url_list.append(a['href'])

    return detailed_url_list


def build_urls(url, listings_per_page=18, pages_per_location=15):
    '''Builds links for all search pages for a given location'''
    
    url_list = []

    for i in range(pages_per_location):
        offset = listings_per_page * i
        url_pagination = url + f'&items_offset={offset}'

        for quadrant in QUADRANTS:
            url_def = url_pagination + add_quadrants(quadrant)
            
            for date in DATES:
                url_def = url_def + add_date(date)
                url_list.append(url_def)

       
    return url_list

"""
