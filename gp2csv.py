import pandas as pd
import pynmea2
from pyproj import Proj


filename = 'line2.gp2'
outname = 'line2.txt'

dat = pd.read_csv(filename, header=5)

gps = dat.GPS.apply(pynmea2.parse)

lat = gps.apply(lambda mes: mes.latitude)
lon = gps.apply(lambda mes: mes.longitude) 
elev = gps.apply(lambda mes: mes.altitude)

myProj = Proj("+proj=utm +zone=16 +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

east,north = myProj(lon,lat)

out = pd.DataFrame({'easting': east, 'northing': north, 'elevation': elev})
print(out)
out.to_csv(outname,index=False)


#import matplotlib.pyplot as plt
#plt.plot(east,north,'.')
#plt.show()

