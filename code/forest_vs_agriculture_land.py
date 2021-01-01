import csv
import matplotlib.pyplot as plt
import numpy as np
from analytics import load_data
from analytics import extract_series

country_code = input("Enter Country Code:")

# Load data
forest_data = load_data('../data/forest area.csv')
agri_data = load_data('../data/agriculture area.csv')

forest_list, years = extract_series(country_code, forest_data)
agri_list, x = extract_series(country_code, agri_data)

# Scatter plot 
m, c = np.polyfit(np.array(agri_list),np.array(forest_list), 1)
print("Agri vs Forest:",m)
plt.scatter(agri_list, forest_list)

# Trend line
z = np.polyfit(agri_list, forest_list, 1)
p = np.poly1d(z)
plt.plot(agri_list,p(agri_list),"y--")

# Plot everything
plt.show()