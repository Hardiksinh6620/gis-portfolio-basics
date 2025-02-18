import geopandas as gpd
import pytest
from shapely.geometry import Point
from src.crs_utils import reproject,describe_crs
def test_reproject_and_describe():
    g=gpd.GeoDataFrame(geometry=[Point(0,0)],crs="EPSG:4326"); out=reproject(g,"EPSG:3857")
    assert out.crs.to_epsg()==3857 and describe_crs(g)["epsg"]==4326
def test_missing_crs():
    with pytest.raises(ValueError): reproject(gpd.GeoDataFrame(geometry=[Point(0,0)]),"EPSG:3857")
