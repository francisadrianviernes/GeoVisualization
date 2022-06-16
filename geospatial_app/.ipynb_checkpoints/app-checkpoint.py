#Preliminaries
from greppo import app
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

#STEP 1 - CREATE A BASE LAYER
#Create Base Layer
app.base_layer(
    name="Open Street Map",
    visible=True,
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    subdomains=None,
    attribution='(C) OpenStreetMap contributors',
)

app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
)

#STEP 2 - IMPORT THE DATA AND MAKE IT READABLE
df = pd.read_csv('Coffee Brands Footprint.csv',
                index_col=0)
#Geometry
geometry = [Point(xy) for xy in zip(df.lng, df.lat)]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

#STEP 3 - ADD COFFEE SHOPS AS VECTOR LAYERS
#We need to add this iteratively, to achieve different colors in the map, we need to separate the brands and treat them as a dataframe

#Borrowing this from our earlier codes
color_dict = {
    "Starbucks": ' #00704A',
    "Coffee Bean and Tea Leaf": '#362d26',
    "Coffee Project": '#654321',
    "Tim Hortons": '#dd0f2d'
}

for brand in color_dict.keys():
    
    app.vector_layer(
        data = gdf[gdf.brand==brand],
        name = f"{brand} Coffee Shops in the Philippines",
        description = f"Scatter plot of {brand} Coffee Shops in the Philippines",
        style = {"fillColor": color_dict[brand],
                "fillOpacity":0.5,
                "opacity":0.5},
    )

# #STEP 4 - INPUT ADDITIONAL DETAILS
app.display(name='title', value='The Battle of Interactive Geographic Visualization Part 6 — Greppo')
app.display(name='description',
            value='A Greppo demo app for vector data using GeoPandas DataFrame')