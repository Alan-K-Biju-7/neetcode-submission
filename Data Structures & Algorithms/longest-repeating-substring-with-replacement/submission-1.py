class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        max_freq = 0
        seen = dict()
        ans = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1
            right = i
            max_freq = max(max_freq,seen[s[i]])  
            while (right-left+1) - max_freq > k:
                seen[s[left]] -= 1
                left +=1




            ans = max(ans, right - left + 1)
        return ans    
                





            

        
        