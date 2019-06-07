import random
from parameters import *

class Gene(object):
    def __init__(self):
        self.n_vertices = random.randint(2, MAX_VERTICES)
        self.vertices = []
        self.randomize_RGBA()
        self.randomize_vertices()

    def randomize_RGBA(self):
        self.R = random.randint(0, 255)
        self.G = random.randint(0, 255)
        self.B = random.randint(0, 255)
        self.A = random.randint(0, 50)

    def randomize_vertices(self):
        for _ in range(self.n_vertices):
            vertex = random.uniform(-10, WIDTH + 10), random.uniform(-10, HEIGHT + 10)
            self.vertices.append(vertex)