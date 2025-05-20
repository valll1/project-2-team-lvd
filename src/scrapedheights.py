import libraries
import requests
from bs4  import BeautifulSoup
import pandas as pd

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
