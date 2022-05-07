#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
                if ans < count:
                    ans = count
            else:
                count = 0
        return ans
# @lc code=end

