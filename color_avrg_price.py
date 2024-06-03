import csv

def calculate_average_price_by_color(filename):
    color_price_sum = {}
    color_count = {}

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            color = row['color']
            price = float(row['price'])

            if color in color_price_sum:
                color_price_sum[color] += price
                color_count[color] += 1
            else:
                color_price_sum[color] = price
                color_count[color] = 1

    color_average_price = {color: color_price_sum[color] / color_count[color] for color in color_price_sum}

    return color_average_price
