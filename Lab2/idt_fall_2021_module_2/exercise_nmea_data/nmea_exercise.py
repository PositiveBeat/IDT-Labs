import matplotlib.pyplot as plt
import numpy as np

from nmea_read import nmea_class
from exportkml import kmlclass

#### Functions ####

def get_row(array, index):
    time = []
    y = []
    for row in array:
        time.append(float(row[1]))
        y.append(float(row[index]))
    return time, y


#### File import ####

print("Importing files...")
nmea_eduquad = nmea_class()
nmea_eduquad.import_file ('nmea_trimble_gnss_eduquad_flight.txt')
# nmea_static = nmea_class()
# nmea_static.import_file ('nmea_ublox_neo_24h_static.txt')
print("Done!")


#### Program ####

figure, axis = plt.subplots(2, 1)

# Altitude above Mean Sea Level
# This was the hint in the lecture
x, y = get_row(nmea_eduquad.data, 9)
axis[0].plot(x, y, 'green')
axis[0].set_title('Altitude')

# Number of satellites tracked
x, y = get_row(nmea_eduquad.data, 7)
axis[1].plot(x, y, 'red')
axis[1].set_title('Nr. of satellites')

plt.show()

# Map showing the drone track during the drone flight
kml = kmlclass()
kml.begin('drone_track.kml', 'Drone Track', 'Drone track during the drone flight', 0.7)
kml.trksegbegin ('', '', 'red', 'absolute') 
for row in nmea_eduquad.data:
    # Latitude: DDMM.MMMMM to DD.DDDDD format
    degrees_lat = float(row[2][0] + row[2][1])
    minutes_lat = float(row[2][2:])
    lat = degrees_lat + minutes_lat / 60

    # Longitude: DDDMM.MMMMM to DDD.DDDDD format
    degrees_lon = float(row[4][0] + row[4][1] + row[4][2])
    minutes_lon = float(row[4][3:])
    lon = degrees_lon + minutes_lon / 60

    # Add to file
    kml.pt(float(lat), float(lon), 20)

kml.trksegend()
kml.end()

