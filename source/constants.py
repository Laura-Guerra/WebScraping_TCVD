# constants.py

# (nelat, nelong, swlat, swlong )
QUADRANTS = [
    ("41.44499", "2.16561", "41.41053333333327", "2.12304"),
    ("41.44499", "2.20819", "41.41053333333327", "2.165615"),
    ("41.41053333333327", "2.165615", "41.38867666666667", "2.12304"),
    ("41.41053333333327", "2.20819", "41.38867666666667", "2.165615"),
    ("41.38867666666667", "2.165615", "41.36052", "2.12304"),
    ("41.38867666666667", "2.12304", "41.36052", "2.165615")
    ]


# (check-in, check-out) yyyy-mm-dd
DATES =[
    ('2023-11-13', '2023-11-15'),
    ('2023-11-17', '2023-11-19'),
    ('2023-12-08', '2023-12-10')
    ]


AIRBNN_URL = "https://www.airbnb.es/s/Barcelona--Spain/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-12-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=7&channel=EXPLORE&date_picker_type=calendar&adults=2&source=structured_search_input_header&search_type=user_map_move&query=Barcelona%2C%20Spain&zoom_level=14.35412066680454&place_id=ChIJ5TCOcRaYpBIRCmZHTz37sEQ&zoom=14.35412066680454&search_by_map=true"


CARD_CLASS = "l1ovpqvx bn2bl2p dir dir-ltr"

DETAIL_URLS_FILE = "data/details_urls.csv"