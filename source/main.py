import pandas as pd

from constants import OUTPUT_FILE, URLS_OUTPUT_FILE, BS4_USER_AGENT
from utils_files import read_element_in_csv
from utils_scraping import generate_df, get_house_urls, get_zone_urls, print_selenium_user_agent


def main():
    """
    Main function to orchestrate web scraping, data processing, and saving results.

    Steps performed by this function:
    1. Prints the User-Agent used by Selenium and BeautifulSoup (BS4).
    2. Retrieves zone URLs for scraping.
    3. Obtains house URLs from these zones and writes them to a CSV file.
    4. Reads the CSV file into a DataFrame.
    5. Generates a DataFrame with detailed house information.
    6. Saves the final DataFrame to a CSV file.

    The function first prints the User-Agent strings to help identify the scraping
    environment. Then, it proceeds with the scraping and data processing tasks,
    culminating in saving the scraped data to a CSV file.

    Raises:
    ValueError: If zone URLs are not found or if the CSV file cannot be read.
    """
    try:
        print_selenium_user_agent()
        print(f'BS4 User-Agent: {BS4_USER_AGENT}')

        zone_urls = get_zone_urls()
        if not zone_urls:
            raise ValueError("No zone URLs were found.")

        get_house_urls(zone_urls)

        df = read_element_in_csv(filename=URLS_OUTPUT_FILE)
        if df is None:
            raise ValueError("Error reading the CSV file.")

        # Generate a DataFrame with house information
        result = pd.DataFrame(generate_df(df))

        # Save the final DataFrame to CSV
        result.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')

    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()


