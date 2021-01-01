# Forest Land Analysis results:
## Description:
Deforestation is a major cause of ecological problems and global warming. This project is undertaken to analyze how much forest land is left in a particular region, the rate of afforestation/deforestation or if agriculture is one of the reasons for deforestation. This repository has four program files and two datasets.
## Data:
We have extracted the data from data.worldbank.org. We have used the agriculture land data and forest land data (in sq.km) from here:
Agriculture land data : https://data.worldbank.org/indicator/AG.LND.AGRI.K2
Forest land data : https://data.worldbank.org/indicator/AG.LND.FRST.K2 
## Analysis:
**1. Correlation of agriculture land vs. forest land**
As we know, the need for agricultural land is one of the major reasons for deforestation. We wanted to see if this is evident from the data. Below is the graph of two major countries India and Brazil:
![India: Graph of agricultural vs. forest land usage](agriculture_vs_forest_India.png?raw=true "India: Agriculture vs Forest Land")
![Brazil: Graph of agricultural vs. forest land usage](agriculture_vs_forest_Brazil.png?raw=true "Brazil: Agriculture vs Forest Land")
Use forest_vs_agriculture_land.py for these graphs.
These graphs show that indeed agriculture land and forest land are inversely proportional.

**2. Trend of change in forest land:**
We now evaluate how severe change is in the actual deforestation/afforestation of a specific country.
We have tried to estimate basic linear growth using simple line fitting though more complex analysis can be done.Presented below are the graphs of the same countries:
![India: Graph of forest area over the years](afforestation_of_India.png?raw=true "India: Forest area over the years")
![Brazil: Graph of forest area over the years](deforestation_of_Brazil.png?raw=true "Brazil: Forest area over the years")
Use forest_growth_trend.py for these graphs.

Here we see a contrast. The Brazil forest area is reducing steadily from the years 1990 to 2016, where the cause of deforestation is prominently the need for agricultural land. On the other hand the Indian forests land is actually growing in the same period and agricultural land is reducing.

**3. We finally look at different countries where change in forest land is significant.**
We have removed countries where rate of change is marginal below 0.15% and also removed many countries whose overall land area is below 50000 sq.kms. You can change these limitations in the code “forest_change_country_wise.py” to accommodate more or less countries in the plot. Below is the graph of the 28 prominent countries:
![Top countries of the world with significant forest area change.](change_of_forests_of_countries.png?raw=true "Top countries of the world with significant forest area change.")
The graph shows that these countries have the maximum rate of change in their forest area.

The countries which have a significant rise in afforestation are: Germany, Japan, South Africa, New Zealand, Poland, Romania, Ghana, Belarus, Gabon, Philippines and Italy.
The countries which have a significant rise in deforestation are: Norway, Papua New Guinea, Suriname, Guyana, South Korea, Congo, Sweden, Guinea, Madagascar, Canada etc.
