import csv

def count_diamond_colors(filename):
    colors_count = {}

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            color = row['color']
            if color in colors_count:
                colors_count[color] += 1
            else:
                colors_count[color] = 1

    return colors_count
