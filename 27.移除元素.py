#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in nums:
            if r != val:
                nums[l] = r
                l += 1

        return l
# @lc code=end

