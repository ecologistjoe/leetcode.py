# This is classified as 'easy', but it's a pretty complicated and interesting problem
# The problem spec says there will only ever be 50 items in the list, so perhaps
# the naive O(n^3) solution is what was expected

# Area of a Triangle: 1/2*(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 -y3*x1)

class Solution:

    # The brute-force search O(n^3) solution
    def largestTriangleAreaO3(self, points):
        N = len(points)
        maxA = -2**31
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i,N):
                x2,y2 = points[j]
                for k in range(j, N):
                    x3,y3 = points[k]
                    A = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
                    if A > maxA:
                        maxA = A
                        #maxAreaPoints = [points[i], points[j], points[k]]
        return maxA
        
        
    # For a very large list, this will become unwieldy.
    # We can pare the list down by recognizing that the points that participate
    # in the largest triangle will always be on the convex hull of the point cloud
    # If there's an efficient way to identify those points, we can send
    # a smaller list to the O3 implementation
    
    
    # This identifies 8 'extreme' points -- think of them as the northern-most
    # northeastern-most, eastern-most etc. They define a polygon* with up to
    # 8 sides / vertices
    # *(or a line, but think of it as a polygon for now)
    def extremePoints(self, points):
        MIN, MAX = -2**31, 2**31
        
        minX, minY, minS, minD = (MAX, MAX, MAX, MAX)
        maxX, maxY, maxS, maxD = (MIN, MIN, MIN, MIN)
        
        # Scan through points to identify 8 extrema
        # Some points may be the same. That's ok
        # Build a polygon with points in anti-clockwise order, starting with
        # the left-most point. The start is arbitrary, but the order is important
        P = [[0,0] for i in range(8)]
        for p in points:
            x,y = p
            if x   < minX: minX, P[0] = x, p
            if x+y < minS: minS, P[1] = x+y, p
            if y   < minY: minY, P[2] = y, p
            if y-x < minD: minD, P[3] = y-x, p
            if x   > maxX: maxX, P[4] = x, p
            if x+y > maxS: maxS, P[5] = x+y, p
            if y   > maxY: maxY, P[6] = y, p
            if y-x > maxD: maxD, P[7] = y-x, p
        
        extrema = []
        for i in range(0,8):
            if P[i] not in extrema:
                extrema += [P[i]]
        
        return extrema
        
        
    # A recursive approach to finding the convex hull,
    # similar to divide and conquer or quick-hull
    def convexHull(self, points):
        
        #Get vertices of an up-to-8-sided polygon where the vertices
        # are extrema from the pointcloud
        extrema = self.extremePoints(points)
        
        # Loop through all of the points. We'll check and see if they are
        # outside of the polygon defined by extrema. In most datasets,
        # only about sqrt(N) of the points will be outside of the polygon
        # We'll just ignore anything inside the polygon as they can't be on the hull.
        # Even better, each point can only be 'outside' of exactly one side of the polygon
        # We'll collect those points that can contribute to the hull ouside of 
        # each side into its own buffer to deal with in the next step.
        # The equation determines what side of the line defined by the consecutive
        # vertices any given point is. Since we're traversing the vertices strictly
        # counter-clockwise, we only want to keep ones on the 'right'
        N = len(extrema)
        Buffer = [ [extrema[j]] for j in range(N)]
        for p in points:
            pX,pY = p
            for j in range(N):
                x1,y1 = extrema[j-1]
                x2,y2 = extrema[j]
                if (x2-x1)*(pY-y1) < (y2-y1)*(pX-x1):               
                    Buffer[j] += [p]
        
        # For each side, we'll add those outside points to our hull or
        # calculate its own hull, and then add those points (recursing as needed) 
        hull = []
        for j in range(N):
            if len(Buffer[j]) > 2:
                # There's 'many' (to a gully dwarf) points in this buffer
                # so we'll simplify it by finding its own complex hull
                Buffer[j] = self.convexHull(Buffer[j])
            # There's only the vertex itself or it plus one other point,
            # which must therefore be on the hull as well. Collect them
            hull += Buffer[j]
        
        return hull
                    

    def largestTriangleArea(self, points):
        # Step one, find a polygon that encloses all points.
        # The biggest triangle must be made from these points
        hull = self.convexHull(points)
        
        # Use the brute force algorithm to find the area from the much smaller
        # number of hull points.
        maxArea = self.largestTriangleAreaO3(list(hull))
        
        
        return maxArea
        


S = Solution()
points = [[0,0],[0,1],[0,2],[1,0],[1,1],[2,0]]
points = [[42, 1], [34, 49], [2, 5], [33, 30], [8, 37], [43, 9], [38, 37], [23, 8], [48, 30], [11, 25], [16, 20], [22, 44], [40, 42], [36, 16], [47, 46], [29, 34], [34, 6], [20, 9], [40, 38], [24, 10], [24, 12], [44, 30], [36, 2], [34, 27], [39, 28], [45, 23], [15, 28], [26, 30], [31, 22], [3, 5], [41, 20], [50, 42], [43, 47], [25, 19], [19, 48], [41, 47], [12, 11], [32, 44], [28, 40], [49, 2]]
points = [[13,-50],[43,3],[-35,38],[-9,-14],[9,2],[43,-3],[-1,-32],[25,7],[28,4],[26,16]]

print(S.largestTriangleArea(points))