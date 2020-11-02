import csv
from sys import argv, exit
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

if len(argv) != 3:
    print("Usage: python weight_graph.py weight_data.csv name")
    exit(1)

with open(argv[1], "r", newline='') as file:
    reader = csv.DictReader(file)
    name = argv[2].lower()

    # Check if the given name is available in the csv file
    if name not in reader.fieldnames:
        print("{} is not in the csv file.".format(name))
        file.close()
        exit(1)

    dates = list()
    y_data = list()
    for row in reader:
        if(row[name] != 'null'):
            dates.append(row['date'])
            y_data.append(float(row[name]))

    # Print dates and corresponding kgs
    for date, kg in zip(dates, y_data):
        print("{}\t{:5g}".format(date, kg))
    print("Number of measurements: {}".format(len(y_data)))

    # Convert dates string into datetime date
    x_data = [datetime.strptime(d, "%d/%m/%Y").date() for d in dates]
    ax = plt.gca()

    # Format the xaxis to show wanted values
    formatter = matplotlib.dates.DateFormatter("%Y - %m - %d")
    ax.xaxis.set_major_formatter(formatter)

    plt.title("{}'s Weight Graph".format(name.capitalize()))
    plt.xlabel("dates (%Y-%m-%d)")
    plt.ylabel("weight")

    plt.plot(x_data, y_data)
    plt.show()
