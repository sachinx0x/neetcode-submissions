class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict={}
        if len(s)==len(t):
            for char in s:
                if char in mydict:
                    mydict.update({char:mydict[char]+1})
                else:
                    mydict[char]=1
            for char in t:
                if char in mydict:
                    mydict.update({char:mydict[char]-1})
            for key in mydict:
                if mydict[key]==0:
                    continue
                else: return False
            return True
        else:return False