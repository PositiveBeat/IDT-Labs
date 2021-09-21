"""
This code is copied from utm_test.py, and modified by Group 1.
"""

from utm import utmconv
from math import pi, cos

# Geodetic reference coordinate
lat_ref =  55.47
lon_ref = 10.33

print ('Reference position [deg]:')
print ('  latitude:  %.8f'  % (lat_ref))
print ('  longitude: %.8f'  % (lon_ref))

# instantiate utmconv class
uc = utmconv()

# convert from geodetic to UTM
(hemisphere, zone, letter, e1, n1) = uc.geodetic_to_utm (lat_ref,lon_ref)
print ('\nConverted from geodetic to UTM [m]')
print ('  %d %c %.5fe %.5fn' % (zone, letter, e1, n1))

# now generating the second UTM coordinate
e2 = e1 + 100.0 
n2 = n1 

# convert back from UTM to geodetic
(lat2, lon2) = uc.utm_to_geodetic (hemisphere, zone, e2, n2)
print ('\nSecond position 100 meter East [deg]:')
print ('  latitude:  %.8f'  % (lat2))
print ('  longitude: %.8f'  % (lon2))


