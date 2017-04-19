import os,sys,numpy
import sklearn,sklearn.decomposition,sklearn.manifold
import matplotlib,matplotlib.pyplot

matplotlib.rcParams.update({'font.size':18,'font.family':'Arial','xtick.labelsize':14,'ytick.labelsize':14})

def caller(tag):

    '''
    this function calls kallisto
    '''

    sampleTag=tag.split('_L001_R1_001.paired.forward.fastq')[0]

    sampleFiles=['{}_L00{}_R1_001.paired.forward.fastq {}_L00{}_R2_001.paired.reverse.fastq'.format(fastqDir+sampleTag,i+1,fastqDir+sampleTag,i+1) for i in range(4)]
    sampleString=' '.join(sampleFiles)

    ### Tru-seq is --fr-firststrand (TopHat) or --rf-stranded (kallisto). First read reverse orientation, check http://onetipperday.sterding.com/2012/07/how-to-tell-which-library-type-to-use.html
    
    cmd='time kallisto quant -i {} -o {}{} --bias --plaintext -t 4 -b 100 --rf-stranded {}'.format(transcriptomeIndex,quantDir,sampleTag,sampleString)

    print()
    print(cmd)
    print()

    os.system(cmd)
    
    return None

### MAIN

# 0. user defined variables
fastqDir='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/cleanFASTQ/'
quantDir='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/kallisto/'
transcriptomeIndex='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/kallistoIndex/coding.idx'
resultsDir='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/expression/'

# 1. reading files
print('reading files...')

# 1.1. defining fastq files
items=os.listdir(fastqDir)
sortedTags=[element for element in items if '_L001_R1_001.paired.forward.fastq' in element]
sortedTags.sort()

# 2. processing
#print('processing files...')
#for tag in sortedTags:
#    caller(tag)
#print('...quantification done.')

# 3. generating full expression matrix
print('generating expression matrix file...')

# 3.1. reading the genes
genes=[]
oneFile=quantDir+sortedTags[0].split('_L')[0]+'/abundance.tsv'
f=open(oneFile,'r')
next(f)
for line in f:
    vector=line.split()
    geneName=vector[0]
    genes.append(geneName)
f.close()
genes.sort()

# 3.2. reading expression
expression={}
for element in sortedTags:
    tag=element.split('_L')[0]
    if tag not in expression.keys():
        expression[tag]={}

    workingFile=quantDir+tag+'/abundance.tsv'
    f=open(workingFile,'r')
    next(f)
    for line in f:
        vector=line.split()
        geneName=vector[0]
        abundance=float(vector[-1])
        expression[tag][geneName]=abundance
    f.close()

# 3.3. writing expression matrix
expressionFile=resultsDir+'expressionMatrix.kallisto.txt'
conditionNames=list(expression.keys())
conditionNames.sort()

g=open(expressionFile,'w')

# header
g.write('\t')
for i in range(len(conditionNames)):
    g.write('{}\t'.format(conditionNames[i]))
g.write('\n')

# body
for i in range(len(genes)):
    g.write('{}\t'.format(genes[i]))
    for j in range(len(conditionNames)):
        value=expression[conditionNames[j]][genes[i]]
        g.write('{}\t'.format(value))        
    g.write('\n')
    
g.close()

# 4. exploring the data
print('visualizing the data...')

theMarkers=[]
theColors=[]
theMFCs=[]

x=[]
for i in range(len(conditionNames)):
    if 'n300-C' not in conditionNames[i]:
        sample=[]
        for j in range(len(genes)):
            value=expression[conditionNames[i]][genes[j]]
            sample.append(value)
        x.append(sample)

        sampleName=conditionNames[i]
        # tubes
        if 'BR1' in sampleName or 'n300' in sampleName:
            theMarkers.append('o')
        elif 'BR2' in sampleName or 'n50' in sampleName:
            theMarkers.append('s')
        elif 'BR3' in sampleName or 'n180' in sampleName:
            theMarkers.append('^')
        else:
            print('error a')
            sys.exit()

        # treatments
        if '-A' in sampleName or '-B' in sampleName or '-D' in sampleName:
            theColors.append('black')
        elif '-C' in sampleName:
            theColors.append('red')
        elif '-E' in sampleName:
            theColors.append('green')
        elif '-F' in sampleName:
            theColors.append('blue')

        # evolution
        if 'BR' in sampleName:
            theMFCs.append('white')
        else:
            theMFCs.append(theColors[-1])

experiment=numpy.array(x)

# 4.1. PCA of samples
print('running PCA...')
pcaMethod=sklearn.decomposition.PCA(n_components=5)
pcaObject=pcaMethod.fit(experiment)
new=pcaObject.transform(experiment)
explainedVar=pcaObject.explained_variance_ratio_
print('cumsum explained variance...')
print(numpy.cumsum(explainedVar))

for i in range(len(new)):
    print(conditionNames[i],new[i,0])
    matplotlib.pyplot.scatter(new[i,0],new[i,1],marker=theMarkers[i],color=theColors[i],facecolor=theMFCs[i])

matplotlib.pyplot.xlabel('PCA 1 ({0:.2f} var)'.format(explainedVar[0]))
matplotlib.pyplot.ylabel('PCA 2 ({0:.2f} var)'.format(explainedVar[1]))
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig('figure.pca.png')
matplotlib.pyplot.clf()

# 4.2. t-SNE of samples
print('running t-SNE...')
tSNE_Method=sklearn.manifold.TSNE(method='exact',verbose=1,init='pca')
tSNE_Object=tSNE_Method.fit(experiment)
new=tSNE_Object.fit_transform(experiment)

for i in range(len(new)):
    matplotlib.pyplot.scatter(new[i,0],new[i,1],s=60)
matplotlib.pyplot.savefig('figure.tSNE.png')
matplotlib.pyplot.clf()
print()
