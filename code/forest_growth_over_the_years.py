import csv
import matplotlib.pyplot as plt
import numpy as np
from analytics import load_data
from analytics import country_stats

forest_data = load_data('../data/forest area.csv')
agri_data = load_data('../data/agriculture area.csv')
country_codes = forest_data.keys()

trend_lst = list()
covarience_lst = list()
country_lst = list()
country_count = 0
for country in country_codes:
    try:
        value = forest_data[country]['2000']
        if float(value) < 50000.0:
            continue
        trend, covarience = country_stats(country,forest_data,agri_data)
        #print("Trend:", trend, abs(trend))
        if abs(trend) < 0.0014 :
            continue
        print("Trend:", trend, abs(trend))
        print(country_count,"Country {} Forest {}".format(country,value))
        country_count = country_count + 1
        country_lst.append(country)
        trend_lst.append(trend)
        covarience_lst.append(covarience)
    except Exception as e:
        print(e)
        continue
print("----------------------------------------------------------------")
print(trend_lst)
plt.bar(country_lst,trend_lst)
plt.show()