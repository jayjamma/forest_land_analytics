import csv
import matplotlib.pyplot as plt
import numpy as np
from analytics import load_data
from analytics import extract_series

def forest_trendline(country_code, forest_data):
	forest_list, years = extract_series(country_code, forest_data)
	plt.scatter(years, forest_list)
	# Trend line
	z = np.polyfit(years, forest_list, 1)
	p = np.poly1d(z)
	plt.plot(years,p(years),"y--")

country_code = input("Enter Country Code:")
forest_data = load_data('../data/forest area.csv')
forest_trendline(country_code, forest_data)

plt.show()