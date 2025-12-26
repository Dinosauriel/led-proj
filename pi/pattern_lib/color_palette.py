from pattern import Pattern1D
import numpy as np
import util as util

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.color = np.array([255,255,255]) * 0.7
        palette = [
            np.array(util.red),
            np.array(util.green),
            np.array(util.blue),
            np.array((255,165,0))
        ]

        choices = np.random.choice(len(palette), size=n)
        self.colors = np.zeros((n, 3))
        for i in range(n):
            self.colors[i] = palette[choices[i]]
        self.interval = 10000

    def draw(self, t):
        return self.colors.astype(np.int)
