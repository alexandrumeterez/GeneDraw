from individual import Individual
from parameters import *
import random 

class Population(object):
    def __init__(self):
        self.individuals = []
        for _ in range(POPULATION_SIZE):
            self.add_individual(Individual())
        self.individuals.sort(key = lambda x: x.fitness, reverse = True)

    def add_individual(self, x):
        self.individuals.append(x)
    
    def forward(self):
        # All individuals are sorted, so I just pick the first 2
        if FORWARD_TYPE == 1:
            del self.individuals[-1]
            del self.individuals[-1]

            fittest = self.individuals[0]
            second_fittest = self.individuals[1]
            self.add_individual(Individual(fittest, second_fittest))
            self.add_individual(Individual(second_fittest, fittest))
        elif FORWARD_TYPE == 2:
            # The solution of the github inspiration
            selection_count = int(POPULATION_SIZE / 10)
            for i in range(selection_count, POPULATION_SIZE):
                m = self.individuals[random.randint(0, selection_count - 1)]
                f = self.individuals[random.randint(0, selection_count - 1)]
                self.individuals[i] = Individual(m, f)
            self.individuals.sort(key = lambda x: x.fitness, reverse = True)

    def fittest(self):
        return self.individuals[0]
    