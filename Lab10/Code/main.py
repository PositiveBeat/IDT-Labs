from CSVfile import CSVfile
from exportkml import kmlclass
from exportplan import planclass


track = CSVfile()
track.loadCSV('../logs/data_103923')


# Create KML file
kml = kmlclass()
kml.begin('drone_track.kml', 'Drone Track', 'Drone track during the drone flight', 0.7)
kml.trksegbegin ('', '', 'red', 'absolute') 
for i in range(len(track.lat)):
    kml.pt(float(track.lat[i]), float(track.lon[i]), 40)
kml.trksegend()
kml.end()


# Create PLAN
plan = planclass('mission.plan')
plan.begin('QGroundControl')
plan.record_plan(track.lat, track.lon, 50)
plan.end([track.lat[0], track.lon[0], 50])

