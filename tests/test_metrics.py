import geopandas as gpd
import pytest
from shapely.geometry import box
from src.metrics import area,bounds
def test_projected_area_and_bounds():
    g=gpd.GeoDataFrame(geometry=[box(0,0,2,2)],crs="EPSG:3857")
    assert area(g).iloc[0]==4 and bounds(g)==[0,0,2,2]
def test_geographic_area_rejected():
    with pytest.raises(ValueError): area(gpd.GeoDataFrame(geometry=[box(0,0,1,1)],crs="EPSG:4326"))
