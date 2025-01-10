class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        def count(word):
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return freq

        max_freq = [0] * 26
        for word in words2:
            for i, cnt in enumerate(count(word)):
                max_freq[i] = max(max_freq[i], cnt)

        result = []
        for word in words1:
            word_freq = count(word)
            if all(word_freq[i] >= max_freq[i] for i in range(26)):
                result.append(word)

        return result
