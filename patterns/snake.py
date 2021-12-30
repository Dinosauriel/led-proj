from pattern import Pattern1D
import util
import numpy as np

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.golden = np.array([184,134,11]) * 0.3
        # self.colors = np.broadcast_to(self.golden, (n, 3))
        self.colors = np.zeros((n, 3))
        self.head = 0
        self.interval = 100
        self.factors = np.random.uniform(low=0.0, high=1., size=(self.n, 1))
        self.last = 0

    def draw(self, t):
        self.colors *= 0.7
        self.colors[self.head] = self.golden
        self.head = (self.head + 1) % self.n
        return self.colors.astype(np.int)
