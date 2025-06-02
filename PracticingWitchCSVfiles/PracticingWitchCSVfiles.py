# Program to read, write, and edit CSV files for Python
movies = [["Nezha", 2019, "Animation", 7.9],
          ["The Lord of the Rings: The Return of the King", 2003, "Fantasy", 9.0],
          ["Star Wars: Episode III - Revenge of the Sith", 2005, "Sci-Fi", 7.5]]

import csv

# How to write the list to a CSV file
with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)

# How to read the CSV file instead of finding the project folder
# This essentially brings the CSV file to the Python IDE
with open("movies.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} ({row[1]}) - Genre: {row[2]}, Rating: {row[3]}")