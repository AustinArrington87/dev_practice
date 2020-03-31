# Source: https://www.w3schools.com/python/python_ml_multiple_regression.asp

#  https://www.w3schools.com/python/python_ml_linear_regression.asp

# stdev
#import numpy
#speed = [86,87,88,86,87,85,86]
#x = numpy.std(speed)
# numpy.mean, numpy.median()

# start w linear reg
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

# run each value of x array through function
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print("R2: ")
print(r)


#  make prediction 
# speed of 10-yr old car ?

speed = myfunc(10)
print("Speed: ")
print(speed)
