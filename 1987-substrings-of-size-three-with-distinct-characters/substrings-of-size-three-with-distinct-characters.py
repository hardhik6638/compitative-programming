class Solution:
    def countGoodSubstrings(self, s: str) -> int:
          if (len(s)) < 3:
            return 0
          ans = 0
          for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                ans += 1
          return ans