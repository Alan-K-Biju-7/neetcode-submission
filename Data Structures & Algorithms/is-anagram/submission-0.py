class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1= sorted(s)
        check2 = sorted(t)
        if check1 == check2:
            return True
        else:
            return False
                
        