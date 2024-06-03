

---

# Diamond Analysis Tool

The Diamond Analysis Tool is a Python script designed to analyze data from a CSV file containing information about diamonds. It offers various functionalities to analyze and extract insights from the diamond dataset.

## Features

1. **Find the Highest Price Diamond**
   - This option finds and displays the highest-priced diamond in the dataset along with its details, including carat, cut, color, clarity, depth, table, price, and dimensions.

2. **Calculate the Average Price of All Diamonds**
   - This option calculates and displays the average price of all diamonds in the dataset.

3. **Count Ideal Diamonds**
   - Ideal diamonds are the highest quality diamonds based on cut. This option counts and displays the number of Ideal diamonds in the dataset.

4. **Count and List Diamond Colors**
   - This option counts and lists the colors of diamonds along with their counts. It provides a breakdown of how many diamonds are available in each color category.

5. **Calculate Median Carat of Premium Diamonds**
   - Premium diamonds are those with high-quality cut grades. This option calculates and displays the median carat of premium diamonds in the dataset.

6. **Calculate Average Carat for Each Cut Type**
   - This option calculates and displays the average carat for each cut type (e.g., Ideal, Premium, Good, Very Good, Fair). It provides insights into the average size of diamonds based on their cut quality.

7. **Calculate Average Price for Each Color Type**
   - This option calculates and displays the average price for each color type (e.g., D, E, F, G, H, I, J). It helps understand the average pricing trends based on the color grading of diamonds.

## Requirements

- Python 3.x
- Required Python modules:
  - `csv`: For handling CSV file operations.
  - `os`: For clearing the terminal screen based on the operating system.

## Installation

1. Clone or download the repository to your local machine.

   

2. Navigate to the project directory.

   ```bash
   cd diamond-analysis-tool
   ```

3. Install the required Python dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Pages Information

### `diamond_higherPrice.py`

This page contains the `find_highest_price` function, which is used to find the highest-priced diamond in the dataset.

### `average_price.py`

This page contains the `calculate_average_price` function, which calculates and displays the average price of all diamonds in the dataset.

### `count_ideal_diamonds.py`

This page contains the `count_ideal_diamonds` function, which counts and displays the number of Ideal diamonds in the dataset.

### `diamond_color.py`

This page contains the `count_diamond_colors` function, which counts and lists the colors of diamonds along with their counts.

### `calculate_median_carat.py`

This page contains the `calculate_median_carat` function, which calculates and displays the median carat of premium diamonds in the dataset.

### `calculate_average_carat_by_cut.py`

This page contains the `calculate_average_carat_by_cut` function, which calculates and displays the average carat for each cut type.

### `color_avrg_price.py`

This page contains the `calculate_average_price_by_color` function, which calculates and displays the average price for each color type.

## Usage

1. **Run the Script**

   Open a terminal or command prompt and navigate to the project directory.

   ```bash
   cd path/to/diamond-analysis-tool
   ```

   Run the script using the following command:

   ```bash
   python main.py
   ```

2. **Menu Options**

   - The script will display a menu with different analysis options.
   - Enter the number corresponding to the analysis option you want to perform and press Enter.

3. **View Results**

   - Depending on your chosen option, the script will display the results of the analysis on the terminal.

## Menu Utility

The menu utility provides functions for clearing the terminal screen and displaying the menu options.

- `clear_screen()`: Clears the terminal screen.
- `menu(options)`: Displays the menu options and takes user input.

## Contributing

Contributions to the Diamond Analysis Tool are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README further or add more sections as needed. Adjust the installation instructions and usage steps based on your project structure and requirements.