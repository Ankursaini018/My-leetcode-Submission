class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        basket = {}
        ans = 0

        for right in range(len(fruits)):

            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            ans = max(ans, right - left + 1)

        return ans