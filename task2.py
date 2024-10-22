from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

import matplotlib.pyplot as plt


def close_gaps(polygons):
    closed_polygons = []
    for polygon in polygons:
        # Automatically extend the polygon to form a complete rectangle
        minx, miny, maxx, maxy = polygon.bounds
        closed_polygons.append(Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)]))
    return closed_polygons


polygon1 = Polygon([(0,0), (2,0), (2,2), (0,2)])
polygon2 = Polygon([(2,0), (4,0), (4,2), (2,2)])
polygons = [polygon1, polygon2]


closed_polygons = close_gaps(polygons)
multi_polygon = unary_union(closed_polygons)

print("Total Area:", multi_polygon.area)

fig, ax = plt.subplots()
for poly in closed_polygons:
    x, y = poly.exterior.xy
    ax.fill(x, y, alpha=0.5)
plt.show()
