
'''
this is a test
1. generate a population of network structures.
2. train them to associate a given pattern.
3. evolve them to associate a second pattern.
'''

def main():

    # 1. read options file
    options = optionsReader()
    
    # 2. create population of networks
    population = populationInitializer(options)

    # 3. evolve population
    results = evolver(population)
    
    # 4. saving results
    resultsWriter(results)
    

    return None
