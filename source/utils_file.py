import csv
import re

# Suponiendo que tienes un archivo 'file.csv' con una URL en cada fila como primer elemento
filename = 'data/details_urls.csv'
unique_numbers = set()

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        # Usamos regex para encontrar el número después de "/rooms/"
        match = re.search(r'/rooms/(\d+)', row[0])
        if match:
            unique_numbers.add(match.group(1))

print(list(unique_numbers)[:10])