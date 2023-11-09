import csv
import pandas as pd
from constants import OUTPUT_FILE

#CANVIAR PATH!!
def write_element_in_csv(id, house_type, zone, url, filename=OUTPUT_FILE):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, house_type, zone, url])
        
def read_element_in_csv(filename=OUTPUT_FILE):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
  