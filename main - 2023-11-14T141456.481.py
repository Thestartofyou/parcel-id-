import geopandas as gpd
import folium

# Load Boston streets shapefile (replace 'path/to/boston_streets.shp' with your actual file path)
streets_path = 'path/to/boston_streets.shp'
streets_gdf = gpd.read_file(streets_path)

# Load parcel data (replace 'path/to/parcel_data.shp' with your actual file path)
parcel_path = 'path/to/parcel_data.shp'
parcel_gdf = gpd.read_file(parcel_path)

# Merge streets and parcel data based on common attributes, adjust as needed
merged_gdf = gpd.merge(streets_gdf, parcel_gdf, how='left', on='common_attribute')

# Create a base map centered around Boston
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Add GeoJSON data to the map
folium.GeoJson(merged_gdf.to_json(), name='geojson').add_to(m)

# Add popup information for each feature
for idx, row in merged_gdf.iterrows():
    popup_text = f"Parcel ID: {row['Parcel_ID']}<br>Other Info: {row['Other_Info']}"
    folium.Marker(location=[row['geometry'].y, row['geometry'].x], popup=popup_text).add_to(m)

# Save the map as an HTML file
m.save('boston_map_with_parcels.html')
