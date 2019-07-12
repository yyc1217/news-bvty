import numpy as np

class Scale:
    '''分數範圍管理'''

    def __init__(self, min = 1, max = 10):
        self.min = min
        self.max = max
        self.mean = (min + max) / 2
        self.sigma = (self.max - self.mean) / 3
        
    def arange(self):
        return np.arange(self.min, self.max + 1)

    def translateZ(self, z_score):
        '''將z-score轉換成實際分數'''
        
        translated = z_score * self.sigma + self.mean
        return max(min(translated, self.max), self.min)