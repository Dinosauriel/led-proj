
import numpy

class Pattern3D():
    '''
    param n: number of LEDs
    param coords: numpy array of shape (n, 3). coords[i] contains the coordinates for LED i.
                    coordinates are normalized to [0, 1]
    '''
    def __init__(self, n, coords) -> None:
        self.n = n
        self.coords = coords
        self.should_finish = False

    '''
    draw() takes as input a time t in milliseconds, and returns a numpy array of shape (n, 3) 
    that contains the color of each LED at time t
    '''
    def draw(self, t):
        pass

class Pattern1D():
    '''
    param n: number of LEDs
    '''
    def __init__(self, n) -> None:
        self.n = n
        self.should_finish = False

    '''
    draw() takes as input a time t in milliseconds, and returns a numpy array of shape (n, 3) 
    that contains the color of each LED at time t
    '''
    def draw(self, t):
        pass
