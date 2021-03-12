    # Pie chart of unique values
    # Author: Daniel Gonzalez

import numpy as np
import matplotlib.pyplot as plt

listOfCounties =    [
                "Antrim", "Armagh", "Carlow", "Cavan", "Clare", 
                "Cork", "Cork", "Donegal", "Down", "Dublin", "Cork", 
                "Galway", "Kerry", "Kildare", "Kilkenny", "Laois", "Leitrim", 
                "Cork", "Longford", "Louth", "Cork", "Meath", "Monaghan", "Offaly", 
                "Roscommon", "Sligo", "Tipperary", "Tyrone", "Cork", "Westmeath", 
                "Wexford", "Wicklow"
                    ]

counties = np.random.choice(listOfCounties, size= len(listOfCounties))

unique, counts = np.unique(counties, return_counts=True)
plt.pie(counts, labels=unique)
plt.show()