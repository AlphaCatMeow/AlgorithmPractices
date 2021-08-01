#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = dict()
        for i in range(len(nums)):
            if target - nums[i] in ans:
                return [ans[target - nums[i]], i]
            ans[nums[i]] = i
# @lc code=end

