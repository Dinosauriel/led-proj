from pattern import Pattern1D
import numpy as np

def rotate(color, speed):
    # print("rotate", color, ", ", speed)
    zero = 0
    for i in range(len(color)):
        if color[i] == 0 and color[(i + 1) % 3] != 0:
            zero = i

    prev = (zero - 1) % 3
    next = (zero + 1) % 3

    if color[prev] < 196:
        color[prev] = min(color[prev] + 3 * speed, 196)
    else:
        color[next] = max(color[next] - 3 * speed, 0)
    return color


class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.colors = np.zeros((n, 3))
        self.colors[:][0] = 196
        self.interval = 150
        self.speed = np.random.uniform(low=0.2, high=1., size=(self.n, 1))

    def draw(self, t):
        for i in range(self.n):
            self.colors[i] = rotate(self.colors[i], self.speed[i])
        return self.colors.astype(np.int)
