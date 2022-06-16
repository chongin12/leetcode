class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxl=0
        maxr=0
        for i in range(n):
            l=i
            r=i
            for j in range(1,n):
                if i-j<0 or i+j>=n:break
                if s[i-j]!=s[i+j]:break
                l=i-j
                r=i+j
            if maxr-maxl<r-l:maxr,maxl=r,l
        for i in range(1,n):
            if s[i-1]!=s[i]:continue
            l=i-1
            r=i
            for j in range(1,n):
                if i-1-j<0 or i+j>=n:break
                if s[i-1-j]!=s[i+j]:break
                l=i-1-j
                r=i+j
            if maxr-maxl<r-l:maxr,maxl=r,l
        return s[maxl:maxr+1]