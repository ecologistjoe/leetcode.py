
import math

class convexHull:
    points = []
    spacing = 0.4
    
    extrema = []
    hull = []
    outsiders = []
    
    def __init__(self, points=[], spacing=0.4):
        self.points = points
        self.spacing = spacing
        if points:
            self.hull = self.findConvexHull()

    def extremePoints(self, spacing=None):
        if spacing != None:
            self.spacing = spacing
        
        # Identifies 8 'extreme' points -- think of them as the northern-most
        # northeastern-most, eastern-most etc. They define a polygon* with up to
        # 8 sides / vertices
        # *(or a line in really degenerate cases, but think of it as a polygon for now)
        MIN, MAX = -2**31, 2**31
        
        minX, minY, minS, minD = (MAX, MAX, MAX, MAX)
        maxX, maxY, maxS, maxD = (MIN, MIN, MIN, MIN)
        
        # Scan through points to identify 4 extrema. Some points may be the same.
        # The numbering ensures that when we add the 'corners', the resulting
        # a list of points will define a polygon in anti-clockwise order.
        P = [[None,None] for i in range(8)]
        for p in self.points:
            x,y = p
            if x   < minX: minX, P[0] = x, p
            if y   < minY: minY, P[2] = y, p
            if x   > maxX: maxX, P[4] = x, p
            if y   > maxY: maxY, P[6] = y, p
        
        # Identify the corner points
        # These rely on knowing the mins and maxes in order to do normalization
        r = (maxX-minX) / (maxY-minY)
        for p in self.points:
            x,y = p
            S = x+y*r
            D = r*y-x
            if S < minS: minS, P[1] = S, p
            if D < minD: minD, P[3] = D, p
            if S > maxS: maxS, P[5] = S, p
            if D > maxD: maxD, P[7] = D, p
               
        # Collect into a list of unique vertices that are separated by at
        # minimum 'gap'% of either the X or Y extent.
        # For moderate 'gap', this reduces run time by removing comparisons
        # against close together points
        extrema=[P[0]]
        for i in range(1,8):
            if abs(P[i][0]-extrema[-1][0]) > self.spacing*(maxX-minX) or abs(P[i][1]-extrema[-1][1]) > self.spacing*(maxY-minY):
              extrema += [P[i]]
        
        self.extrema = extrema
        return extrema
        
        
    def findConvexHull(self, points=None, spacing=None):
        if points != None:
            self.points = points
        if spacing != None:
            self.spacing = spacing
        
        #Get vertices of an up-to-8-sided polygon where the vertices
        # are extrema from the pointcloud
        extrema = self.extremePoints()
        N = len(extrema)

        # 1. Loop through all of the points. We'll check and see if they are
        #  outside of the polygon defined by extrema. In most datasets,
        #  only about sqrt(N) of the points will be outside of the polygon
        #  We'll just ignore anything inside the polygon as they can't be on the hull.
        # Additionally, each point can only be 'outside' of exactly one side of the polygon
        #  We'll collect those points that can contribute to the hull ouside of 
        #  each side into its own candidates to deal with in the next step.
        #  The equation determines what side of the line defined by the consecutive
        #  vertices any given point is. Since we're traversing the vertices strictly
        #  counter-clockwise, we only want to keep ones on the 'right'
        # Almost all of the work is done in this loop. It's timing is O(N*m)
        #  Having *fewer* sides to the octogon can speed things up when the
        #  the side is short (i.e. the points are close together).
        
        candidates = [[] for j in range(N)]
        for j in range(N):
            x1,y1 = extrema[j]
            deltaX = extrema[j-1][0] - x1
            deltaY = extrema[j-1][1] - y1
            candidates[j] = [[pX,pY]
                for pX,pY in self.points
                if deltaX*(pY-y1) > deltaY*(pX-x1)
                ]
                
        self.outsiders =[p for B in candidates for p in B]

        # Aside: You'll be tempted to apply the above steps to each candidates.
        # The speed improvement is minimal, only about 2% at best.
        # Even for largest candidatess, most of the points get cleared out in the
        # first couple of passes while comparing to random points, so even though
        # it looks like it's N'**2, it's really closer to NlogN


        # Treat each side independently to discover the points on the hull
        # in between the points defined by extrema[j-1] and extrema[j]
        hull = []
        for j in range(N):
            
            # All extrema are part of the hull. Add it in order.
            hull += [extrema[j-1]]
            
            # Special cases
            if len(candidates[j]) == 0:
                continue
            if len(candidates[j]) == 1:
                hull += candidates[j]
                continue
            
            # 2. Winnow the candidates further by removing points that
            # are interior to the triangle made with two adjacent extrema
            # and any other outside point
            x1,y1 = extrema[j-1]
            x3,y3 = extrema[j]
            candidatescopy = candidates[j]
            for x2,y2 in candidatescopy:
                if [x2,y2] not in candidates[j]: continue
                candidates[j] = [[pX,pY]
                    for pX,pY in candidates[j]
                    if (x2==pX and y2==pY) or (x3==pX and y3==pY) or 
                        (((x2-x1)*(pY-y1) < (y2-y1)*(pX-x1)) or
                         ((x3-x2)*(pY-y2) < (y3-y2)*(pX-x2)))
                    ]
                    
            # 3. Order the remaining candidates by rotational angle
            # By this point, there are typically very few points remaining
            angles = []
            x2,y1 = extrema[j-1]
            x3,y3 = extrema[j]
            basis = math.atan2((y3-y1),(x3-x1))
            for pX,pY in candidates[j]:
                angles += [(math.atan2((pY-y3),(pX-x3))-basis) % 6.2831852]
            
            candidates[j] = [p for a,p in sorted(zip(angles, candidates[j]), key=lambda pair: pair[0])]
            
            # Add the node with the min angle from extrema[j-1] to the hull.
            hull += [candidates[j][0]]
            
            #4. Search the sorted list for nodes that have the shallowest
            # angle from the line made from the previous two points on the hull
            # Then search the remaining candidates that are ahead of the current node
            # for the one with the shallowest angle, and add it to the hull. Repeat.
            currentNodeId=0
            minAngle = 0;
            candidates[j] += [extrema[j]]
            while currentNodeId < len(candidates[j])-1:
                x2,y2 = hull[-2]
                x1,y1 = hull[-1]
                basis = math.atan2((y1-y2),(x1-x2))
                minAngle = float('inf')
                nextNodeId = None
                for k in range(currentNodeId+1, len(candidates[j])):
                    pX, pY = candidates[j][k]
                    angle= (math.atan2((pY-y1),(pX-x1)) - basis) % 6.2831852
                    if angle < minAngle:
                        minAngle = angle
                        nextNodeId = k
                hull += [candidates[j][nextNodeId]]
                currentNodeId = nextNodeId
        
        self.hull = hull
        return hull
                    

