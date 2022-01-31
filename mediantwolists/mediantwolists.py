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
        
        return M
    
    
    def findMedianSortedArrays(self, nums1, nums2):
        
        print(nums1, nums2)
        
        N1 = len(nums1)
        N2 = len(nums2)
        
        #
        # Case 1: One of the lists is empty
        #
        if (N1 == 0):
            return self._findMedian(nums2)
        if (N2 == 0):
            return self._findMedian(nums1)
            
        
        #
        # Case 2: Numbers in Lists do not overlap
        #
        if (nums1[-1] < nums2[0]):
            return self._findDisjointMedian(nums1, nums2)
        if (nums2[-1] < nums1[0]):
            return self._findDisjointMedian(nums2, nums1)
        
        
        #
        #Case 3: Lists have overlapping values
        #
    
        low1 = 0
        high1 = N1
        low2 = 0
        high2 = N2

        M1 = self._findMedian(nums1)
        M2 = self._findMedian(nums2)

        if M1==M2:
            return M1

        if N1 <= N2:
            m = (N1-1) // 2
        else:
            m = (N2-1) // 2
            
        if M1 < M2:
            low1 = low1 + m +1
            high2= high2 - m-1

        if M1 > M2:
            low2  = low2 + m +1
            high1 = high1 - m -1

        return self.findMedianSortedArrays(nums1[low1:high1], nums2[low2:high2])            
        
        
        
        
        
        
        
        