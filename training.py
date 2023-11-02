from flask import Flask, request, jsonify
import pandas as pd

from flask import Flask, render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open('//Users/volatylventures/Desktop/NFL-Prediction/model.pkl', 'rb'))
# Load the dataset
gameData = pd.read_csv('/Users/volatylventures/Desktop/NFL-Prediction/Game_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def get_predictions():
   
    # Get team abbreviations from the request query parameter
    team1_abbrev = request.args.get('team1')
    team2_abbrev = request.args.get('team2')
   
    # Look up the team details from the dataset
    team1_data = gameData[gameData['ABBREV'] == team1_abbrev].iloc[0]
    team2_data = gameData[gameData['ABBREV'] == team2_abbrev].iloc[0]

    # Select features
    feature_columns = ['Avg_PK%','Avg_PP%','Avg_S/GP%', 'Avg_PTS%', 'SV/GP', 'Avg_Goals']

    # Create a 2D array
    data = [team1_data[feature_columns].values.tolist(), team2_data[feature_columns].values.tolist()]

    # Make predictions using the model
    predictions = model.predict(data)

    probabilities = [predictions[0], predictions[1]]
    winning_probability = max(probabilities)
    losing_probability = min(probabilities)
    
# Determine the winning and losing teams
    winning_team = team1_data['TEAM'] if probabilities.index(
    winning_probability) == 0 else team2_data['TEAM']
    losing_team = team2_data['TEAM'] if probabilities.index(
    winning_probability) == 0 else team1_data['TEAM']
    

    result = {
        'winning_team': winning_team,
        'losing_team': losing_team,
        'win_prob': round(winning_probability,2),
        'losing_prob': round(losing_probability, 2),
        'team1': {
            'team': team1_data['TEAM'],
            'abbrev': team1_data['ABBREV'],
            'pp': team1_data['Avg_PP%'],
            'pk': team1_data['Avg_PK%'],
            'shots': team1_data['Avg_S/GP%'],
            'pts': team1_data['Avg_PTS%'],
            'saves': team1_data['SV/GP'],
            'goals': team1_data['Avg_Goals'],
            'wins': team1_data['Av_W%'],
            
            },
        'team2': {
        'team': team2_data['TEAM'],
        'abbrev': team2_data['ABBREV'],
        'pp': team2_data['Avg_PP%'],
        'pk': team2_data['Avg_PK%'],
        'shots': team2_data['Avg_S/GP%'],
        'pts': team2_data['Avg_PTS%'],
        'saves': team2_data['SV/GP'],
        'goals': team2_data['Avg_Goals'],
        'wins': team2_data['Av_W%'],
            
            }
        }

    return render_template('index.html', team_data=result )
  
   
if __name__ == '__main__':
    app.run(debug=True)