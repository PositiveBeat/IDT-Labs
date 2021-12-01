from CSVfile import CSVfile
from exportkml import kmlclass
from exportplan import planclass
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
    utm.append([easting, northing])




#### CREATE PLAN ####
if print_files == True:
    altitude = 50
    home = [track.lat[0], track.lon[0], altitude]

    plan = planclass('generated_files/mission.plan')
    plan.begin('QGroundControl')
    plan.record_plan(track.lat, track.lon, altitude)
    plan.end(home)

