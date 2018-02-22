"""
  Simple Regression AI
  By jdw136
"""

import numpy as np  #import the required modules
from math import *

"""
  If you want to change up the program, change the x and the y values here, or even add some.  Just make sure that there is an equal number of x and y values.
"""

x = [1.0,2.0,4.0,3.0,5.0] #put the x-values into an array.
y = [1.0,3.0,3.0,2.0,5.0] #put the y-value into an array.

mean_x = 1/len(x)*sum(x)  #Find the mean of the x-values.
mean_y = 1/len(y)*sum(y)  #Find the mean of the y-values.

error_x_array = []  # Create an array to store all the values of the errors for the x-values.
error_y_array = []  #Create an array to store all the values of the error for the -values.
final_error = []  #Create an array so you can easily find the sum of all the errors
b1_denom = [] #Create an error so you can easily find the sum of the x-values, so you can find the denominator of B1.

for a in range(len(x)): 
  error_x = mean_x - x[a] #Find the error for ALL of the x-values.
  error_x_array.insert(len(error_x_array), error_x) #Insert each of the errors into our array for easy use.
for a in range(len(y)):
  error_y = mean_y - y[a] #Find the error for ALL the y-values.
  error_y_array.insert(len(error_y_array), error_y) #Insert each of the errors for the y-axis into out array.

for a in range(len(x)):
  final_error1 = error_x_array[a] * error_y_array[a]  #Find the final error for all of the x and y values.
  final_error.insert(len(final_error), final_error1)  #Insert all the final errors into out array.

for a in range(len(x)):
  b1_denom1 = (x[a]-mean_x)**2  #Find our denominator for each of our values.
  b1_denom.insert(len(b1_denom), b1_denom1) #Insert each of our denominators into our array.
  
numerator = sum(final_error)  #Find the numerator using the sum of all the values in our final_error array.
denomerator = sum(b1_denom) #Find the denominator using the sum of all our denominators we found.
real_B1 = numerator/denomerator #Divide our numerator by our denominator to find the value of B1.

B0 = mean_y-real_B1*mean_x  #Find the value of B0.

print ("Equation: y=" + str(real_B1) + "+" + str(B0) + "x") #Print out our equation that we found using the values of B1 and B0.

x_value = float(input("Enter the x-value: ")) #Ask the user to define the x-value.
answer = real_B1+B0*x_value #Use our equation that we defined and the x-value defined by the user to find the expected y-value.
print (answer)  #Print out the expected y-value.

"""
  Ending Notes:
    AI is never an exact science.  You can test how inaccurate the program is by inputing 1 as the x-value and comparing that to the y-value listed.
    For example, when 1 is inputed as the x-value, it outputs 1.2 instead of the expected value of 1 for y.  This means that it is about 0.2 units off.
"""