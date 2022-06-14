class Solution:
    dp=[[0 for i in range(501)] for j in range(501)]
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        for i in range(n):
            for j in range(m):
                self.dp[i+1][j+1]=max(self.dp[i][j+1],self.dp[i+1][j])
                if word1[i]==word2[j]:
                    self.dp[i+1][j+1]=max(self.dp[i+1][j+1],self.dp[i][j]+1)
        return n+m-2*self.dp[n][m]