from bisect import bisect_left, insort

class Container:
    def __init__(self, k):
            self.k = k

            self.st1 = {}
            self.st1_keys = []
            self.st1Size = 0

            self.st2 = {}
            self.st2_keys = []
            self.st2Size = 0

            self.sm = 0  
    def _add_one(self, mp, keys, x):
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1
            insort(keys, x)

    def _remove_one(self, mp, keys, x):
        if mp[x] == 1:
            del mp[x]
            keys.pop(bisect_left(keys, x))
        else:
            mp[x] -= 1

    def _adjust(self):
        while self.st1Size < self.k and self.st2Size > 0:
            x = self.st2_keys[0]
            self._add_one(self.st1, self.st1_keys, x)
            self.st1Size += 1
            self.sm += x

            self._remove_one(self.st2, self.st2_keys, x)
            self.st2Size -= 1

        while self.st1Size > self.k:
            x = self.st1_keys[-1]
            self._add_one(self.st2, self.st2_keys, x)
            self.st2Size += 1

            self._remove_one(self.st1, self.st1_keys, x)
            self.st1Size -= 1
            self.sm -= x

    def add(self, x):
        if self.st2Size > 0 and x >= self.st2_keys[0]:
            self._add_one(self.st2, self.st2_keys, x)
            self.st2Size += 1
        else:
            self._add_one(self.st1, self.st1_keys, x)
            self.st1Size += 1
            self.sm += x

            self._adjust()

    def erase(self, x):
        if x in self.st1:
            self._remove_one(self.st1, self.st1_keys, x)
            self.st1Size -= 1
            self.sm -= x
        else:
            self._remove_one(self.st2, self.st2_keys, x)
            self.st2Size -= 1

        self._adjust()

    def sum(self):
        return self.sm


class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)

        cnt = Container(k - 2)

        for i in range(1, k - 1):
            cnt.add(nums[i])

        ans = cnt.sum() + nums[k - 1]

        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cnt.erase(nums[j])

            cnt.add(nums[i - 1])
            ans = min(ans, cnt.sum() + nums[i])

        return ans + nums[0]