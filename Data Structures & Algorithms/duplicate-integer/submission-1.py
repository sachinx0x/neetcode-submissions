class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict={}
        for i,num in enumerate(nums):
            if num in mydict:
                return True
            else:
                mydict[num] =i
        return False