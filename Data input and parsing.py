import csv

def read_traverse_data(file_path):
    traverse_points = []

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                try:
                    point_number = int(row[0].strip())
                    easting = float(row[1].strip())
                    northing = float(row[2].strip())

                    traverse_points.append((point_number, easting, northing))
                except (ValueError, IndexError):
                    print(f"Error: Invalid data format in row {csv_reader.line_num}. Skipping the row.")
    except FileNotFoundError:
        print("Error: File not found.")

    return traverse_points

# Example usage
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)
print(traverse_data)
