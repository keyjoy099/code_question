# -*- coding:utf-8 -*-

"""
题目：n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

1 <= n <= 11
"""

"""
思路：
用两个数组存储骰子点数之和出现的次数。
在一轮循环中，第一个数组的第n个数字表示骰子点数之和为n出现的次数；
在下一轮循环中(增加一个骰子，假设骰子点数最多为6)，此时骰子点数之和为n出现的次数 等于 上一轮循环中骰子点数之和为 n-1、n-2、n-3、n-4、n-5、n-6 出现的次数之和。

"""


class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        max_value = 6
        probability = [[0] * (n * max_value + 1) for i in range(2)]  # 0位不使用，角标从1开始用；最大点数为n * max_value

        # 第一次初始化
        flag = 0
        for i in range(1, max_value + 1):
            probability[flag][i] = 1  # 每个点数出现1次

        # 第一次之后的循环
        for k in range(2, n + 1):
            for m in range(1, k):
                probability[1 - flag][m] = 0  # k个骰子，最小的点数之和为k，将小于k的位置值置为0

            for z in range(k, max_value * k + 1):  # k个骰子，最小点数之和为k，最大点数之和为 max_value * k
                probability[1 - flag][z] = 0  # 将[最小点数之和k, 最大点数之和max_value * k] 这些需要重新计算的位置 先置为0
                for j in range(1, min(z, max_value) + 1):  # 注意不能越界；假设k=3，那么z=4这个位置只能有 4-1=3、4-2=2、4-3=1(、4-4=0) 来加和；j要能取到max_value，因此min后要+1，如 z=8，max_value=6
                    probability[1 - flag][z] += probability[flag][z - j]
            flag = 1 - flag

        total = max_value ** n  # 每个骰子都有 max_value 种点数可能
        result_list = []
        for i in range(n, max_value * n + 1):
            result_list.append(round(probability[flag][i] / float(total), 5))

        return result_list


def execute():
    # n = 11
    # n = 1
    n = 2
    sol = Solution()
    print(sol.dicesProbability(n))


if __name__ == "__main__":
    execute()
