import numpy

def main(generation, label):

    inputFile='/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/evol3/data/colony counts APEE3 - generation %s.tsv'%str(generation)
    with open(inputFile,'r') as f:
        lines=f.readlines()
        for line in lines:
            vector=line.split()
            if vector[0] == label:

                c30pre=[int(element) for element in vector[1].split(',')]
                c30post=[int(element) for element in vector[2].split(',')]
                m30pre=[int(element) for element in vector[3].split(',')]
                m30post=[int(element) for element in vector[4].split(',')]

    xSignal = numpy.array([c30pre, c30post])
    xNoSignal = numpy.array([m30pre, m30post])
    
    return xSignal, xNoSignal
