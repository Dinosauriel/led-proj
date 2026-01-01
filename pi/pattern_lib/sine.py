from pattern import Pattern3D
import numpy as np
import math

class Pattern(Pattern3D):
    def __init__(self, n, coords):
        super().__init__(n, coords)
        self.colors = np.zeros((n, 3))

    def draw(self, t):
        y = math.sin(t / 500) * 500 + 500
        for i in range(self.n):
            if abs(self.coords[i][1] - y) < 100:
                self.colors[i] = (255, 255, 255)
            else:
                self.colors[i] = (0, 0, 0)
        return self.colors.astype(np.int)
