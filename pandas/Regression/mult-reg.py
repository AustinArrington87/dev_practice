import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("winequality.csv")
#print(dataset.shape)

# stat details 
#print(dataset.describe())

# check for nulls 
print(dataset.isnull().any())
# if there are nulls, fix like this: 
dataset = dataset.fillna(method='ffill')

#X = attribute, Y = label 
X = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']].values
y = dataset['quality'].values

# split data between training and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train model
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# now see what coefficients the model has chosen
#coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])

# prediction on test data
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)
print(df1)

# plot actual vs predicted
df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# evaluate
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


