from scipy.signal import convolve2d

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1 = [row[::-1] for row in img1][::-1] 
        res = convolve2d(img2, img1) 
        return res.max()