from diamond_higherPrice import find_highest_price
import os
from average_price import calculate_average_price
from count_ideal_diamonds import count_ideal_diamonds
from diamond_color import count_diamond_colors
from calculate_median_carat import calculate_median_carat
from calculate_average_carat_by_cut import calculate_average_carat_by_cut
from color_avrg_price import calculate_average_price_by_color  

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    filename = 'diamonds.csv'
    
    while True:
        clear_screen()
        print("Menu:")
        print("1. Find the highest price")
        print("2. Calculate the average price")
        print("3. Count Ideal Diamonds")
        print("4. Count and List Diamond Colors")
        print("5. Calculate Median Carat of Premium Diamonds")
        print("6. Calculate Average Carat for Each Cut Type")
        print("7. Calculate Average Price for Each Color Type")  
        print("8. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        clear_screen()
        
        if choice == '1':
            highest_price, highest_price_diamond = find_highest_price(filename)
            if highest_price_diamond:
                print(f"The highest price for a diamond is ${highest_price}")
                print("Details of the diamond:")
                for key, value in highest_price_diamond.items():
                    print(f"{key}: {value}")
            else:
                print("No data found.")
        elif choice == '2':
            average_price = calculate_average_price(filename)
            print(f"The average price of all diamonds is ${average_price:.2f}")
        elif choice == '3':
            ideal_count = count_ideal_diamonds(filename)
            print(f"There are {ideal_count} Ideal diamonds in the dataset.")
        elif choice == '4':
            colors_count = count_diamond_colors(filename)
            print("Colors and their counts:")
            for color, count in colors_count.items():
                print(f"{color}: {count}")
        elif choice == '5':
            median_carat = calculate_median_carat(filename)
            print(f"The median carat of premium diamonds is {median_carat:.2f} carats.")
        elif choice == '6':
            average_carat_by_cut = calculate_average_carat_by_cut(filename)
            print("Average carat for each cut type:")
            for cut, avg_carat in average_carat_by_cut.items():
                print(f"{cut}: {avg_carat:.2f} carats")
        elif choice == '7':
            average_price_by_color = calculate_average_price_by_color(filename)
            print("Average price for each color type:")
            for color, avg_price in average_price_by_color.items():
                print(f"{color}: ${avg_price:.2f}")
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("Press Enter to continue...")


