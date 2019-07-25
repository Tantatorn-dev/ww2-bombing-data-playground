# %%
# import libs and dataset
import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./operations.csv", delimiter=',')
data = data.head(100)

# %%
# get the location of bombing sites
locations = data[['Target Latitude', 'Target Longitude']]
# %%
# print all locations of bombing sites on a world map
gdf = geopandas.GeoDataFrame(locations, geometry=geopandas.points_from_xy(
    locations['Target Longitude'], locations['Target Latitude']))

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world.plot()

gdf.plot(ax=ax,color='blue',markersize=1)
plt.plot()
# %%
