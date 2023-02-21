class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high :
            m = (low+high) // 2
            
            if nums[m] == target :
                return m
            elif nums[m] < target :
                low = m + 1
            else :
                high = m - 1
        return low
        
#Approach - 2

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]>=target):
                return i
        return len(nums)   
