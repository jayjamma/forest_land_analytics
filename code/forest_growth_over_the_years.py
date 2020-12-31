import csv
import matplotlib.pyplot as plt
import numpy as np 

def load_data(file_name):
    with open(file_name) as csv_file:
        land_data = dict()
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                headers = row
                line_count += 1
                headers[0] = "Country"
            else:
                cell_count = 0
                data = dict()
                for cell in row:
                    data[headers[cell_count]] = row[cell_count] 
                    cell_count += 1
                land_data[data["Country Code"]] = data
            line_count += 1
    return land_data

def extract_series(country_code,data):
    series = list()
    years = list()
    for year in range(1993, 2016): 
        series.append(float(data[country_code][str(year)]))
        years.append(float(year))
    return series,years

def country_stats(country_code):
    global forest_list
    global agri_list
    global urban_list
    
    forest_list, years = extract_series(country_code, forest_data)
    agri_list, x = extract_series(country_code, agri_data)
    #urban_list, x = extract_series(country_code, urban_data)
    trend, c = np.polyfit(np.array(forest_list),np.array(years), 1)
    covariance, c = np.polyfit(np.array(agri_list),np.array(forest_list), 1)
    return trend,covariance

forest_data = load_data('Forest Area.csv')
agri_data = load_data('Agriculture Area.csv')
#urban_data = load_data('Urbanization data.csv')

#country_code = "BRA"

#print(trend, covarience)
country_codes = forest_data.keys()
#print(country_codes)
trend_lst = list()
covarience_lst = list()
country_lst = list()
country_count = 1
for country in country_codes:
    try:
        value = forest_data[country]['2000']
        if float(value) < 50000.0:
            continue

        trend, covarience = country_stats(country)
        #if trend > 15 or trend < -15:
        #    continue
        #if covarience > 5 or covarience <-5:
        #    continue
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
#plt.plot(trend_lst)
#plt.scatter(covarience_lst,trend_lst)
#plt.scatter(agri_list, forest_list)
#plt.scatter(agri_list, urban_list)
plt.show()
#print(agri_data)

