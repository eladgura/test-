import csv

def count_ideal_diamonds(filename):
    ideal_count = 0

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['cut'].lower() == 'ideal':
                ideal_count += 1

    return ideal_count
