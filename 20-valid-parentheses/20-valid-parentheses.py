class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for c in s:
            if c==")" or c=="]" or c=="}":
                if len(a)==0:return False
                if ord(a[-1])//7==ord(c)//7:
                    a.pop(-1)
                else:return False
            else:
                a.append(c)
        if len(a)==0:return True
        return False