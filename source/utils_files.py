import csv
from constants import OUTPUT_FILE

def write_element_in_csv(id, house_type, zone, url, filename=OUTPUT_FILE):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, house_type, zone, url])