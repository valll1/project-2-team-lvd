'''
This function analyzes the heights of athletes from men's volleyball team, women's volleyball team, men's swimming and diving team, and women's swimming and diving team.
For each team, the code will print all athletes who are among the tallest 5 (including ties) and shortest 5 (including ties).
'''

def tallest_shortest_athletes(team_csvs):
	# Loops through each key in the team_csvs dictionary and finds the tallest 5 and shortest 5 athletes for each team.
	for csv in team_csvs:
		team_name = team_csvs[csv]
		df = pd.read_csv(csv)

		# Sort the heights from tallest to shortest and finds the tallest 5 heights.
		sorted_df = df.sort_values(by = 'Height', ascending = False)
		top_heights = sorted_df['Height'].nlargest(5).unique()
		fifth_tallest = top_heights[-1]

		# Include all athletes that have a height greater than the fifth tallest height to include anyone who has the same height.
		tallest = sorted_df[sorted_df['Height'] >= fifth_tallest]

		# Team, Name, and Height are printed.
		print(f'\nTallest Athletes in {team_name}:')
		print(tallest[['Name', 'Height']])

		# Sort the heights from shortest to tallest and finds the shortest 5 heights.
		sorted_df_asc = df.sort_values(by = 'Height', ascending = True)
		shortest_heights = sorted_df_asc['Height'].nsmallest(5).unique()
		fifth_shortest = shortest_heights[-1]

		# Include all athletes that have a height shorter than the fifth shortest height to include anyone who has the same height.
		shortest = sorted_df_asc[sorted_df_asc['Height'] <= fifth_shortest]

		# Team, Name, and Height are printed.
		print(f'\nShortest Athletes in {team_name}:')
		print(shortest[['Name', 'Height']])