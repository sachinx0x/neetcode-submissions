class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i,num in enumerate(nums):
            mydict[num]=i
        print(mydict)
        for t,n in enumerate(nums):
            temp=target-n
            if temp in mydict and mydict[temp]!=t:
                return [t,mydict[temp]]