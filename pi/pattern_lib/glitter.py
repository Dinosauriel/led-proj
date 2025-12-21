from pi.pattern import Pattern1D
import numpy as np

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.color = np.array([255,255,255]) * 0.7
        self.colors = np.zeros((n, 3))
        self.interval = 70
        self.decay = np.random.uniform(low=0.95, high=0.9999, size=(self.n, 1))

    def draw(self, t):

        k = np.random.geometric(0.8) - 1
        glitter_i = np.random.choice(np.arange(self.n), size=k)
        for i in glitter_i:
            self.colors[i] = self.color
        self.colors = self.colors * self.decay
        return self.colors.astype(np.int)
