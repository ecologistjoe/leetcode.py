import mediantwolists as mtl
import statistics as stat


tests = [
            ([5], [1,2,3,4,6]),
            ([5,6], [1,2,3,4,7]),

            ([3], [1,2,4]),
            ([4], [1,2,3,3,6]),
            ([1,3,4,7],[0,1,5,6]),
            ( [1,2], [1,2]),
            ([1, 3, 5, 7, 8, 12], [-4, -3, 0, 3, 16]),
            ( [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [10, 18, 21, 22, 24, 26, 28, 30])
        ]


for i in range(len(tests)):
    A = tests[i][0]
    B = tests[i][1]
    S = mtl.Solution()
    print(i+1, 'Expected: ', stat.median(A+B),' : ', S.findMedianSortedArrays(A,B))
    print()
    

