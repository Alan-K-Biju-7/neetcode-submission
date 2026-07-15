class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        left  = 0
        right = 1
       
        curr_streak = 1
        max_streak = 1
        if len(nums) == 0:
            return 0
        while right < len(nums):
            if len(nums) == 1:
                return 1
            elif nums[left] + 1 == nums[right]:
                curr_streak += 1
                left +=1
                right +=1
            elif nums[left] == nums[right]:
                
                left +=1
                right +=1
            else:
                curr_streak = 1
                left +=1
                right +=1
            max_streak = max(curr_streak,max_streak)   
        print(nums)        
        return max_streak           
        