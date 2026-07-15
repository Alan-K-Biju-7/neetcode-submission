class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        start = 0 
        seen = dict()
        curr = dict()
        left = 0
        right = 1 
        matched = 0
        required = 0
        if len(s) == 0:
            return res
        if s == t:
            return s
        if len(s) < len(t):
            return ""       
        for i in t:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        for i in range(len(s)):
            right = i
            if s[right] not in curr:
                curr[s[right]] = 1
            else:
                 curr[s[right]] += 1
            if s[right] in seen and seen[s[right]] == curr[s[right]]:
                matched += 1
            required = len(seen)

            while required == matched:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left 
                curr[s[left]] -= 1

                if s[left] in seen and curr[s[left]] < seen[s[left]]:
                    matched -= 1
                left += 1   
        if min_len == float('inf'):
             return ""

        return s[start:start + min_len]               

             







        