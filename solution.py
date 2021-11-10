from configuration import candies, extraCandies, jewels, stones, num


class Solution:
    def __init__(self):
        self.candies = candies
        self.extraCandies = extraCandies
        self.jewels = jewels
        self.stones = stones

    # 1431
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for x in candies:
            if x + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

    # 771
    def numJewelsInStones(self, jewels, stones):
        jewels_list = list(set(list(jewels)))
        counter = 0
        stones_list = list(stones)
        for jewel in jewels_list:
            for stone in stones_list:
                if jewel == stone:
                    counter += 1
        return counter

    # 1342
    def numberOfSteps(self, num):
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                counter += 1
            elif num % 2 != 0:
                num = num - 1
                counter += 1
        return counter

easy = Solution()

# 1431
print(easy.kidsWithCandies(candies, extraCandies))

# 771
print(easy.numJewelsInStones(jewels, stones))

# 1342
print(easy.numberOfSteps(num))