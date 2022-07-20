class Solution:
    def isPalindrome(self, x: int) -> bool:
        l1=str(x)
        l2=l1[::-1]
        return l1==l2