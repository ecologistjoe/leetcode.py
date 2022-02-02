# This is classified as 'easy', but it's a pretty complicated and interesting problem
# The problem spec says there will only ever be 50 items in the list, so perhaps
# the naive O(n^3) solution is what was expected


# Area of a Triangle: 1/2*(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 -y3*x1)

class Solution:
    def largestTriangleArea(self, points):
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
    
            


    
S = Solution()
points = [[0,0],[0,1],[0,2],[1,0],[1,1],[2,0]]
print(S.largestTriangleArea(points))