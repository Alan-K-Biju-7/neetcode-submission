class Solution:
    def countSubstrings(self, s: str) -> int:
       n = len(s)
       dp = [[False] * n for _ in range(n)]
       ans = s[0]
       count = 0
       for i in range(n):
            dp[i][i] = True
            count += 1
       for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True 
            ans = s[i:i+2]
            count += 1   
       for length in range(3,n+1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end] and dp[start+1][end-1]:
                dp[start][end] = True
                ans = s[start:end+1]
                count += 1
       return count                 
