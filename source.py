#%%
#import libs and dataset
import pandas as pd
import numpy as np

data = pd.read_csv("./operations.csv",delimiter=',')

#%%
#get the location of bombing sites
locations = data[['Target Latitude','Target Longitude']]
print(locations)
#%%
