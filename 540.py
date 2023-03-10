class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = set()
        d = set()
        for i in nums :
            if i not in s :
                s.add(i)
            else :
                d.add(i)
        return list(s-d)[0]


#Approach - 2
 
