from shapely.geometry import Point,box
from src.predicates import contains,intersects,within,touches
def test_predicates():
    polygon=box(0,0,2,2); point=Point(1,1)
    assert contains(polygon,point) and within(point,polygon) and intersects(polygon,point)
    assert touches(polygon,Point(0,1))
