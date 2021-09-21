"""
This code is copied from utm_test.py, and modified by Group 1.
"""

from utm import utmconv
from math import pi, cos, acos, radians, sin, asin, sqrt

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
# print ('\nConverted from geodetic to UTM [m]')
# print ('  %d %c %.5fe %.5fn' % (zone, letter, e1, n1))

# now generating the second UTM coordinate
e2 = e1 + 1000.0 
n2 = n1 

# convert back from UTM to geodetic
(lat_e, lon_e) = uc.utm_to_geodetic (hemisphere, zone, e2, n2)
print ('\nSecond position 1000 meter East [deg]:')
print ('  latitude:  %.8f'  % (lat_e))
print ('  longitude: %.8f'  % (lon_e))


# Great circle formulae: Distance between points
def gcf_distance(lat1, lon1, lat2, lon2):
    distance_radians = 2 * asin(sqrt((sin((lat1 - lat2) / 2))**2 + cos(lat1) * cos(lat2) * (sin((lon1 - lon2) / 2))**2))
    radius_km = 1.852 * (180 * 60 / pi)
    return radius_km *  distance_radians

d_e = gcf_distance(lat_ref, lon_ref, lat_e, lon_e)

print ('\nGreat Circle formula:')
print ('  distance:     %.8f' % (d_e))
print ('  Error in %%:  %.8f' % (100 * (d_e - 1) / 1))
