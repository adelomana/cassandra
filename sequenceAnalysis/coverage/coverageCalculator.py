# this script computes a coverage graph for each sample

import numpy,sys,subprocess,pickle,os

import matplotlib
import matplotlib.pyplot

import multiprocessing
import multiprocessing.pool

def coverageComputer(tube):

    '''
    this function computes the coverage over all chromosomes in a bam file
    '''
    
    bamfile=path2datafiles+tube+'/data/reference.bam'
    print('working with',bamfile,'...')

    # computing the coverage
    chromosomeNames=list(chromosomes.keys())
    chromosomeNames.sort()

    for chromosome in chromosomeNames:
        
        bins=numpy.arange(size,chromosomes[chromosome],size)
        
        for i in range(len(bins)-1):
            loca=int(bins[i])
            locb=int(bins[i+1])
            pos=chromosome+':'+str(loca)+'-'+str(locb)

            command=['samtools','mpileup','-r',pos,bamfile]

            outFile=scratchDir+'samtoolsOutput/'+tube+'.'+pos+'.out.txt'
            errFile=scratchDir+'samtoolsError/'+tube+'.'+pos+'.err.txt'
            stdout = open(outFile,"w")
            stderr = open(errFile,"w")

            subprocess.call(command,stdout=stdout,stderr=stderr)

            stdout.close()
            stderr.close()

    return None

def coverageReader(tubes):

    '''
    this function build plots for the coverage
    '''
    
    coverage={}
    
    # entering a parallel word
    print('entering a parallel world...')
    hydra=multiprocessing.pool.Pool(4)
    output=hydra.map(tubeCoverageReader,tubes)

    for i in range(len(output)):
        coverage[tubes[i]]=output[i]

    return coverage

def tubeCoverageReader(tube):

    '''
    this function retrieves the coverage for each tube
    '''

    finalCoverage=[]
    chromosomeNames=list(chromosomes.keys())
    chromosomeNames.sort()

    for chromosome in chromosomeNames:

        bins=numpy.arange(size,chromosomes[chromosome],size)
        
        for i in range(len(bins)-1):
            loca=int(bins[i])
            locb=int(bins[i+1])
            pos=chromosome+':'+str(loca)+'-'+str(locb)
            outFile=scratchDir+'samtoolsOutput/'+tube+'.'+pos+'.out.txt'

            # taking the mean coverage for that window 
            average=[]
            with open(outFile,'r') as f:
                for line in f:
                    vector=line.split('\t')
                    reads=int(vector[3])
                    average.append(reads)
            theAverage=numpy.median(average)
            finalCoverage.append(theAverage)

    return finalCoverage

# 0. user defined variables
path2datafiles='/Volumes/omics4tb/alomana/projects/ap/seqsFromGates/results/toronto/'
scratchDir='/Users/alomana/scratch/'

experiments=['exp1','exp2','exp3','exp4','exp5']
tubeCorrespondance={}
tubeCorrespondance['exp1']=['A2','B','D']
tubeCorrespondance['exp2']=['E2','F','G']
tubeCorrespondance['exp3']=['H2','I']
tubeCorrespondance['exp4']=['J2','K']
tubeCorrespondance['exp5']=['L','M']

tubes=[]
for experiment in experiments:
    for tube in tubeCorrespondance[experiment]:
        tubes.append(tube)
tubes.sort()

size=1e4 # size of the stretch of DNA to compute coverage

chromosomes={}
chromosomes['chr01']=230222
chromosomes['chr02']=813185
chromosomes['chr03']=305936
chromosomes['chr04']=1531932
chromosomes['chr05']=575777
chromosomes['chr06']=270161
chromosomes['chr07']=1090940
chromosomes['chr08']=562641
chromosomes['chr09']=439891
chromosomes['chr10']=745751
chromosomes['chr11']=666818
chromosomes['chr12']=1075778
chromosomes['chr13']=924428
chromosomes['chr14']=784331
chromosomes['chr15']=1091101
chromosomes['chr16']=948066
#chromosomes['chr17']=85781

chromosomeNames=list(chromosomes.keys())
chromosomeNames.sort()

# 1. compute coverage
for experiment in experiments:
    print('working with experiment %s...'%experiment)
    for tube in tubeCorrespondance[experiment]:
        coverageComputer(tube)
        
# 2. pickling the computed coverage: reading files and storing as pickle object
coverage=coverageReader(tubes)
jar='coverage.final.pckl'
f=open(jar,'wb')
pickle.dump(coverage,f)
f.close()

# 3. plot coverage
f=open(jar,'r')
coverage=pickle.load(f)
f.close()
sys.exit()

# 3.1. plotting raw coverage
currentColor='blue'
for tube in tubes:
    for chromosome in chromosomes:
        values=coverage[tube][chromosome]
        print(tube,chromosome,values)
        sys.exit()
    
        if currentColor == 'blue':
            currentColor='red'
        else:
            currentColor='blue'

        theColors.append(currentColor)    

# 3.2. plotting relative coverage

# 3.3. plotting relative coverage normalized by empirical expectations
