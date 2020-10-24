# Data from John Hopkins
# https://github.com/CSSEGISandData

import pandas as pd
import geopandas as gpd
import PIL
import io
from shapely.geometry import Polygon

# Reading in the csv data
data = pd.read_csv('time_series_covid19_confirmed_global.csv')

# Group data by the country
data = data.groupby('Country/Region').sum()

# Drop Lat and Lon columns
data = data.drop(columns = ['Lat', 'Long'])

# Create a transpose of the dataframe
data_transposed = data.T
##data_transposed.plot(y = ["France", "Germany", "United Kingdom", "Italy"],
                     ##use_index = True, figsize = (8,8), marker = '*')

# Read in the world map shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# To mitigate discrepancies change name in shapefile with name in database
world.replace('Czech Republic','Czechia', inplace = True)
world.replace('Republic of Moldova','Moldova', inplace = True)
world.replace('The former Yugoslav Republic of Macedonia','North Macedonia', inplace = True)
world.replace('Syrian Arab Republic','Syria', inplace = True)
world.replace('Palestine','West Bank and Gaza', inplace = True)
world.replace('Bosnia and Herz.', 'Bosnia and Herzegovina', inplace = True)
world.replace('Macedonia','North Macedonia', inplace = True)



Europe = world[world["continent"] == "Europe"]
capitals = gpd.read_file(gpd.datasets.get_path("naturalearth_cities"))

# Create a custom polygon
polygon = Polygon([(-25, 30), (-25, 75), (50, 75), (50, 30), (-25, 30)])
poly_gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs=world.crs)
capitals_clipped = gpd.clip(capitals, Europe)
world_clipped = gpd.clip(Europe, polygon)

## Checking the names of the countries for any discrepancies
#for index, row in data.iterrows():
    #if index not in world_clipped['name'].to_list():
        #print(index + ' is not in the shapelist')
    #else:
        #pass

# Merge info from two sources into one
merge = world_clipped.join(data, on = 'name', how = 'right')

image_frames = []

#first is at 6 last at 281
for dates in merge.columns.to_list()[6:281]:

    # Plot
    ax = merge.plot(column = dates,
                    cmap = 'OrRd',
                    figsize = (14,14),
                    legend = True,
                    scheme = 'user_defined',
                    classification_kwds = {'bins': [10, 100, 1000, 2500, 5000, 10000,
                                                    25000, 50000, 100000, 200000, 500000, 1000000]},
                    edgecolor = 'black',
                    linewidth = 0.4)

    # Add a title to the map
    ax.set_title('Total Confirmed Coronavirus Cases '+ dates, fontdict =
    {'fontsize':20}, pad = 12.5)

    # Removing the axes
    ax.set_axis_off()

    # Move the legend
    ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

    img = ax.get_figure()


    f = io.BytesIO()
    img.savefig(f, format = 'png', bbox_inches = 'tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))


# Create GIF animation from the images
image_frames[0].save('Dynamic Covid-19 Europe Map.gif', format = 'GIF',
                     append_images = image_frames[1:],
                     save_all = True, duration = 150,
                     loop = 1)

f.close()

print('success!')
