"""Vector I/O helpers."""
from pathlib import Path
import geopandas as gpd

def read_vector(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    return gpd.read_file(path)

def write_vector(gdf, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(path)
