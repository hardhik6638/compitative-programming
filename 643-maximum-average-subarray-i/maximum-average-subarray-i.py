class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        r=k
        if len(nums)==1:
            return nums[0]
        maxi=sum(nums[i:r])
        csum=maxi
        for r in range(k,len(nums)):
            csum=csum-nums[i]+nums[r]
            if maxi<csum:
                maxi=csum
            i+=1
        return maxi/k