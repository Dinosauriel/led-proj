from pattern import Pattern3D
import numpy as np
import math
import time

def rainbow(alpha: int):
    alpha %= 768
    r = max(0, -129 + abs(alpha - 384))
    g = max(0, 255 - abs(alpha - 256))
    b = max(0, 255 - abs(alpha - 512))
    if max(r, max(g, b)) > 255:
        print(f"{alpha} -> {(r,g,b)}")
    return (r, g, b)

class Pattern(Pattern3D):

    def __init__(self, n, coords):
        super().__init__(n, coords)
        self.colors = np.zeros((n, 3))
        self.color = (0, 0, 0)
        self.last_color_change = -1

    def draw(self, t):
        lt = time.localtime()
        h = lt.tm_hour
        m = lt.tm_min
        s = lt.tm_sec

        #if lt.tm_hour < 23 and lt.tm_hour > 1:
        #    return self.colors.astype(np.int)

        # if lt.tm_hour == 23 and lt.tm_minute

        if self.last_color_change == -1 or (s % 10 == 0 and self.last_color_change != s):
            self.last_color_change = s
            # self.color = np.random.uniform(low=50, high=255, size=3).astype(np.int)
            self.color = rainbow(np.random.uniform(low=0, high=768))

        for i in range(self.n):
            if self.coords[i][1] > 900 - (s % 10) * 100:
                self.colors[i] = self.color
            else:
                self.colors[i] = (0, 0, 0)
        return self.colors.astype(np.int)
