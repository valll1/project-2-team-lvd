# Project #2: Question 2
This project involves implementing a Python program that scrapes the names and heights of athletes across ten different schools, computing the average height per sport by gender, and returns the ten tallest and shortest athletes by sport and gender.

To run the program, run: python src/main.py

## Members: 
* Lydia Mei
* Valeria Ortega Preciado
* Dora Zhu 

## Allocation of tasks
Lydia Mei - Lydia was in charge of implementing the process_data function, which takes the dictionary of urls as a parameter, creating requests and scraping the desired data by HTML tag. Data was put into gender and sport-specific dataframes, which were later exported as csv files. 

Valeria Ortega Preciado - Valeria was in charge of creating the average_heights function which takes a dataframe as a parameter, summing the height columns and dividing it by the length of the column to calculate and return the average height. Additionally, Valeria created the SQLite database, inserted rows into their respective tables, and wrote the README.md file highlighting all contributions made by each member.

Dora Zhu - Dora created the tallest_shortest_athletes function that takes a csv file as a parameter, and returns the five tallest and five shortest athletes. Athletes that were tied for each position were also included. Additionally, Dora created the bar charts of the average heights across every data frame, implemented the main() function, and integrated functions into main branch. 
