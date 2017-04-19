import os,sys,numpy
import sklearn,sklearn.decomposition,sklearn.manifold
import matplotlib,matplotlib.pyplot

matplotlib.rcParams.update({'font.size':18,'font.family':'Arial','xtick.labelsize':14,'ytick.labelsize':14})

# 0. user defined variables
expressionDataFile='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/cufflinks/allSamples/isoforms.fpkm_table'

# 1. reading the data
x=[]
theMarkers=[]
theColors=[]
theMFCs=[]

with open(expressionDataFile,'r') as f:

    header=f.readline()
    vectorHeader=header.split('\t')[1:]
    for i in range(len(vectorHeader)):
        
        x.append([])

        sampleName=vectorHeader[i]
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
            theMFCs.append(theColors[i])

    for line in f:
        vector=line.split('\t')[1:]
        for i in range(len(vector)):
            value=float(vector[i])
            x[i].append(value)

# 4. exploring the data
print('visualizing the data...')
original=numpy.array(x)

# 4.1. PCA of samples
print('running PCA...')
pcaMethod=sklearn.decomposition.PCA(n_components=5)
pcaObject=pcaMethod.fit(original)
new=pcaObject.transform(original)
explainedVar=pcaObject.explained_variance_ratio_
print('cumsum explained variance...')
print(numpy.cumsum(explainedVar))

for i in range(len(new)):
    matplotlib.pyplot.scatter(new[i,0],new[i,1],marker=theMarkers[i],color=theColors[i],facecolor=theMFCs[i])

matplotlib.pyplot.xlabel('PCA 1 ({0:.2f} var)'.format(explainedVar[0]))
matplotlib.pyplot.ylabel('PCA 2 ({0:.2f} var)'.format(explainedVar[1]))
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig('figure.pca.png')
matplotlib.pyplot.clf()
print()

sys.exit()

# 4.2. t-SNE of samples
print('running t-SNE...')
tSNE_Method=sklearn.manifold.TSNE(method='exact',verbose=1,init='pca')
tSNE_Object=tSNE_Method.fit(original)
new=tSNE_Object.fit_transform(original)

for i in range(len(new)):
    matplotlib.pyplot.scatter(new[i,0],new[i,1])
matplotlib.pyplot.savefig('figure.tSNE.png')
matplotlib.pyplot.clf()
print()
