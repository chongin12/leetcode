class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs[0])
        for s in strs:
            idx=-1
            for i in range(len(s)):
                if i==l:break
                if strs[0][i]!=s[i]:break
                idx=i;
            l=idx+1
        return strs[0][:l]