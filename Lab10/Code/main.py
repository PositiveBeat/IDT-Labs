import matplotlib.pyplot as plt
import numpy as np

from CSVfile import CSVfile
from exportkml import kmlclass
from exportplan import planclass
from outliers_begone import outliers_begone
from Simplifier import simplify
from utm import utmconv


print_files = True

track = CSVfile()
# track.loadCSV('../logs/data_103923')
track.loadCSV('data_outlier')



#### CONVERT TO UTM ####
uc = utmconv()  # Instantiate utmconv class
utm = []

for i in range(len(track.time)):
    (hemisphere, zone, letter, easting, northing) = uc.geodetic_to_utm (track.lat[i], track.lon[i])
    utm.append([easting, northing])

print("number og points in path:        ", len(utm))



#### REMOVE OUTLIERS #### 
purged = outliers_begone()
utm = purged.purge(track.time, utm)
print("points after removing outliers:  ", len(utm))



#### SIMPLIFY PATH ####
# simple = simplify()
# epsilon = 10
# utm = simple.rdp(np.array(utm), epsilon)
# print("points after simplifying:        ", len(utm))



#### CONVERT TO GEODETIC ####
geodetic = []
for easting, northing in utm:
    lat, lon = uc.utm_to_geodetic (hemisphere, zone, easting, northing)
    geodetic.append([lat, lon])



#### CREATE PLAN ####
if print_files == True:
    altitude = 50
    home = geodetic[-1] + [altitude]

    plan = planclass('generated_files/mission.plan')
    plan.begin('QGroundControl', home)
    plan.record_plan(geodetic, altitude)
    plan.end()



#### CREATE KML FILE ####
if print_files == True:
    kml = kmlclass()
    kml.begin('generated_files/drone_track_filter.kml', 'Filtered Drone Track', 'Drone track during the drone flight with applied filters.', 0.7)
    kml.trksegbegin ('', '', 'red', 'absolute') 
    for i in range(len(geodetic)):
        kml.pt(float(geodetic[i][0]), float(geodetic[i][1]), 40)
    kml.trksegend()
    kml.end()

