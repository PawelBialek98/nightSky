#from matplotlib import pylab
from pylab import *
from random import randrange


def star(R, x, y, color='w', N = 5, thin =0.5):
    polystar = zeros((2*N,2))
    for i in range(2*N):
        angle = i*pi/N
        r = R*(1-thin*(i%2))
        polystar[i] = [r*cos(angle)+x, r*sin(angle)+y]
    return Polygon(polystar, fc=color, ec=color)

imgSize = 800
numberOfStars = 40

minPoints = 5
maxPoints = 11
minRadius = 6
maxRadius = 20
minThin = 5
maxThin = 9

figure(facecolor='k')
curAxes = gca()

for i in range(numberOfStars):
    newStar = star(randrange(minRadius,maxRadius),
                   randrange(0,imgSize),
                   randrange(0,imgSize),
                   'w',
                   randrange(minPoints, maxPoints),
                   randrange(minThin,maxThin)/10.0)
    curAxes.add_patch(newStar)

axis([0, imgSize, 0, imgSize])
axis('scaled')
axis('off')
savefig('sky', facecolor = 'k', edgecolor = 'k')