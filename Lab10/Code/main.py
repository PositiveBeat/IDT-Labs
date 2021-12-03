import matplotlib.pyplot as plt

from CSVfile import CSVfile
from exportkml import kmlclass
from exportplan import planclass
from outliers_begone import outliers_begone
from simplify_path import simplify
from utm import utmconv


print_files = True


track = CSVfile()
track.loadCSV('../logs/data_103923')



#### CREATE KML FILE ####
if print_files == True:
    kml = kmlclass()
    kml.begin('generated_files/drone_track.kml', 'Drone Track', 'Drone track during the drone flight', 0.7)
    kml.trksegbegin ('', '', 'red', 'absolute') 
    for i in range(len(track.t)):
        kml.pt(float(track.lat[i]), float(track.lon[i]), 40)
    kml.trksegend()
    kml.end()



#### CONVERT TO UTM ####
uc = utmconv()  # Instantiate utmconv class
utm = []

for i in range(len(track.t)):
    (hemisphere, zone, letter, easting, northing) = uc.geodetic_to_utm (track.lat[i], track.lon[i])
    utm.append([track.t[i], easting, northing])



#### REMOVE OUTLIERS ####
purged = outliers_begone()
utm = purged.purge(utm)



#### SIMPLIFY PATH ####
simple = simplify()
# utm = simple.simplify_maxDistance()



#### CONVERT TO GEODETIC ####
geodetic = []
for t, easting, northing in utm:
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
