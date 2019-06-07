from PIL import Image
import sys
if len(sys.argv) != 2:
    print("Usage: python genedraw.py <target_image>")
    sys.exit()
TARGET = Image.open(sys.argv[1]).convert('RGB')
WIDTH = TARGET.size[0]
HEIGHT = TARGET.size[1]

# Number of members in a population
POPULATION_SIZE = 50
MUTATION_RATE = 0.02
# How many polygons are in an individual
GENOME_LENGTH = 100

MAX_VERTICES = 4
CROSSOVER_TYPE = 2
FORWARD_TYPE = 2
