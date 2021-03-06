# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 11:50
# @Author  : Yulong Liu
# @File    : p0003_M_LongestSubstringWithoutRepeatingCharacters.py

"""
题号：3
难度：medium
链接：https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
描述：找一个字符串中无重复字符的最长子串
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        longest = 0
        for x in s:
            if x not in l:
                l.append(x)
            else:
                index = l.index(x)
                l = l[index+1:]
                l.append(x)
            if len(l) > longest:
                longest = len(l)
        return longest


if __name__ == '__main__':
    # s = 'abcabcbb'
    s = 'pwwkew'
    print(Solution().lengthOfLongestSubstring(s))