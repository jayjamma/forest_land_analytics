import csv

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
    forest_list, years = extract_series(country_code, forest_data)
    agri_list, x = extract_series(country_code, agri_data)
    trend, c = np.polyfit(np.array(forest_list),np.array(years), 1)
    covariance, c = np.polyfit(np.array(agri_list),np.array(forest_list), 1)
    return trend,covariance