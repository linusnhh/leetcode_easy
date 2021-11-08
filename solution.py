class Solution:
    def __init__(self):
        self.candies = candies
        self.extraCandies = extraCandies

    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for x in candies:
            if x + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


# 1431
candies = [12, 1, 10]
extraCandies = 10
easy = Solution()
print(easy.kidsWithCandies(candies, extraCandies))
