import csv
import matplotlib.pyplot as plt

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

# Example usage:
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)
if traverse_data:
    # Extract coordinates and point numbers
    point_numbers = [point[0] for point in traverse_data]
    eastings = [point[1] for point in traverse_data]
    northings = [point[2] for point in traverse_data]

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(eastings, northings, marker='o', color='red')

    # Annotate points with their corresponding point numbers
    for i, txt in enumerate(point_numbers):
        plt.annotate(txt, (eastings[i], northings[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title('Traverse Visualization')
    plt.xlabel('Easting')
    plt.ylabel('Northing')
    plt.grid(True)
    plt.show()
