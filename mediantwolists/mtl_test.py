import mediantwolists as mtl

A = [0, 1, 3, 5, 7, 8, 12]
B = [-4, -3, 0, 3, 16]
S = mtl.Solution()
print(S.findMedianSortedArrays(A,B))
print("Solution should be: 3")
print()

A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
B = [10, 18, 21, 22, 24, 26, 28, 30]
S = mtl.Solution()
print(S.findMedianSortedArrays(A,B))
print("Solution should be: 19")

