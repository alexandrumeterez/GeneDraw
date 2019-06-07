from population import Population

GENERATIONS = 20000

if __name__ == "__main__":
    population = Population()
    for i in range(GENERATIONS):
        print(f"Current generation: {i}")
        population.forward()

        fittest = population.fittest()
        print(f"Best fitness: {fittest.fitness}")
        if (i + 1) % 100 == 0:
            fittest.image.save(f"fittest_gen{i}.png")