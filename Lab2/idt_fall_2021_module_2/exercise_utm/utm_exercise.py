"""
This code is copied from utm_test.py, and modified by Group 1.
"""
#### Imports ####
from utm import utmconv
from math import pi, cos, acos, radians, sin, asin, sqrt

#### Functions ####
# Great circle formulae: Distance between points
def gcf_distance(lat1, lon1, lat2, lon2):
    distance_radians = 2 * asin(sqrt((sin((lat1 - lat2) / 2))**2 + cos(lat1) * cos(lat2) * (sin((lon1 - lon2) / 2))**2))
    # radius_km = 1.852 * (180 * 60 / pi)
    radius_km = 1
    return radius_km *  distance_radians

#### Program ####
# Geodetic reference coordinate
lat_ref =  55.47
lon_ref = 10.33

print ('Reference position [deg]:')
print ('  latitude:  %.8f'  % (lat_ref))
print ('  longitude: %.8f'  % (lon_ref))

# Instantiate utmconv class
uc = utmconv()

# Convert from geodetic to UTM
(hemisphere, zone, letter, e_ref, n_ref) = uc.geodetic_to_utm (lat_ref,lon_ref)
# print ('\nConverted from geodetic to UTM [m]')
# print ('  %d %c %.5fe %.5fn' % (zone, letter, e_ref, n_ref))


move_distance = 1    # km

# MOVING EAST
# Generating the East UTM coordinate
e2 = e_ref + move_distance * 1000.0 
n2 = n_ref 

# Convert back from UTM to geodetic
(lat_e, lon_e) = uc.utm_to_geodetic (hemisphere, zone, e2, n2)
print ('\nPosition 1000 meter East [deg]:')
print ('  latitude:  %.8f'  % (lat_e))
print ('  longitude: %.8f'  % (lon_e))

d_e = gcf_distance(lat_ref, lon_ref, lat_e, lon_e)
print ('\nMoving East:')
print ('  distance:     %.8f' % (d_e))
print ('  Error in %%:  %.8f' % (100 * (d_e - move_distance) / move_distance))


# MOVING NORTH
# Generating the North UTM coordinate
e3 = e_ref
n3 = n_ref + move_distance * 1000.0

# Convert back from UTM to geodetic
(lat_n, lon_n) = uc.utm_to_geodetic (hemisphere, zone, e3, n3)
print ('\nPosition 1000 meter North [deg]:')
print ('  latitude:  %.8f'  % (lat_n))
print ('  longitude: %.8f'  % (lon_n))

d_n = gcf_distance(lat_ref, lon_ref, lat_n, lon_n)
print ('\nMoving North:')
print ('  distance:     %.8f' % (d_n))
print ('  Error in %%:  %.8f' % (100 * (d_n - move_distance) / move_distance))
