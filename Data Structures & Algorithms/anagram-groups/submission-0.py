class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict={}
        for i in strs:
            j="".join(sorted(i))
            if j in mydict:
                mydict[j].append(i)
            else:
                mydict[j]=[i]
        return list(mydict.values())