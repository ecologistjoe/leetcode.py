# This is classified as 'easy', but it's a pretty complicated and interesting problem
# The problem spec says there will only ever be 50 items in the list, so perhaps
# the naive O(n^3) solution is what was expected

# Area of a Triangle: 1/2*(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 -y3*x1)

from convexHull import convexHull

class Solution:
    # The brute-force search O(n^3) solution
    # There's probably small pythonic optimizations that could be done
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
        
    def largestTriangleArea(self, points):
        # Step one, find a polygon that encloses all points.
        # The biggest triangle must be made from these points
        ch = convexHull(points)
        # Use the brute force algorithm to find the area from the much smaller
        # number of hull points.
        maxArea = self.largestTriangleAreaO3(ch.hull)
        return maxArea


points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(S.largestTriangleArea(points))




