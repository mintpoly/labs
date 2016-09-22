import math
import pylab
from matplotlib import mlab

amin = -20.0
amax = 20.0

da = 0.05
alist = mlab.frange (amin, amax, da)

pylab.ion()
t = 0
for a in range (50):
        ylist = [math.cos(2*a) for a in alist]
        xlist = [math.sin(t+a) for a in alist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()
        t = t + 1
pylab.pause(0.5)


pylab.close()