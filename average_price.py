import csv

def calculate_average_price(filename):
    total_price = 0
    count = 0

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_price += float(row['price'])
            count += 1

    average_price = total_price / count if count > 0 else 0
    return average_price
