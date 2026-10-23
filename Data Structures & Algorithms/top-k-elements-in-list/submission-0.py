class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for n in nums:
            if n not in mydict:
                mydict[n]=1
            else :
                mydict[n]+=1
        l=sorted(mydict,key=mydict.get,reverse=True)
        return l[:k]
