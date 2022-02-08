from convexHull import convexHull

import matplotlib.pyplot as plt
import random
from time import time
import json
from multiprocessing import Pool


def runTest(gap):
    
    x =  [random.gauss(0,1) for k in range(10000)]
    y =  [random.gauss(0,1) for k in range(10000)]
    points = list(zip(x,y))
    tic = time()
    shape = convexHull(points)
    hull = shape.hull
    return time()-tic, len(shape.outsiders)
    
def testHull():
    
    random.seed(0)

    N = 50
    gaps = [i/N for i in range(N)]
    totals = [[] for i in range(N)]
    removals = [[] for i in range(N)]
    
    for i in range(N):
        gap = gaps[i]
        with Pool(12) as p:
            result = p.map(runTest, [gap for i in range(1000)])
        
        totals[i]   = [r[0] for r in result]
        removals[i] = [r[1] for r in result]
        
        print(gap, ':', sum(totals[i]))
        
    with open('convexhulltimes_normal_normal_10000.txt', 'w+') as outfile:
        outfile.write(json.dumps({'gaps':gaps, 'totals':totals, 'removals':removals}))
    
        
    fig,(ax1,ax2)= plt.subplots(2,1)
    fig.suptitle("Data distributed X: N(0,1) Y: N(0,1)")
    
    ax1.plot(gaps,[sum(t) for t in totals] )
    ax1.set_ylabel('Runtime')
    
    ax2.plot(gaps,[sum(r) for r in removals])
    ax2.set_ylabel('Outside points')
    
    ax2.set_xlabel('Min distance between extrema')

    plt.show()
    

def plotHull(points, outside, hull, extrema):
    fig,ax= plt.subplots()
    
    x, y = zip(*points)
    ax.scatter(x,y,s=0.5, color='#27c')

    outsidex, outsidey = zip(*outside)
    ax.scatter(outsidex,outsidey,s=4, color='green')

    hull += [hull[0]]
    hullx, hully = zip(*hull)
    ax.plot(hullx,hully, color='orange')
    ax.scatter(hullx,hully, color='orange')

    extX, extY = zip(*extrema)
    ax.scatter(extX,extY, color='red')

    plt.show()


if __name__ == '__main__':
    testHull()
    
