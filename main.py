import pyrosm

# Get filepath to test PBF dataset
print("Filepath to test data:", "russia-latest.osm.pbf")

# Initialize the OSM object
osm = pyrosm.OSM("russia-latest.osm.pbf")

# See the type
print("Type of 'osm' instance: ", type(osm))