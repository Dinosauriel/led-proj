from pattern import Pattern1D
import numpy as np

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.colors = np.zeros((n, 3))
        self.color = np.zeros(3)
        self.color[0] = 255
        self.head = 0
        self.interval = 10
        self.state = 0

    def draw(self, t):
        if self.state == 0:
          self.color[0] -= 1
          self.color[1] += 1
        elif self.state == 1:
          self.color[1] -= 1
          self.color[2] += 1
        else:
          self.color[2] -= 1
          self.color[0] += 1
        
        if self.color[self.state] == 0:
          self.state = (self.state + 1) % 3
          
        self.colors *= 0.9
        self.colors[self.head] = self.color
        self.head = (self.head + 1) % self.n
        
        return self.colors.astype(np.int)
