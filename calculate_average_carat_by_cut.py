import csv

def calculate_average_carat_by_cut(filename):
    cut_carat_sum = {}
    cut_count = {}

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cut = row['cut']
            carat = float(row['carat'])

            if cut in cut_carat_sum:
                cut_carat_sum[cut] += carat
                cut_count[cut] += 1
            else:
                cut_carat_sum[cut] = carat
                cut_count[cut] = 1

    cut_average_carat = {cut: cut_carat_sum[cut] / cut_count[cut] for cut in cut_carat_sum}

    return cut_average_carat
