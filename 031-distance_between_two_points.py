# distance_between_two_points

def distance_between_two_points():
    x1,y1 = str(input("Enter first point => x,y: ")).split(',')
    x2, y2 = str(input("Enter second point => x,y: ")).split(',')
    distance = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5
    return f"Distance Between ({float(x1), float(y1)}) , ({float(x2), float(y2)}): {distance}"

print(distance_between_two_points())

# Write a function that calculates the distance between two points on a 2D plane.
# The function should take the coordinates of two points (x1, y1) and (x2, y2) and compute the Euclidean distance using the standard distance formula.