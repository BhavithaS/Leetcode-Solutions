class Solution:
    def search(self, nums, target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j :
            mid = (i+j)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                i = mid + 1
            else :
                j = mid - 1
        return -1


class Solution:
    def search(self, nums, target: int) -> int:
        if target in nums :
            return nums.index(target)
        return -1
