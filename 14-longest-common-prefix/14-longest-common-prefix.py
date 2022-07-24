class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=strs[0]
        for s in strs:
            idx=-1
            for i in range(len(s)):
                if i==len(l):break
                if l[i]!=s[i]:break
                idx=i;
            l=l[:idx+1]
        return l