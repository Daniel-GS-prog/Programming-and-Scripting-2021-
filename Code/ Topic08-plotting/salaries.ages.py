# Distribution of ages and salaries
# Author: Daniel Gonzalez

import numpy as np
import matplotlib.pyplot as plt


# variables: 
minSalary = 20000
maxSalary = 80000
increment = 5000
minAge = 21
maxAge = 65

np.random.seed(1)
# Making same results each time

salaries = np.random.randint(minSalary, maxSalary, 100)
ages = np.random.randint(minAge, maxAge, 100)
#10 random salaries and ages
plt.scatter(ages, salaries, label="age - income")


x = np.arange(100)
y = x**2
z = x + 2
# range of x and x square
plt.plot(x, y, label="xsquared", color="blue")

plt.legend()
plt.show()