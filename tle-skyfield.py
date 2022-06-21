# tle-skyfield.py
from skyfield.api import load, wgs84
import json

stations_url = 'ALL-SAT-TLE.txt'
# stations_url = 'http://celestrak.com/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
# stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

# timescale

from skyfield.api import EarthSatellite
ts = load.timescale()

# select satellite
satellite_name = "IRIDIUM 108"
by_name = {sat.name: sat for sat in satellites}
satellite = by_name[satellite_name]
print(satellite)

# You can instead use ts.now() for the current time
t = ts.utc(2022, 6, 15, 11, 18, 7)

geocentric = satellite.at(t)
print(geocentric.position.km)

lat, lon = wgs84.latlon_of(geocentric)
print('Latitude:', lat)
print('Longitude:', lon)

data = {'satellite name': satellite_name, 'Latitude': str(lat), 'Longitude': str(lon)}
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)

obj = json.dumps(data, indent=4)
print(obj)
