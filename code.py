class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            upperLimit = (l + r) // 2
            curSum, pieces = 0, 1
            for num in nums:
                curSum += num
                if curSum > upperLimit:
                    curSum = num
                    pieces += 1
            if pieces <= m: 
                r = upperLimit
            else: 
                l = upperLimit + 1
        return l 
