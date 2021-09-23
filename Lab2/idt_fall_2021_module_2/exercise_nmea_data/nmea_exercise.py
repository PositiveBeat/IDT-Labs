import matplotlib.pyplot as plt
import numpy as np

from nmea_read import nmea_class

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
# WHAT INDEX IS THIS? D:
x, y = get_row(nmea_eduquad.data, 9)
axis[0].plot(x, y, 'green')
axis[0].set_title('Altitude')

# Number of satellites tracked
x, y = get_row(nmea_eduquad.data, 7)
axis[1].plot(x, y, 'red')
axis[1].set_title('Nr. of satellites')


plt.show()