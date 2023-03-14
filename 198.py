class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        if n == 1 : return nums[0]
        # if n < 2 :
        #     return 
        dp[1]=nums[0]
        dp[2] = nums[1]
        for i in range(3,n+1):
            dp[i] = max(dp[i-2],dp[i-3]) + nums[i-1]
        return max(dp[n],dp[n-1])