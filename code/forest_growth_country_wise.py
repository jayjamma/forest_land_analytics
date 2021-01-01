import csv
import matplotlib.pyplot as plt
import numpy as np
from analytics import load_data
from analytics import country_stats

forest_data = load_data('../data/forest area.csv')
agri_data = load_data('../data/agriculture area.csv')
country_codes = forest_data.keys()

trend_lst = list()
trend_map = dict()
covarience_lst = list()
country_lst = list()
country_count = 0
for country in country_codes:
    try:
        value = forest_data[country]['2000']
        if float(value) < 50000.0:
            continue
        trend, covarience = country_stats(country,forest_data,agri_data)
        if abs(trend) < 0.0014 :
            continue
        #print(country_count,"Country {} Forest {}".format(country,value))
        #print("Trend:", trend, abs(trend))
        country_count = country_count + 1
        country_lst.append(country)
        trend_lst.append(trend)
        covarience_lst.append(covarience)
        trend_map[country] = trend
    except Exception as e:
        continue

sorted_keys = sorted(trend_map, key=trend_map.get)
sorted_map = dict()
for k in sorted_keys:
    sorted_map[k] = trend_map[k]
#{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
#{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
print(sorted_map.keys(),sorted_map.values())
plt.bar(sorted_map.keys(),sorted_map.values())
plt.show()
