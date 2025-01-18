"""Geometry metrics requiring a projected CRS where units matter."""
def _projected(gdf):
    if gdf.crs is None or not gdf.crs.is_projected: raise ValueError("A projected CRS is required")
def area(gdf): _projected(gdf); return gdf.geometry.area
def length(gdf): _projected(gdf); return gdf.geometry.length
def centroid(gdf): return gdf.geometry.centroid
def bounds(gdf): return gdf.total_bounds.tolist()
