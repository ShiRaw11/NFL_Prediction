import pandas as pd
import pickle

# Load the trained model
model = pickle.load(
    open('//Users/volatylventures/Desktop/NFL-Prediction/model.pkl', 'rb'))
# Load  dataset
gameData = pd.read_csv(
    '/Users/volatylventures/Desktop/NFL-Prediction/Game_data.csv')

# Prompt  FOR entering  the names of the two teams
while True:
    team1 = input("Enter the name of Team 1: ")
    team2 = input("Enter the name of Team 2: ")

    # Check if both teams are entered
    if team1 and team2:
        break  
    else:
        print("Error: Please enter names for both teams.")

# Look up the team details from the dataset
team1_data = gameData[gameData['ABBREV'] == team1].iloc[0]
team2_data = gameData[gameData['ABBREV'] == team2].iloc[0]

# features
feature_columns = ['Avg_PK%', 'Avg_PP%',
                   'Avg_S/GP%', 'Avg_PTS%', 'SV/GP', 'Avg_Goals']

# array
data = [team1_data[feature_columns].values.tolist(
), team2_data[feature_columns].values.tolist()]

# Make predictions
prediction = model.predict(data)

probabilities = [prediction[0], prediction[1]]
winning_probability = max(probabilities)
losing_probability = min(probabilities)

# get the winning and losing teams
print(f'Data for {team1_data['TEAM']}: \n{team1_data[feature_columns]}')
print(f'Data for {team2_data['TEAM']}: \n{team2_data[feature_columns]}')
if winning_probability == losing_probability:
    print(f'Both teams have the same winning probability of {
          winning_probability}')
else:
    winning_team = team1_data['TEAM'] if probabilities.index(
        winning_probability) == 0 else team2_data['TEAM']
    losing_team = team2_data['TEAM'] if probabilities.index(
        winning_probability) == 0 else team1_data['TEAM']
    print(f"The predicted winner is {
        winning_team} with a probability of {winning_probability}%")
    print(f"The predicted loser is {
        losing_team} with a probability of {losing_probability}%")
