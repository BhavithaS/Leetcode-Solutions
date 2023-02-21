#using list, set to identify occurences and store
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        s = set(arr)
        occurences = []
        for i in s:
            k = arr.count(i)
            if k not in occurences :
                occurences.append(k)
            else :
                return False
        return True


#ANOTHER SOLUTION
#using COUNTER and comparing lengths
import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        res = collections.Counter(arr).values()
        return len(list(res)) == len(set(res))

#simplified 
class Solution:
    def uniqueOccurrences(self, A) -> bool:
    	return (lambda x: len(x) == len(set(x)))(collections.Counter(A).values())

