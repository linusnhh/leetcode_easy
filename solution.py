from configuration import candies, extraCandies, jewels, stones, num, s, nums, target


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

    # 1859
    def sortSentence(self, s):
        l_of_words = s.split()
        words_dict = {}
        for word in l_of_words:
            order = int(word[-1])
            word = word[:-1]
            words_dict[order] = word
        word_list_s = sorted(words_dict.items())
        sentence = []
        for word_order in word_list_s:
            sentence.append(word_order[1])
        answer = ' '.join(sentence)
        return answer

    # 704
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1

    # 35
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            nums.append(target)
            nums.sort()
            return nums.index(target)

    def sortedSquares(self, nums):
        sq_nums = [i**2 for i in nums]
        sq_nums.sort()
        return sq_nums


easy = Solution()

# 1431
print(easy.kidsWithCandies(candies, extraCandies))

# 771
print(easy.numJewelsInStones(jewels, stones))

# 1342
print(easy.numberOfSteps(num))

# 1859
print(easy.sortSentence(s))

# 704
print(easy.search(nums, target))

# 35
print(easy.searchInsert(nums, target))

# 997
print(easy.sortedSquares(nums))
