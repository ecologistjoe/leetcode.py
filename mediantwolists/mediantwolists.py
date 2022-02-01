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
        #Case 3: Lists have overlapping values
        #
    
        
        # Do a swap to ensure N1 is shorter than N2
        
        if N2<N1:
            _tmp = nums1
            nums1 = nums2
            nums2 = _tmp
            
            _tmp = N1
            N1 = N2
            N2 = _tmp
            
        
        #Case 3a: One list has only 1 value
        
        
        
        #Case 3b:
        low = 0
        high = N1
        t = (N1+N2-1)//2
        c = 0
        while  (c < 10):
            c = c+1
            
            p1 = (low+high)//2
            p2 = t-p1
            
            diff = nums1[p1] - nums2[p2]
            if diff==0:
                return nums1[p1]
                
            if diff > 0:
                high = p1
            else:
                low = p1
            
            if(high-low <= 1): break 
            
        # get the greater value from the two smaller indices



        p1 = low
        p2 = t-p1-1


        if low==0 and nums1[p1]>nums2[p2+1]:
            p1 = p1-1
            p2 = p2+1
            M = nums2[p2]    
        elif nums1[p1] > nums2[p2]:
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
                    
            
        
        
        
        
        
        
        
        
        