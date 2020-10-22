import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

# import locally saved file
Covid = pd.read_excel('World_data.xlsx')

# import world shape map externally, no need to have a saved file
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

Europe = world[world["continent"] == "Europe"]
capitals = gpd.read_file(gpd.datasets.get_path("naturalearth_cities"))
# Create a custom polygon
polygon = Polygon([(-25, 30), (-25, 75), (50, 75), (50, 30), (-25, 30)])
poly_gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs=world.crs)
capitals_clipped = gpd.clip(capitals, Europe)
world_clipped = gpd.clip(Europe, polygon)

# merge both data sets using country code/iso_a3 as unique identifiers
for_plotting = world_clipped.merge(Covid, left_on='iso_a3', right_on='CODE')
# check the occurrence
for_plotting.info()

# plot merged file. use dropna to remove any country with no revenue value
ax = for_plotting.plot(figsize=(15, 9), column='Deaths', cmap='Reds', legend=True)

# add title to the map
ax.set_title('Total Deaths of COVID-19', fontdict={'fontsize': 25})

# remove axes
ax.set_axis_off()
# move legend to an empty space
#ax.get_legend().set_bbox_to_anchor((.12, .12))
ax.get_figure()

plt.show()