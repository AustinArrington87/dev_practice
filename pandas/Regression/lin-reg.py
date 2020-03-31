# source: https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('Weather.csv')

print(dataset.shape)
print(dataset.describe())

#dataset.plot(x='MinTemp', y='MaxTemp', style='o')
#plt.title('MinTemp vs MaxTemp')
#plt.xlabel('MinTemp')
#plt.ylabel('MaxTemp')
#plt.show()

X = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

# 80% for training, 20% to test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("Intercept: ")
print(regressor.intercept_)
print("Slope: ")
print(regressor.coef_)

#  now make predictions on test data
y_pred = regressor.predict(X_test)

# now compare output for X_test values with the predicted vals 

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
#print(df)

# visualize bar graph 
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# evaluate models
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))







