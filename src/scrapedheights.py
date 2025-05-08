import libraries
import requests
from bs4  import BeautifulSoup
import pandas as pd
# Creates a dictionary of lists conaining links for scrapping
sports_teams = {
                    'mens_volleyball': ['https://ccnyathletics.com/sports/mens-volleyball/roster?view=2', 'https://lehmanathletics.com/sports/mens-volleyball/roster?view=2', 'https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster?view=2', 'https://johnjayathletics.com/sports/mens-volleyball/roster?view=2', 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster?view=2', 'https://mecathletics.com/sports/mens-volleyball/roster?view=2', 'https://www.huntercollegeathletics.com/sports/mens-volleyball/roster?view=2', 'https://yorkathletics.com/sports/mens-volleyball/roster', 'https://ballstatesports.com/sports/mens-volleyball/roster'],
                    'womens_volleyball': ['https://bmccathletics.com/sports/womens-volleyball/roster?view=2', 'https://yorkathletics.com/sports/womens-volleyball/roster', 'https://hostosathletics.com/sports/womens-volleyball/roster?view=2', 'https://bronxbroncos.com/sports/womens-volleyball/roster/2021?view=2', 'https://queensknights.com/sports/womens-volleyball/roster?view=2', 'https://augustajags.com/sports/wvball/roster?view=2', 'https://flaglerathletics.com/sports/womens-volleyball/roster?view=2', 'https://pacersports.com/sports/womens-volleyball/roster', 'https://www.golhu.com/sports/womens-volleyball/roster?view=2'],
                    'mens_swimming_diving': ['https://csidolphins.com/sports/mens-swimming-and-diving/roster/2023-2024?view=2', 'https://yorkathletics.com/sports/mens-swimming-and-diving/roster', 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster?view=2', 'https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster/2024-25?view=2', 'https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster?view=2', 'https://mckbearcats.com/sports/mens-swimming-and-diving/roster?view=2', 'https://ramapoathletics.com/sports/mens-swimming-and-diving/roster?view=2', 'https://oneontaathletics.com/sports/mens-swimming-and-diving/roster?view=2', 'https://binghamtonbearcats.com/sports/mens-swimming-and-diving/roster/2021-22?view=2', 'https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22?view=2'],
                    'womens_swimming_diving': ['https://csidolphins.com/sports/womens-swimming-and-diving/roster/2023-2024?view=2', 'https://queensknights.com/sports/womens-swimming-and-diving/roster?view=2', 'https://yorkathletics.com/sports/womens-swimming-and-diving/roster', 'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?view=2', 'https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster?view=2', 'https://mckbearcats.com/sports/womens-swimming-and-diving/roster?view=2', 'https://ramapoathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://keanathletics.com/sports/womens-swimming-and-diving/roster?view=2', 'https://oneontaathletics.com/sports/womens-swimming-and-diving/roster?view=2']
                }

#create function to process urls
def process_data(urls):

    #list to store names
    names = []
    #list to store heights
    heights = []
    #counter for while loop
    counter = 0

    # loop to visit each url
    for url in urls:

       # make request to server
       page = requests.get(url)
       #process data if request is successful
       if page.status_code == 200:
           # import raw html into beautiful soup
            soup = BeautifulSoup(page.content,'html.parser')
            #identifies the tag with the athlete's name
            name_tag = soup.find_all('td', class_="sidearm-table-player-name")
            # identifies the tag with the heights
            height_tag = soup.find_all('td', class_="height")
            #iterates through the entire list
            while counter < len(name_tag) - 1:
                if height_tag[counter].get_text().find('-') > 0: # skips anyone with invalid height
                    names.append(name_tag[counter].get_text())
                    heights.append(height_tag[counter].get_text())
                    counter +=1 #increments the counter
                else:
                  counter += 1   #increments the counter regardless if the height is empty or not
       else:
        continue



    # strips extra whitespace in each name
    names = list(map(lambda x : x.strip(), names))
    # strips whitespace and splits the height into feet/inches seperate
    heights = list(map(lambda x : x.strip().split('-'), heights))
    #adds the total height in inches
    heights = list(map(lambda x : (float(x[0]) * 1.0 * 12) + (float(x[1]) * 1.0)  , heights))


    #create pandas dataframe from the names list and heights list
    data = {
            'Name' : names,
            'Height': heights
          }
    df = pd.DataFrame(data)

    return df #return the dataframe

#create dataframe for each sport using the corresponding list of urls
mens_volleyball_df = process_data(sports_teams['mens_volleyball'])
womens_volleyball_df = process_data(sports_teams['womens_volleyball'])
mens_swimming_diving_df = process_data(sports_teams['mens_swimming_diving'])
womens_swimming_diving_df = process_data(sports_teams['womens_swimming_diving'])

#output data as csv file for each sport
mens_volleyball_df.to_csv('Mens_Volleyball.csv', index=False)
womens_volleyball_df.to_csv('Womens_Volleyball.csv', index=False)
mens_swimming_diving_df.to_csv('Mens_Swimming_Diving.csv', index = False)
womens_swimming_diving_df.to_csv('Womens_Swimming_Diving.csv', index = False)
