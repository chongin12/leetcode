class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":0, "V":1, "X":2, "L":3, "C":4, "D":5, "M":6}
        n=[1,5,10,50,100,500,1000]
        r=0
        prev=7
        for i in s:
            r+=n[d[i]]
            if prev==(d[i]-1)//2*2:
                r-=n[prev]*2
            prev=d[i]
        return r
            
                    