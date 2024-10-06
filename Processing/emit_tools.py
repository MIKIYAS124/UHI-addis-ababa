from flask import Flask, jsonify, request
import geopandas as gpd
import numpy as np
import rasterio
from rasterstats import zonal_stats

app = Flask(__name__)

def load_geojson(filepath):
    """Load GeoJSON data."""
    try:
        return gpd.read_file(filepath)
    except Exception as e:
        return {"error": str(e)}

def calculate_ndvi(nir, red):
    """Calculate NDVI from NIR and Red bands."""
    return (nir - red) / (nir + red)

@app.route('/process_uhi', methods=['POST'])
def process_uhi():
    # Example of receiving file paths
    uhi_geojson_path = request.json['uhi_geojson_path']
    
    # Load UHI data
    uhi_data = load_geojson(uhi_geojson_path)
    
    # Further processing logic (NDVI or Zonal stats)...
    if 'error' in uhi_data:
        return jsonify(uhi_data)
    
    bounds = uhi_data.total_bounds  # Bounding box as [minx, miny, maxx, maxy]
    
    return jsonify({"bounds": bounds.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
