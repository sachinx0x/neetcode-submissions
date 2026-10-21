class Solution:
    def isValid(self, s: str) -> bool:
        mydict={"]":"[",")":"(","}":"{"}
        stack=[]
        for i in s:
            if i!="]" and i!=")" and i!="}":
                stack.append(i)
            else:
                if stack:
                    top=stack.pop()
                    if top!=mydict[i]:
                        return False
                else: return False 
        return not stack