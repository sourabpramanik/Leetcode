class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(map(tuple, trees), key=lambda x:(x[0], x[1]))
        
        def sign(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])
        
        def build(trees):
            hull = []
            for p in trees:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull += p,
            return hull
        
        return list(set(build(trees) + build(trees[::-1])))