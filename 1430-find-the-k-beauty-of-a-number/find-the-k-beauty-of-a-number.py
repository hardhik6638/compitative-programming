class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        nums=str(num)
        sub=""
        for char in nums:
            sub+=char
            if len(sub)-1>=k-1:
                if int(sub)!=0 and len(sub)==k and num % int(sub)==0:
                    count+=1
                sub=sub[1:k+1]
        return count

        