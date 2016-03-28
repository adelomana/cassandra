
'''
this is the main function of schema.
1. generate a population of graphs, inputs, outputs and expected fitness.
2. evolve population to equilibrium, test it for the new coupled pattern of EFs.
3. build graphs of the final results.
'''

def main():

    # 1. read options file
    options = optionsReader()
    
    # 2. create population of networks
    population = populationInitializer(options)

    # 3. evolve population
    results = evolver(population)
    
    # 4. saving results
    graphsBuilder(results)
    
    return None
