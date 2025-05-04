''' This function will find the average height in a given data frame'''
def avg_height(frame): # Defines the function that will take the frames
  avg_height = round(frame['Height'].sum() * 1.0 / len(frame['Height']),2) # Finds the avg of heights (in inches)
  return avg_height # returns the average height of the data frame
