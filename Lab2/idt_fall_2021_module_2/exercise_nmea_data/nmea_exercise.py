import matplotlib.pyplot as plt
import numpy as np

from nmea_read import nmea_class


print("Importing files...")
nmea_eduquad = nmea_class()
nmea_eduquad.import_file ('nmea_trimble_gnss_eduquad_flight.txt')
# nmea_static = nmea_class()
# nmea_static.import_file ('nmea_ublox_neo_24h_static.txt')
print("Done!")



x = []
for row in nmea_eduquad.data:
    # x.append(row[1])
    print(row[1])

print(x)
# Altitude above Mean Sea Level
# plt.plot(nmea_eduquad.data[:,1])
# plt.show()

# print(nmea_eduquad.data[0][0])




