'''
This code controls the program. It will integrate the following functions: process_data(), avg_height(), tallest_shortest_athletes.

It scrapes athletes' data from various college athletic websites, processes player's heights and analyzes the data by sport and gender. A dictionary of URLs containing college athletes are used. For each team, athletes' name and height are scraped and placed into dataframes. The dataframes are used to identify the five tallest and shortest (including ties) athletes and returns the average height for each team, which will be visualized through a bar chart using matplotlib.
'''

# Import libraries 
import requests
from bs4  import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# This imports specific functions from other Python files into main.py.
from scrapedheights import process_data
from averageheights import avg_height
from topfivenameheight import tallest_shortest_athletes

# Dictionary containing team names and each roster's URL.
sports_teams = {
                    'Mens_Volleyball': ['https://ccnyathletics.com/sports/mens-volleyball/roster?view=2', 'https://lehmanathletics.com/sports/mens-volleyball/roster?view=2', 'https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster?view=2', 'https://johnjayathletics.com/sports/mens-volleyball/roster?view=2', 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster?view=2', 'https://mecathletics.com/sports/mens-volleyball/roster?view=2', 'https://www.huntercollegeathletics.com/sports/mens-volleyball/roster?view=2', 'https://yorkathletics.com/sports/mens-volleyball/roster', 'https://ballstatesports.com/sports/mens-volleyball/roster'],
                    'Womens_Volleyball': ['https://bmccathletics.com/sports/womens-volleyball/roster?view=2', 'https://yorkathletics.com/sports/womens-volleyball/roster', 'https://hostosathletics.com/sports/womens-volleyball/roster?view=2', 'https://bronxbroncos.com/sports/womens-volleyball/roster/2021?view=2', 'https://queensknights.com/sports/womens-volleyball/roster?view=2', 'https://augustajags.com/sports/wvball/roster?view=2', 'https://flaglerathletics.com/sports/womens-volleyball/roster?view=2', 'https://pacersports.com/sports/womens-volleyball/roster', 'https://www.golhu.com/sports/womens-volleyball/roster?view=2'],
                    'Mens_Swimming_Diving': ['https://csidolphins.com/sports/mens-swimming-and-diving/roster/2023-2024?view=2', 'https://yorkathletics.com/sports/mens-swimming-and-diving/roster', 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster?view=2', 'https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster/2024-25?view=2', 'https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster?view=2', 'https://mckbearcats.com/sports/mens-swimming-and-diving/roster?view=2', 'https://ramapoathletics.com/sports/mens-swimming-and-diving/roster?view=2', 'https://oneontaathletics.com/sports/mens-swimming-and-diving/roster?view=2', 'https://binghamtonbearcats.com/sports/mens-swimming-and-diving/roster/2021-22?view=2', 'https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22?view=2'],
                    'Womens_Swimming_Diving': ['https://csidolphins.com/sports/womens-swimming-and-diving/roster/2023-2024?view=2', 'https://queensknights.com/sports/womens-swimming-and-diving/roster?view=2', 'https://yorkathletics.com/sports/womens-swimming-and-diving/roster', 'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?view=2', 'https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster?view=2', 'https://mckbearcats.com/sports/womens-swimming-and-diving/roster?view=2', 'https://ramapoathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://keanathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://oneontaathletics.com/sports/womens-swimming-and-diving/roster?view=2']
                }

# Dictionary to map each output CSV file
team_csvs = {}

# For each team, this will scrape, save to CSV, and map the name of each CSV file back to the team_csvs dictionary.
for team in sports_teams:
  df = process_data(sports_teams[team])
  file_name = team + '.csv'
  df.to_csv(file_name, index = False)
  team_csvs[file_name] = team.replace('_', ' ')

# Calls the tallest_shortest_athletes(team_csvs) function and returns the list of tallest and shortest athletes from the urls.
tallest_shortest_athletes(team_csvs)

# Empty list to hold the average heights.
avg_data = []

# Computes the average heights for each of the 4 teams by using the avg_height(frame) function. The results are printed and added to the avg_data list.
print('\nAverage Heights in Inches:')
for csv, team_name in team_csvs.items():
  df = pd.read_csv(csv)
  avg = avg_height(df)
  print(f'{team_name}: {avg} inches')
  avg_data.append({'Team': team_name, 'Average Height': avg})

# Plots a bar chart comparing the average heights.
avg_data_df = pd.DataFrame(avg_data)
avg_data_df.plot.bar(x = 'Team', y = 'Average Height', title = 'Average Heights Among Athletes in Inches')
plt.show()