#brute-force approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1 : return strs[0]
        if all(strs) is False : return ''
        s = strs[0]
        res = ''
        n = len(strs) -1
        for i in range(len(s)) :
            k = s[i]
            count = 0
            for j in strs[1:] :
                try :
                    if j[i] == k : 
                        count += 1
                except :
                    break
            if count == n :
                res += k
            else :
                return res
        return res


#Approach-2

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        l = list(zip(*strs)) #[('f','f','f'),('l','l','l'),('o','o','i'),('w','w','g')]
        res = ''
        for i in l :
            if len(set(i)) == 1 :
                res += i[0]
            else : break
        return res

#Approach - 3

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre     
