import sys,math,subprocess,numpy,pickle,os
import multiprocessing,multiprocessing.pool
import matplotlib,matplotlib.pyplot

def coverageComputer(tube):

    '''
    this function calls samtools to perform coverage calculation, reads the obtained files, computes the median and returns a single array of values according to geneBins
    '''
    
    localCoverage=[]
    hydra=multiprocessing.pool.Pool(numberOfThreads)
    

    tasks=[[gene,tube] for gene in allGenesSorted]
    localCoverage=hydra.map(singleGeneCoverageComputer,tasks)
                
    return localCoverage

def geneDefiner():

    '''
    this function returns the genes as a dictionary
    '''

    geneLocations={}
    geneNames={}
    
    with open(gffFile,'r') as f:
        for i in range(17):
            next(f)
        for line in f:
            v=line.split('\t')
            if len(v) > 2:
                if v[2] == 'gene':
                    geneName=v[8].split(';')[0].split('ID=')[1].split('_B')[0]
                    chromo=v[0]
                    start=int(v[3])
                    stop=int(v[4])

                    if chromo != 'chr17':
                        geneLocations[geneName]=[chromo,start,stop]
                        
                        if chromo not in geneNames.keys():
                            geneNames[chromo]=[geneName]
                        else:
                            geneNames[chromo].append(geneName)
                    
    return geneLocations,geneNames

def singleGeneCoverageComputer(task):

    '''
    this function computes the coverage for a single gene at a single tube
    '''

    gene=task[0]
    tube=task[1]

    bamfile=path2datafiles+tube+'/data/reference.bam'
    
    chromosome=geneLocations[gene][0]
    loca=geneLocations[gene][1]
    locb=geneLocations[gene][2]
    pos=chromosome+':'+str(loca)+'-'+str(locb)

    command=['samtools','mpileup','-r',pos,bamfile]

    outFile=scratchDir+'samtoolsOutput/'+tube+'.'+gene+'.out.txt'
    errFile=scratchDir+'samtoolsError/'+tube+'.'+gene+'.err.txt'
    
    stdout = open(outFile,"w")
    stderr = open(errFile,"w")

    subprocess.call(command,stdout=stdout,stderr=stderr)

    stdout.close()
    stderr.close()

    # taking the median coverage for that gene 
    average=[]
    with open(outFile,'r') as f:
        for line in f:
            vector=line.split('\t')
            reads=int(vector[3])
            average.append(reads)
    coverage=numpy.median(average)

    # removing files
    os.remove(outFile)
    os.remove(errFile)

    # final message
    #print('computed coverage {} for tube {} gene {}'.format(coverage,tube,gene))

    return coverage

def trajectoriesPlotter3(localTubes):

    '''
    this function builds rich figures about coverage
    '''

    # defining pseudo legend
    localText=['E2 (n=0)','E2 (AP+)','E2 (AP-)']

    # defining y
    y1=numpy.log2(numpy.array(correctedCoverage[localTubes[0]]))
    y2=numpy.log2(numpy.array(correctedCoverage[localTubes[1]]))
    y3=numpy.log2(numpy.array(correctedCoverage[localTubes[2]]))

    # defining x and colors
    print(len(y1))
    print(len(theColors))
    x=[i for i in range(len(theColors))]
              
    
    # plotting subfigures
    matplotlib.pyplot.subplot(311)
    matplotlib.pyplot.scatter(x,y1,marker='.',color=theColors)
    matplotlib.pyplot.xlim([-0.025*len(x),len(x)+0.025*len(x)])
    matplotlib.pyplot.ylim([-3,3])
    matplotlib.pyplot.plot([0,max(x)],[1,1],'--r',lw=2)
    matplotlib.pyplot.plot([0,max(x)],[-1,-1],'--b',lw=2)
    matplotlib.pyplot.xticks([])
    matplotlib.pyplot.yticks([-2,-1,0,1,2])
    
    matplotlib.pyplot.subplot(312)
    matplotlib.pyplot.scatter(x,y2,marker='.',color=theColors)
    matplotlib.pyplot.xlim([-0.025*len(x),len(x)+0.025*len(x)])
    matplotlib.pyplot.ylim([-3,3])
    matplotlib.pyplot.plot([0,max(x)],[1,1],'--r',lw=2)
    matplotlib.pyplot.plot([0,max(x)],[-1,-1],'--b',lw=2)
    matplotlib.pyplot.xticks([])
    matplotlib.pyplot.yticks([-2,-1,0,1,2])
    matplotlib.pyplot.ylabel('Coverage')
    
    matplotlib.pyplot.subplot(313)
    matplotlib.pyplot.scatter(x,y3,marker='.',color=theColors)
    matplotlib.pyplot.xlim([-0.025*len(x),len(x)+0.025*len(x)])
    matplotlib.pyplot.ylim([-3,3])
    matplotlib.pyplot.plot([0,max(x)],[1,1],'--r',lw=2)
    matplotlib.pyplot.plot([0,max(x)],[-1,-1],'--b',lw=2)
    matplotlib.pyplot.yticks([-2,-1,0,1,2])
    
    # final arrangements
    matplotlib.pyplot.figtext(0.85,0.325,localText[2])
    matplotlib.pyplot.figtext(0.85,0.625,localText[1])
    matplotlib.pyplot.figtext(0.85,0.925,localText[0])
    
    matplotlib.pyplot.xlabel('Chromosome')

    #pos=0
    #xtickPositions=[]
    #for chromosome in chromosomeNames:
    #    bins=numpy.arange(size,chromosomes[chromosome],size)
    #    for i in range(len(bins)-1):
    #        pos=pos+1
    #    xtickPositions.append(pos-len(bins)/2)
    #minimalLabels=[str(i+1) for i in range(len(chromosomeNames))]

    #matplotlib.pyplot.xticks(xtickPositions,minimalLabels)
    #$for i in range(len(matplotlib.pyplot.gca().get_xticklabels())):
    #if i%2 == 0:
    #        matplotlib.pyplot.gca().get_xticklabels()[i].set_color('orange')
    #    else:
    #        matplotlib.pyplot.gca().get_xticklabels()[i].set_color('green')

    matplotlib.pyplot.tight_layout()
    figureFile=figuresDir+'trajectories.perGene.{}.pdf'.format('.'.join(localTubes))
    matplotlib.pyplot.savefig(figureFile)
    matplotlib.pyplot.clf()
    sys.exit()

    return None

###
### MAIN
###

# 0. user defined variables
gffFile='/proj/omics4tb/alomana/projects/ap/seqsFromGates/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff'
path2datafiles='/proj/omics4tb/alomana/projects/ap/seqsFromGates/results/toronto/'
scratchDir='/proj/omics4tb/alomana/scratch/'
figuresDir='figures/'

numberOfThreads=64

tubeCorrespondance={}
experiments=['exp1','exp2','exp3','exp4','exp5']
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

# 1. define the set of genes for which average coverage will be computed

# 1.1. define gene positions
geneLocations,geneNames=geneDefiner()

# 1.2. define groups of genes
allGenesSorted=[]
chromosomeNames=list(geneNames.keys())
chromosomeNames.sort()

for chromo in chromosomeNames:
    geneStarts={}
    for gene in geneNames[chromo]:
        geneStarts[gene]=geneLocations[gene][1]
    orderedGenes=sorted(geneStarts,key=geneStarts.__getitem__)
    for element in orderedGenes:
        allGenesSorted.append(element)
        
# 2. compute coverage
coverage={}
for tube in tubes:
    localCoverage=coverageComputer(tube)
    coverage[tube]=localCoverage

# 3. writing or reading coverage
print('pickling or unpickling data...')
jar='coverage.perSingleGene.pckl'

f=open(jar,'wb')
pickle.dump(coverage,f)
f.close()

sys.exit()

f=open(jar,'rb')
coverage=pickle.load(f)
f.close()

# 4. correcting coverage
# 4.1. computing fold-change relative to median coverage
relativeCoverage={}
for tube in tubes:
    relative=coverage[tube]/numpy.median(coverage[tube])
    relativeCoverage[tube]=relative

# 4.2. computing fold-change relative coverage to the empirical expectation
correctedCoverage={}

values=[]
for tube in tubes:
    values.append(relativeCoverage[tube])
v=numpy.array(values)
expectedCoverage=numpy.mean(v,axis=0)

for tube in tubes:
    corrected=relativeCoverage[tube]/expectedCoverage
    correctedCoverage[tube]=corrected

# 4. plot figure
print('plotting figures...')
trajectoriesPlotter3(['A2','B','D'])
