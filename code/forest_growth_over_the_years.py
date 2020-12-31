import csv
import matplotlib.pyplot as plt
import numpy as np 
import analytics.py

forest_data = load_data('Forest Area.csv')
agri_data = load_data('Agriculture Area.csv')
country_codes = forest_data.keys()

trend_lst = list()
covarience_lst = list()
country_lst = list()
for country in country_codes:
    try:
        value = forest_data[country]['2000']
        if float(value) < 50000.0:
            continue
        trend, covarience = country_stats(country)
        if abs(trend) < 0.0014 :
            continue
        print(country_count,"Country {} Forest {}".format(country,value))
        country_count = country_count + 1
        country_lst.append(country)
        trend_lst.append(trend)
        covarience_lst.append(covarience)
    except:
        continue

plt.bar(country_lst,trend_lst)
plt.show()