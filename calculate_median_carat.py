import csv

def calculate_median_carat(filename):
    carat_values = []

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['cut'].lower() == 'premium':
                carat_values.append(float(row['carat']))

    carat_values.sort()
    length = len(carat_values)
    if length % 2 == 0:
        median_index = length // 2
        median_carat = (carat_values[median_index - 1] + carat_values[median_index]) / 2
    else:
        median_index = length // 2
        median_carat = carat_values[median_index]

    return median_carat
