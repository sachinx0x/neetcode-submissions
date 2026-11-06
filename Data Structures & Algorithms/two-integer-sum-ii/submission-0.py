class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L=0
        R=len(numbers)-1
        while target!= (total:=numbers[L]+numbers[R]):
            if total<target:
                L=L+1
            else : R=R-1
        return [L+1,R+1]