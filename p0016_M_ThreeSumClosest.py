# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 15:45
# @Author  : Yulong Liu
# @File    : p0016_M_ThreeSumClosest.py


"""
题号：16
难度：medium
链接：https://leetcode.com/problems/3sum-closest/
描述：一串数字中，找出和最接近 target 的三个数的和
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """直接参考上一题，target 减一下就跟 closest 0 一样"""
        if not nums:
            return 0
        nums.sort()
        closest = closest_delta = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                delta = s - target
                if not closest_delta or abs(delta) < abs(closest_delta):
                    closest_delta = delta
                    closest = s
                if delta < 0:
                    l += 1
                elif delta > 0:
                    r -= 1
                else:
                    return target
        return closest


if __name__ == '__main__':
    data = [-1, 2, 1, 4]
    target = 1
    print(Solution().threeSumClosest(data, target))
