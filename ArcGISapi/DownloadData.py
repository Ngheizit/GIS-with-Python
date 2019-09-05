# 0. import the GIS class to create a connection to ArcGIS Online
from arcgis.gis import GIS
# Pyhton Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

print("Library Modules have been imported")

# 1. Store the ID of the public data item we want to download
public_data_item_id = 'a04933c045714492bda6886f355416f2'

# 2. Beacause the data is public, we can use an anonymous connection to ArcGIS Online to download the data
anon_gis = GIS()


# 3. The content property for gis is an instance of a ContentManager that is used to manage content on ArcGIS Online
    # ↓Below, get() makes an ArcGIS REST API request to retrieve an Item object data_item
data_item = anon_gis.content.get(public_data_item_id)
print("data_item is {}".format(data_item))
# 'ContentManager.get' will return 'None' if there is no Item with ID for public_data_item_id

# 4. Download
data_path = Path("./DownloadData")
print("data_path is {}".format(data_path))
if not data_path.exists():
    data_path.mkdir()
data_item.download(save_path=data_path)

# 5. Extract the zip file
zip_path = data_path.joinpath('LAHubDatasets.zip')
extract_path = data_path.joinpath('LA_Hub_datasets')
zip_file = ZipFile(zip_path)
zip_file.extractall(path=extract_path)

