# GIS Portfolio Basics

Foundational GIS operations in Python: vector I/O, CRS transforms, static maps.

## Install
```bash
pip install -r requirements.txt
```

## Usage
```python
from src.io_utils import read_vector, write_vector
from src.crs_utils import reproject
from src.plot_utils import plot_layer

gdf = read_vector("data/sample.geojson")
gdf_utm = reproject(gdf, "EPSG:32633")
plot_layer(gdf_utm, "output.png")
```

## Test
```bash
pytest -v
```

## Provenance

See [HISTORY.md](HISTORY.md) for collaboration and reconstruction details.
