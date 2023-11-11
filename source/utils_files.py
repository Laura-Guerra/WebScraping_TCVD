import csv
import pandas as pd
from constants import URLS_OUTPUT_FILE

def write_element_in_csv(id, house_type, zone, url, filename=URLS_OUTPUT_FILE):
    """
    Writes a new row with house details to a CSV file.

    Args:
    id (str): The unique identifier for the house.
    house_type (str): The type of the house (e.g., apartment, villa).
    zone (str): The geographical zone of the house.
    url (str): URL of the house listing.
    filename (str, optional): The name of the CSV file to write to. Defaults to OUTPUT_FILE.

    Notes:
    - Appends a new row to the CSV file.
    - Opens the file in append mode with UTF-8 encoding.
    """
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, house_type, zone, url])
        
        
def read_element_in_csv(filename=URLS_OUTPUT_FILE):
    """
    Reads and returns the contents of a CSV file as a pandas DataFrame.

    Args:
    filename (str, optional): The name of the CSV file to read from. Defaults to OUTPUT_FILE.

    Returns:
    pd.DataFrame: DataFrame containing the data read from the CSV file, or None if an error occurs.

    Notes:
    - Handles exceptions during file reading and prints an error message.
    """
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
  