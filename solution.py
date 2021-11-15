# from configuration import candies, extraCandies, jewels, stones, num, s, target


class Solution:
    def __init__(self, candies, extraCandies, nums, jewels, stones, num, s, target):
        self.candies = candies
        self.extraCandies = extraCandies
        self.nums = nums
        self.jewels = jewels
        self.stones = stones
        self.num = num
        self.s = s
        self.target = target

    # 1431
    def kidsWithCandies(self):
        result = []
        for candy in self.candies:
            if candy + self.extraCandies >= max(self.candies):
                result.append(True)
            else:
                result.append(False)
        return result

    # 283
    def moveZeroes(self):
        for num in self.nums:
            if num == 0:
                self.nums.remove(num)
                self.nums.append(num)
            else:
                self.nums = self.nums
        return self.nums

    # 771
    def numJewelsInStones(self):
        jewels_list = list(set(list(self.jewels)))
        counter = 0
        stones_list = list(self.stones)
        for jewel in jewels_list:
            for stone in stones_list:
                if jewel == stone:
                    counter += 1
        return counter

    # 1342
    def numberOfSteps(self):
        counter = 0
        while self.num != 0:
            if self.num % 2 == 0:
                self.num = self.num / 2
                counter += 1
            elif self.num % 2 != 0:
                self.num = self.num - 1
                counter += 1
        return counter

    # 1859
    def sortSentence(self):
        l_of_words = self.s.split()
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
    def search(self):
        if self.target in self.nums:
            return self.nums.index(self.target)
        else:
            return -1

    # 35
    def searchInsert(self):
        try:
            return self.nums.index(self.target)
        except ValueError:
            self.nums.append(self.target)
            self.nums.sort()
            return self.nums.index(self.target)

    # 977
    def sortedSquares(self):
        sq_nums = [i ** 2 for i in self.nums]
        sq_nums.sort()
        return sq_nums
