from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt


# Define the lines (rectangles) based on coordinates from the question 1.
lines = [
    LineString([(0, 1), (7, 1)]),  
    LineString([(0, 0), (1, 0)]),  
    LineString([(1, 0), (6, 0)]),  
    LineString([(1, -3), (6, -3)]),
    LineString([(0, -4), (1, -4)]),
    LineString([(1, -4), (5, -4)]),
    LineString([(3, -6), (5, -6)]),
    LineString([(3, -7), (5, -7)]) 
]


rectangles = [
    {"coords": [(0, 0), (1, 0), (1, -3), (0, -3)], "length": 1, "width": 3},  # Rectangle 1
    {"coords": [(1, 0), (6, 0), (6, -3), (1, -3)], "length": 5, "width": 3},  # Rectangle 2
    {"coords": [(0, -4), (1, -4), (1, -7), (0, -7)], "length": 1, "width": 3},  # Rectangle 3
    {"coords": [(3, -6), (5, -6), (5, -7), (3, -7)], "length": 2, "width": 1}   # Rectangle 4
]


def create_polygon(coords):
    return Polygon(coords)


def calculate_distance(poly1, poly2):
    return poly1.distance(poly2)


polygon_objects = [create_polygon(rect["coords"]) for rect in rectangles]


print(f"Number of rectangles: {len(polygon_objects)}")


for i in range(len(polygon_objects) - 1):
    poly1 = polygon_objects[i]
    poly2 = polygon_objects[i + 1]
    distance = calculate_distance(poly1, poly2)
    print(f"Distance between Rectangle {i + 1} and Rectangle {i + 2}: {distance:.2f} units")


def draw_rectangles(polygons):
    fig, ax = plt.subplots()
    for poly in polygons:
        x, y = poly.exterior.xy
        ax.plot(x, y, color='blue')
        ax.fill(x, y, alpha=0.5, color='lightblue')

    ax.set_aspect('equal', 'box')
    plt.grid(True)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Rectangles Visualization")
    plt.show()


draw_rectangles(polygon_objects)


for i, rect in enumerate(rectangles, start=1):
    print(f"Rectangle {i}: Coordinates: {rect['coords']}, Length: {rect['length']}, Width: {rect['width']}")
