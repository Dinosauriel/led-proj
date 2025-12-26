from pattern import Pattern1D
import numpy as np
import util as util

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.color = np.array(util.white)
        self.colors = np.broadcast_to(self.color, (n, 3))
        self.interval = 1000

    def draw(self, t):
        return self.colors.astype(np.int)
