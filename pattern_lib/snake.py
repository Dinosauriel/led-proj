from pattern import Pattern1D
import numpy as np

class PatternSnake(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.colors = np.zeros((n, 3))
        self.head = 0
        self.interval = 20

    def draw(self, t):
        if self.head == 0:
            self.color = np.random.uniform(0.0, 255., size=3)

        self.colors *= 0.9
        self.colors[self.head] = self.color
        self.head = (self.head + 1) % self.n
        return self.colors.astype(np.int)
