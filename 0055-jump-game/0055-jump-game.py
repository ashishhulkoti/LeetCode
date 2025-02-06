class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        dest=len(nums)-1
        jump_position=dest-1
        while jump_position>=0:
            if (jump_position+nums[jump_position])>=dest:
                dest=jump_position
                if jump_position==0:
                    return True            
            jump_position-=1
        return False
            