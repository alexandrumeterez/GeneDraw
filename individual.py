from parameters import *
from gene import Gene
from PIL import Image, ImageDraw, ImageChops
import random
class Individual(object):
    def __init__(self, mother=None, father=None): 
        self.genome = []
        if mother is None and father is None:
            for _ in range(GENOME_LENGTH):
                self.add_gene(Gene())
        else:
            if CROSSOVER_TYPE == 1:
                crossover_point = random.randint(1, GENOME_LENGTH)
                self.genome = mother.genome[:crossover_point]
                self.genome.extend(father.genome[crossover_point:])
            elif CROSSOVER_TYPE == 2:
                # Solution of the github inspiration
                for i in range(GENOME_LENGTH):
                    if random.random() > 0.5:
                        self.add_gene(mother.genome[i])
                    else:
                        self.add_gene(father.genome[i])
                self.mutate()

        self.image = self.draw_individual()
        self.fitness = self.compute_fitness()

    def add_gene(self, x):
        self.genome.append(x)

    def draw_individual(self):
        image = Image.new('RGB', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(image, 'RGBA')
        for i in range(GENOME_LENGTH):
            poly = self.genome[i].vertices
            color = (self.genome[i].R, self.genome[i].G, self.genome[i].B, self.genome[i].A)
            draw.polygon(poly, color) 
        return image
    
    def compute_fitness(self):
        diff = ImageChops.difference(self.image, TARGET)
        data = diff.getdata()
        illness = 1.0 * sum(map(sum, data)) / (WIDTH * HEIGHT * 255 * 3)
        return 1 - illness
    
    def mutate(self):
        for i in range(GENOME_LENGTH):
            if random.random() < MUTATION_RATE:
                self.genome[i] = Gene()