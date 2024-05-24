import csv
import math

def read_traverse_data(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header if present
            traverse_data = []
            for row in csv_reader:
                if len(row) != 3:
                    print("Error: Invalid data format in the CSV file.")
                    return None
                try:
                    point_number = int(row[0])
                    easting = float(row[1])
                    northing = float(row[2])
                    traverse_data.append((point_number, easting, northing))
                except ValueError:
                    print("Error: Invalid data format in the CSV file.")
                    return None
        return traverse_data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def calculate_traverse_characteristics(traverse_data):
    if not traverse_data:
        return None

    num_points = len(traverse_data)
    eastings = [point[1] for point in traverse_data]
    northings = [point[2] for point in traverse_data]
    min_easting = min(eastings)
    max_easting = max(eastings)
    min_northing = min(northings)
    max_northing = max(northings)

    return {
        "num_points": num_points,
        "min_easting": min_easting,
        "max_easting": max_easting,
        "min_northing": min_northing,
        "max_northing": max_northing
    }

def calculate_distance(point1, point2):
    dx = point2[1] - point1[1]
    dy = point2[2] - point1[2]
    return math.sqrt(dx**2 + dy**2)

def calculate_bearing(point1, point2):
    dx = point2[1] - point1[1]
    dy = point2[2] - point1[2]
    bearing = math.atan2(dy, dx)
    return math.degrees(bearing)

# Example usage:
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)
if traverse_data:
    traverse_characteristics = calculate_traverse_characteristics(traverse_data)
    if traverse_characteristics:
        print("Traverse Characteristics:")
        for key, value in traverse_characteristics.items():
            print(f"{key}: {value}")

        # Example distance and bearing calculation between point 1 and point 2
        point1 = traverse_data[0]
        point2 = traverse_data[1]
        distance = calculate_distance(point1, point2)
        bearing = calculate_bearing(point1, point2)
        print(f"Distance between point 1 and point 2: {distance}")
        print(f"Bearing from point 1 to point 2: {bearing} degrees")
