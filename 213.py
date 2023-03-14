class Solution:
    def rob(self, nums) -> int:
        def houseRob(nums) :
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n) :
                dp[i] = max(dp[i-1],nums[i]+dp[i-2])
            
            return dp[-1]
        
        if len(nums) <= 2 : return max(nums)

        return max(houseRob(nums[1:]),houseRob(nums[:-1]))