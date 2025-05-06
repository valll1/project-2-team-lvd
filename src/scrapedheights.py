#import libraries
import requests
from bs4  import BeautifulSoup
import pandas as pd


#create dictionary of all the websites
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

    # loop to visit each url
    for url in urls:
       # make request to server
       page = requests.get(url)

    # process data if request is successful
    if page.status_code == 200:
      # import raw html into beautiful soup
      soup = BeautifulSoup(page.content,'html.parser')

     # extract height from the td tags
      height_tags = soup.find_all('td', class_='height')

      # loop through each td tag and extract content for heights
      for height_tag in height_tags:
        raw_height = height_tag.get_text()
        #only process players that have a given height that is not an empty string
        if len(raw_height.split('-')) == 2 and raw_height.split('-')[0]!= '':
          # extract the feet and inches from the list and convert string into floats
          feet = float(raw_height.split('-')[0]) * 12 #convert feet to inches by multiplying by 12
          inches = float(raw_height.split('-')[1]) #extract inches from the list
          height_in_inches = feet + inches #add to find the total inches
          heights.append(height_in_inches) #append height in inches to the heights list

          #extract the name of the player only if the height is given and not an empty string
          #find can be used instead of find all since the for loop is going through each player for the height
          name_tags = soup.find('td', class_='sidearm-table-player-name')
          #extract and append each name that has a given height into the names list
          names.append(name_tags.get_text().strip())
        #if the player does not have a given height or it is an empty string continue to the next player
        else:
          continue

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
womens_swimming_diving_df.to_csv('Womens_Swimming_Diving', index = False)