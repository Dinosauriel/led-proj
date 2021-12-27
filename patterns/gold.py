from pattern import Pattern1D
import util
import numpy as np

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.colors = np.zeros((n, 3), dtype=np.int)

        self.dark_orange = (255,140,0)
        self.medium_blue = (0,0,205)
        self.golden =      (218,165,32)
        self.lime_green = (50,205,50)

        self.pallette = [
            util.multiply_color(util.red, 0.1),
            util.multiply_color(util.green, 0.1),
            util.multiply_color(util.blue, 0.1)
            # self.lime_green,
            # self.golden
        ]

        self.dt = 0
        for i in range(self.n):
            self.colors[i] = self.pallette[i % len(self.pallette)]

    def draw(self, t):
        # if t - self.dt > 1000:
        #     self.dt = t
        #     for i in range(self.n):
        #         j = np.random.randint(0, len(self.pallette))
        #         self.colors[i] = self.pallette[j]
        return self.colors
