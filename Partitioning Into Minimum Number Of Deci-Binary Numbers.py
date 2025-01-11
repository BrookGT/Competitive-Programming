class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        ans = 0
        for i in range(10):
            if str(i) in n:
                ans = i
        return ans
