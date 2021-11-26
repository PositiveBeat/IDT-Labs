'''
Plotting csv files.

Author: Nicoline Louise Thomsen
'''

import csv
from exportkml import kmlclass
import matplotlib.pyplot as plt

lat = []
lon = []

def plotCSV_d(filename):
    
    with open(filename + '.csv','r') as csvfileQuick:
        plots = csv.reader(csvfileQuick, delimiter=',')
        next(plots)
        for row in plots:
            lat.append(float(row[0]))
            lon.append(float(row[1]))

    plt.plot(lat, lon, label = 'Position')
    plt.xlabel('Lattitude')
    plt.ylabel('Longitude')
    plt.title('GNSS Position')
    plt.legend()
    plt.axis('equal')
    
    plt.show()



if __name__ == '__main__':
    plotCSV_d('logs/data_085254')
    
    # Map showing the drone track during the drone flight
    kml = kmlclass()
    kml.begin('drone_track.kml', 'Drone Track', 'Drone track during the drone flight', 0.7)
    kml.trksegbegin ('', '', 'red', 'absolute') 
    
    for i in range(len(lat)):

        la = lat[i]
        lo = lon[i]

        # Add to file
        kml.pt(float(la), float(lo), 40)

    kml.trksegend()
    kml.end()
