import geopandas as gpd
from shapely.geometry import Point
import pytest
from src.io_utils import read_vector, write_vector

@pytest.fixture
def sample_gdf():
    return gpd.GeoDataFrame({"name": ["a", "b"]},
                            geometry=[Point(0, 0), Point(1, 1)],
                            crs="EPSG:4326")

def test_write_then_read_geojson(tmp_path, sample_gdf):
    p = tmp_path / "out.geojson"
    write_vector(sample_gdf, p)
    back = read_vector(p)
    assert len(back) == 2
    assert back.crs.to_epsg() == 4326

def test_read_missing_file():
    with pytest.raises(FileNotFoundError):
        read_vector("nope.geojson")
