import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        left = 0
        right = len(A)
        total = (len(A) + len(B))  
        half =  (total + 1) // 2
        median = 0
        while left <= right:
            mid  = (left + right) // 2
            par_A = mid
            par_B = half - par_A
            A_left = A[par_A-1] if par_A > 0 else -math.inf

            A_right = A[par_A] if par_A < len(A) else math.inf
            B_left = B[par_B-1] if par_B > 0 else -math.inf
            B_right = B[par_B] if par_B < len(B) else math.inf

            if A_left <= B_right and B_left <= A_right:
                if total%2 != 0:
                    median = max(A_left,B_left)
                    return median
                else:
                    median = (max(A_left,B_left) + min(A_right,B_right)) / 2
                    return median
            else:
                if A_left > B_right:
                    right = mid - 1
                else:
                    left = mid + 1    
        return median            

                








        

        