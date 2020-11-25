import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


import folium
import pandas as pd
import webbrowser

# define the world map
world_map = folium.Map()

# display world map

world_map

# San Francuisco latitude and longitude values

latitude = 37.77
longitude = -122.42

# Create map and display it

san_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Display the map of San Francisco
san_map


import numpy as np
from sklearn import linear_model

from sklearn import linear_model
import scikitplot as skplt
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print(reg.coef_)
