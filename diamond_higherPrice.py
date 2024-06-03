import csv

def find_highest_price(filename):
    highest_price = 0
    highest_price_diamond = None

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            price = float(row['price'])
            if price > highest_price:
                highest_price = price
                highest_price_diamond = row

    return highest_price, highest_price_diamond
