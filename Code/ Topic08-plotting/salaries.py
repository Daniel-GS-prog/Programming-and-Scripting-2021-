# makes a random list of salaries
# Author: Daniel Gonzalez

import numpy as np



# variables: 
minSalary = 20000
maxSalary = 80000
increment = 5000

np.random.seed(1)
# Making same results each time

salaries = np.random.randint(minSalary, maxSalary, 10)
#10 random salaries

incrementedSalaries = increment + salaries
# Salaries incremente by 5000

newSalaries = 1.05 * salaries
newSalaries = newSalaries.astype(int)
# Salaries incremented by 5% and fromatted to int type


# Print out results: 
print('\nInitial salaries: {} .'.format(salaries))
print("\nSalaries with 5000 increment: {}.".format(incrementedSalaries))
print("\nSalaries with 5% increment: {}. \n".format(newSalaries))
