class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1 , 'V' : 5, 'X' : 10, 'L' : 50 , 'C' : 100,'D': 500,'M' : 1000}
        res = 0
        for i in range(len(s)) :
            val = d[s[i]]
            if i < len(s) -1 and d[s[i+1]] > val:
                res -= val
            else :
                res += val
        return res

# Approach 2
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1 , 'V' : 5, 'X' : 10, 'L' : 50 , 'C' : 100,'D': 500,'M' : 1000}
        res = 0
        i = 0
        while i < len(s) :
            if s[i] not in ['I','X','C'] :
                res += d[s[i]]
                i += 1
            else:
                if s[i] == 'I' :
                    try :
                        if s[i+1] =='V' or s[i+1] =='X' :
                            res += (d[s[i+1]] - d[s[i]])
                            i += 2
                        else :
                            res += d[s[i]]
                            i += 1
                    except :
                        res += d[s[i]]
                        i += 1
                elif s[i] == 'X' :
                    try :
                        if s[i+1] =='L' or s[i+1] =='C' :
                            res += (d[s[i+1]] - d[s[i]])
                            i += 2
                        else :
                            res += d[s[i]]
                            i += 1
                    except :
                        res += d[s[i]]
                        i += 1
                else :
                    try :
                        if s[i+1] =='D' or s[i+1] =='M' :
                            res += (d[s[i+1]] - d[s[i]])
                            i += 2
                        else :
                            res += d[s[i]]
                            i += 1
                    except :
                        res += d[s[i]]
                        i += 1
        return res