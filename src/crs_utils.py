"""CRS transformation helpers."""
def reproject(gdf, target_crs):
    if gdf.crs is None:
        raise ValueError("Source GeoDataFrame has no CRS set.")
    return gdf.to_crs(target_crs)

def describe_crs(gdf):
    if gdf.crs is None:
        return {"crs": None}
    return {"crs": gdf.crs.to_string(),
            "epsg": gdf.crs.to_epsg(),
            "units": gdf.crs.axis_info[0].unit_name if gdf.crs.axis_info else None}
