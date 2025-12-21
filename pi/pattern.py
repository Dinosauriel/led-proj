
import numpy

class Pattern1D():
    '''
    param n: number of LEDs
    '''
    def __init__(self, n) -> None:
        self.n = n
        # set to true, if the pattern has finished (optional)
        self.should_finish = False
        # the (approximate) interval [ms] at which the pattern is polled
        self.interval = 10

    '''
    draw() takes as input a time t in milliseconds, and returns a numpy integer array of shape (n, 3) 
    that contains the color of each LED at time t
    '''
    def draw(self, t):
        pass


class Pattern3D(Pattern1D):
    '''
    param n: number of LEDs
    param coords: numpy array of shape (n, 3). coords[i] contains the coordinates for LED i.
                    coordinates are normalized to [0, 1]
    '''
    def __init__(self, n, coords) -> None:
        super().__init__(n)
        self.coords = coords