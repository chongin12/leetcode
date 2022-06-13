class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[0 for i in range(201)] for j in range(2)]
        dp[0][0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j==0:
                    dp[i%2][j]=dp[(i-1)%2][j]+triangle[i][j]
                elif j==i:
                    dp[i%2][j]=dp[(i-1)%2][j-1]+triangle[i][j]
                else:
                    dp[i%2][j]=min(dp[(i-1)%2][j-1], dp[(i-1)%2][j])+triangle[i][j]
        r=987654321
        for i in range(len(triangle)):
            r=min(r,dp[(len(triangle)-1)%2][i])
        return r
        