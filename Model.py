import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pickle

# Load he CSV file
gameData = pd.read_csv('/Users/volatylventures/Desktop/NFL-Prediction/Game_data.csv')

feature_columns = ['Avg_PK%','Avg_PP%','Avg_S/GP%','Avg_PTS%','SV/GP','Avg_Goals']
#  target variable
target_column = 'Av_W%'
data = gameData[feature_columns + [target_column]]
# Create the feature matrix
X = gameData[feature_columns]
y = gameData[target_column]

# Split the dataset into a training set (70%) and a testing set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#model to use
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

#  make predictions
y_pred = model.predict(X_test)
#calculate mse and r2
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

for feature in feature_columns:
    plt.figure()
    plt.scatter(data[feature], data[target_column])
    plt.xlabel(feature)
    plt.ylabel(target_column)
    plt.title(f'Scatter Plot of {feature} vs. {target_column}')
    plt.show()

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared (R2): {r2:.2f}')

pickle.dump(model, open('model.pkl','wb'))

