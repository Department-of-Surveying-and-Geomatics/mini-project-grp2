
import csv
import math
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

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

def calculate_distance(point1, point2):
    dx = point2[1] - point1[1]
    dy = point2[2] - point1[2]
    distance = math.sqrt(dx**2 + dy**2)

    return distance

def calculate_bearing(point1, point2):
    dx = point2[1] - point1[1]
    dy = point2[2] - point1[2]
    angle_radians = math.atan2(dy, dx)
    bearing_degrees = math.degrees(angle_radians)
    if bearing_degrees < 0:
        bearing_degrees += 360

    return bearing_degrees

def plot_traverse(traverse_data):
    point_numbers = [point[0] for point in traverse_data]
    eastings = [point[1] for point in traverse_data]
    northings = [point[2] for point in traverse_data]

    plt.scatter(eastings, northings, marker='o', color='blue')

    for i in range(len(traverse_data)):
        plt.annotate(point_numbers[i], (eastings[i], northings[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.xlabel('Easting')
    plt.ylabel('Northing')
    plt.title('Traverse Visualization')
    plt.grid(True)
    plt.show()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        traverse_data = read_traverse_data(file_path)
        plot_traverse(traverse_data)

def calculate_and_display_results(point1, point2):
    distance = calculate_distance(point1, point2)
    bearing = calculate_bearing(point1, point2)

    result_label.config(text=f"Distance: {distance:.2f}, Bearing: {bearing:.2f} degrees")

# Create the main window
window = tk.Tk()
window.title("Traverse Analysis")
window.geometry("400x200")

# Create the file selection button
file_button = tk.Button(window, text="Select File", command=browse_file)
file_button.pack(pady=20)

# Create the point selection widgets
point1_label = tk.Label(window, text="Point 1:")
point1_label.pack()
point1_entry = tk.Entry(window)
point1_entry.pack()

point2_label = tk.Label(window, text="Point 2:")
point2_label.pack()
point2_entry = tk.Entry(window)
point2_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=lambda: calculate_and_display_results(
    eval(point1_entry.get()), eval(point2_entry.get())))
calculate_button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop() 
