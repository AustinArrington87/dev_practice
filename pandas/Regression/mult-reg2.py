# Source: https://www.w3schools.com/python/python_ml_multiple_regression.asp

####### Move on to  Multiple Regression 

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[["Weight", "Volume"]]
y = df["CO2"]

# creattet regression Object 
regr = linear_model.LinearRegression()
regr.fit(X,y)

# print regression coeffs
print("Coefficients: ")
print(regr.coef_)

# [0.00755095 0.00780526] - weight , vol

# predict CO2 emission of car where weight 2300g and volume 1300ccm

predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)

