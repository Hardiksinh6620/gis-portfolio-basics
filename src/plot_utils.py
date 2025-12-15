"""Static map plotting helpers."""
from pathlib import Path
import matplotlib.pyplot as plt
import contextily as cx

def plot_layer(gdf, out_path, title="Layer", use_basemap=True):
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, alpha=0.6, edgecolor="k")
    if use_basemap and gdf.crs and gdf.crs.to_epsg() == 3857:
        cx.add_basemap(ax, source=cx.providers.OpenStreetMap.Mapnik)
    ax.set_title(title)
    ax.set_axis_off()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
