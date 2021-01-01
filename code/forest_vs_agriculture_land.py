import csv
import matplotlib.pyplot as plt
import numpy as np
from analytics import load_data
from analytics import extract_series

country_code = input("Enter Country Code:")

forest_data = load_data('../data/forest area.csv')
agri_data = load_data('../data/agriculture area.csv')

forest_list, years = extract_series(country_code, forest_data)

agri_list, x = extract_series(country_code, agri_data)

m, c = np.polyfit(np.array(agri_list),np.array(forest_list), 1)
print("Agri vs Forest:",m)
m, c = np.polyfit(np.array(forest_list), np.array(years),1)
print("Forest Trend:",m)
plt.scatter(agri_list, forest_list)
plt.show()