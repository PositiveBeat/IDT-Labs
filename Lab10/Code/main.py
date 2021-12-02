import matplotlib.pyplot as plt

from CSVfile import CSVfile
from exportkml import kmlclass
from exportplan import planclass
from rm_outliers import outliers_begone
from utm import utmconv


print_files = False


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



# print(len(utm))
purged = outliers_begone()
utm = purged.purge(utm)
# print(len(utm))








# print(track.lat, track.lon)


#### CONVERT TO GEODETIC ####
geodetic = []
for t, easting, northing in utm:
    lat, lon = uc.utm_to_geodetic (hemisphere, zone, easting, northing)
    geodetic.append([lat, lon])
    

print(len(geodetic))

plt.plot(geodetic[0], geodetic[1], label = 'Position')
plt.xlabel('Lattitude')
plt.ylabel('Longitude')
plt.title('GNSS Position')
plt.legend()
plt.axis('equal')
plt.show()



#### CREATE PLAN ####
if print_files == True:
    altitude = 50
    home = geodetic[0] + [altitude]

    plan = planclass('generated_files/mission.plan')
    plan.begin('QGroundControl')
    plan.record_plan(geodetic, altitude)
    plan.end(home)

