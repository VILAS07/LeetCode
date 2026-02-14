class Solution:
    def champagneTower(self, p: int, r: int, c: int) -> float:
        return min(1,reduce(lambda q,_:[*map(sum,
            pairwise(max(v-1,0)/2 for v in [0]+q+[0]))],range(r),[p])[c])