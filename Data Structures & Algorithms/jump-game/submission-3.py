class Solution:
    def canJump(self, nums: List[int]) -> bool:
        biggest_jump = nums[0]

        for i in range(1,len(nums)):
            if biggest_jump < i :
                return False
            curr_jump = i + nums[i]
        
            biggest_jump = max(biggest_jump,curr_jump)
        if biggest_jump >= len(nums) - 1:
            return True
        else:
            return False        
                