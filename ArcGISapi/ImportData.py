# 0. Click insert cell below to create a anew code cell below the last call.
    # Log into ArcGIS Online by making a GIS connection to ArcGIS Online using your deceloper account.
        # Replace "username" and "password" with the credentials for your ArcGIS account
from arcgis.gis import GIS

gis = GIS("https://www.arcgis.com", username="xizhewu", password="Wxz041499")



# 1. Make a dict to store the metadata for the Shapefile with the fields title, tags and type
parks_properties = {
    'title': 'Parks and Open Space',
    'tags': 'parks, open data, tutorials',
    'type': 'Shapefile'
}



# 2. load the data as a feature layer with a ContentManager by calling gis.content.add witch returns an Item object
data_file_location = 'DownloadData\LA_Hub_datasets\LA_Hub_Datasets\Parks_and_Open_Space.zip'
parks_shp = gis.content.add(parks_properties, data=data_file_location)

# You can now visualize the Item object 'parks_shp' in rich HTML notation
print(parks_shp)

# 3. Call the publish method of parks_shp to publish the Shapefile, which returns another arcgis.gis.Item instance for the feature layer
parks_feature_layer_item = parks_shp.publish()

# Then visualize the new feature layer
print(parks_feature_layer_item)
# Use the url property of the feature layer object parks_features_layer to get the Service URL.
    # Use this URL to gain access to your feature layer in other tutorials and projects.
print(parks_feature_layer_item.url)