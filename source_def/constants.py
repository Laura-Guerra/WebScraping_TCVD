# constants.py

PISOS_AD_BASE = "https://pisos.ad"
URL_FILTER = "tots-els-tipus/tots-subtipus"

HOUSE_TYPES = ("venda", "lloguer")
ANDORRA_ZONES = [
    "ordino",
    "canillo",
    "encamp",
    "andorra-la-vella",
    "sant-julia-de-loria",
    "escaldes-engordany",
    "la-massana"
]

HOUSE_HREF_CLASS = "list-item__link-1"
PRICE_CLASS = "fitxa__preu"
AREA_CLASS = "col-6 col-md fitxa__icos-superficie mb-3 mb-lg-0"
BEDROOMS_CLASS = "col-6 col-md fitxa__icos-habitacions text-lowercase mb-3 mb-lg-0"
BATHROOM_CLASS = "col-6 col-md fitxa__icos-banys text-lowercase mb-3 mb-lg-0"
PARKING_CLASS = "col-6 col-md fitxa__icos-parking mb-3 mb-lg-0"
FEATURES_CLASS = "col-xl-4 col-sm-6 col-12"
IMMO_CLASS = "list-unstyled fitxa__immo"


OUTPUT_FILE = "dataset/houses.csv"
DEF_OUTPUT_FILE = "dataset/houses_dataset.csv"