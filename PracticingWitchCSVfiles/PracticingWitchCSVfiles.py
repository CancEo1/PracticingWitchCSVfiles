# Program to read, write, and edit CSV files for Python
movies = [["Nezha", 2019, "Animation", 7.9],
          ["The Lord of the Rings: The Return of the King", 2003, "Fantasy", 9.0],
          ["Star Wars: Episode III - Revenge of the Sith", 2005, "Sci-Fi", 7.5]]

import csv

# How to write the list to a CSV file
with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)