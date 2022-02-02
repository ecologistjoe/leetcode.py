class Solution:
    
    def _findMedian(self, nums):
        m = len(nums) // 2
        median = nums[m]
        if len(nums) % 2 == 0:
            median += nums[m-1]
            median /= 2
        return median
    
    
    def _findDisjointMedian(self, lower, higher):
        # This finds the median of two independantly sorted lists of arbitrary length 
        
        N1 = len(lower)
        N2 = len(higher)
        
        # gets the proper index of the midpoint if there's an odd-number of elements
        m = (N1+N2) // 2
        if m < N1:
            median = lower[m]
        else:
            median = higher[m-N1]

        # If there are an even number of elements, midpoint has the second index
        #  so get the previous index and average them
        if (N1+N2) % 2 == 0:
            if m-1 < N1:
                median += lower[m-1]
            else:
                median += higher[m-1-N1]
            median = median / 2
        
        return median
    
    
    def findMedianSortedArrays(self, nums1, nums2):
        
        N1 = len(nums1)
        N2 = len(nums2)
        
        #
        # Case 1: One of the lists is empty
        #
        if (N1 == 0):
            return self._findMedian(nums2)
        if (N2 == 0):
            return self._findMedian(nums1)
        
        # Case 2: Numbers in Lists do not overlap
        #
        if (nums1[-1] <= nums2[0]):
            return self._findDisjointMedian(nums1, nums2)
        if (nums2[-1] <= nums1[0]):
            return self._findDisjointMedian(nums2, nums1)
        
        #
        # Case 3: The values in the arrays overlap.
        #
        
        # Do a swap to ensure N1 is shorter than N2
        if N2<N1:
            _tmp = nums1
            nums1 = nums2
            nums2 = _tmp
            
            _tmp = N1
            N1 = N2
            N2 = _tmp

        # The median index value (or the first of two if N1+N2 is even)
        target = (N1+N2-1)//2

        #Case 3a: 'Near disjoint' This happens when the first value of the short
        # array is greater than the target index considering only the longer array
        # This can often be the case when one list is much smaller
        if nums1[0] > nums2[target]:
            M = nums2[target]
            if (N1+N2) % 2 == 0:
                if (target == N2-1):
                    M = M + nums1[0]
                elif nums1[0] < nums2[target+1]:
                    M = M + nums1[0]
                else:
                    M = M + nums2[target+1] 
                M = M/2
            return M
        
        #
        #Case 3b: Lists have fully overlapping values
        # In this case we perform a binary search to find the balanced
        # pair of indices with the smallest gap
        low = 0
        high = N1
        while  high-low > 1:
            
            p1 = (low+high)//2
            p2 = target-p1
            
            diff = nums1[p1] - nums2[p2]
            if diff==0:
                return nums1[p1]
                
            if diff > 0:
                high = p1
            else:
                low = p1
            
            
        # get the greater value from the two smaller indices
        p1 = low
        p2 = target-p1-1

        if nums1[p1] > nums2[p2]:
            M= nums1[p1]
        else:
            M= nums2[p2]
        
        
        if (N1+N2)%2==0:
            if (p1 == N1-1):
                M = M + nums2[p2+1]
            elif (p2 == N2-1):
                M = M + nums1[p1+1]
            elif nums1[p1+1] < nums2[p2+1]:
                M = M + nums1[p1+1]
            else:
                M = M + nums2[p2+1] 
            M = M/2
        
        
        return M
                    
            
        
        
        
        
        
        
        
        
        