### this script reads joined variants, sort them by trajectory and checks that frequency changes are significant based on FDR corrected test on the number of reads supporting alternative variant

import sys,os,subprocess,re,numpy,pickle
import scipy.stats,statsmodels.sandbox.stats.multicomp

def baseRetriever(tube,uloc):

    '''
    this function uses breseq to recover bases called at BAM file specific position
    '''

    #! qualityThreshold=0
    pos=uloc[1]+':'+str(uloc[2])+'-'+str(uloc[2])
    label=tube+pos
    
    bamfile=path2datafiles+tube+'/data/reference.bam'
    outFile='base.calling.files/%s.out.txt'%label
    errFile='base.calling.files/%s.err.txt'%label

    stdout = open(outFile,"w")
    stderr = open(errFile,"w")

    command=['samtools','mpileup','-r',pos,bamfile]
    subprocess.call(command,stdout=stdout,stderr=stderr)

    # retrieving bases and qualities
    f=open(outFile,'r')
    line=f.readline()
    f.close()

    if line == '':
        print 'WARNING: tube %s at position %s has no mapping reads. Returning empty genotype...'%(tube,uloc)
        expectedNumberOfBases=1
        rawBases='*'
        qualities='!'
    else:
        vector=line.split()
        expectedNumberOfBases=int(vector[3])
        if expectedNumberOfBases == 0:
            print 'WARNING: tube %s at position %s has 0 mapping reads. Returning empty genotype...'%(tube,uloc)
            rawBases=''
            qualities=''
        else:
            rawBases=vector[4]
            qualities=vector[5]

    treatedBases=rawBases.replace('$','')

    indexes=[m.start() for m in re.finditer('\^',treatedBases)]
    strings2remove=[]
    for index in indexes:
        string2remove='^'+treatedBases[index+1]
        strings2remove.append(string2remove)
    for element in strings2remove:
        treatedBases=treatedBases.replace(element,'')

    treatedBases=treatedBases.replace('*','O')
    
    treatedBases=treatedBases.replace('+','/')
    treatedBases=treatedBases.replace('-','/')

    splittedBases=treatedBases.split('/')

    for i in range(len(splittedBases)-1):
        toTrimList=re.findall(r'\d+', splittedBases[i+1])
        if len(toTrimList) != 1:
            print len(toTrimList)
            print 'problem finding integers in splittedBases variable. Exiting...'
            sys.exit()
        toTrim=int(toTrimList[0])
        additionalTrimming=len(toTrimList[0])
        splittedBases[i+1]=splittedBases[i+1][toTrim+additionalTrimming:]

    cleanBases=''.join(splittedBases)

    if expectedNumberOfBases != len(cleanBases):
        print expectedNumberOfBases,len(cleanBases)
        print 'expected number of bases and reported number of bases do not match. Exiting...'
        sys.exit()

    if len(cleanBases) != len(qualities):
        print len(cleanBases),len(qualities)
        print 'number of bases and number of qualities do not match. Exiting...'
        sys.exit()

    # computing the statistical abundance of each base, considering read quality
    genotype={}
    genotype['A']=0.
    genotype['C']=0.
    genotype['G']=0.
    genotype['T']=0.
    genotype['O']=0.
    
    for i in range(len(cleanBases)):

        score=ord(qualities[i])-33
        error=10**(-score/10.)
        p=1.-error

        base=cleanBases[i].upper()
        genotype[base]=genotype[base]+p

    return genotype

# 0. user defined variables
path2datafiles='/Users/alomana/projects/ap/seqs/results/toronto/'
inputFile='joinedVariants.23626.txt'

experiments=['exp1','exp2','exp3','exp4','exp5']
tubeCorrespondance={}
tubeCorrespondance['exp1']=['A2','B','D']
tubeCorrespondance['exp2']=['E2','F','G']
tubeCorrespondance['exp3']=['H2','I']
tubeCorrespondance['exp4']=['J2','K']
tubeCorrespondance['exp5']=['L','M']

epsilon=1e-3

# 1. reading variants
print 'reading the input...'
variants=[]
with open(inputFile,'r') as f:
    for line in f:
        vector=line.split('\t')
        x=[]
        for element in vector:
            x.append(element)
        x[3]=int(x[3])
        x[6]=float(x[6])
        x[7]=x[7].replace('_BY4741','')
        x[7]=x[7].replace('_CDS','')
        x.pop()
        t=tuple(x)
        variants.append(t)

print '%s variant calls detected.'%len(variants)

# 2. obtaining a list of trajectories
print 'testing changes in variant frequencies...'

tested_experiments=[]
tested_positions=[]
tested_observedFrequencies=[]
tested_statistics=[]
tested_pValues=[]

for experiment in experiments:

    print 'working with experiment %s...'%experiment

    # retrieve all mutation positions for that particular trajectory
    allLocations=[]
    for variant in variants:
        tube=variant[1]
        loc=(variant[0],variant[2],variant[3])
        if tube in tubeCorrespondance[experiment]:
            allLocations.append(loc)
    uniqueLocations=list(set(allLocations))
    
    #  for each variant, define if there is a change in frequency and associate a test
    for uloc in uniqueLocations:
        observed=[]
        for tube in tubeCorrespondance[experiment]:

            # for each uloc and tube, retrieve frequency and quality of called bases
            genotype=baseRetriever(tube,uloc)
            o=[genotype['A'],genotype['C'],genotype['G'],genotype['T'],genotype['O']]
            observed.append(o)
            
        # performing a Chi-square test of homogeneity
        table=numpy.array(observed)+epsilon
        statistic,pValue,tempo1,tempo2=scipy.stats.chi2_contingency(table,lambda_="log-likelihood")

        tested_experiments.append(experiment)
        tested_positions.append(uloc)
        tested_observedFrequencies.append(observed)
        tested_statistics.append(statistic)
        tested_pValues.append(pValue)


# 4. obtain table of significances corrected by FDR
print 'correcting for false discovery rate for %s tests...'%len(tested_pValues)

rejected_corrected,pValues_corrected,tempo1,tempo2=statsmodels.sandbox.stats.multicomp.multipletests(tested_pValues,method='bonferroni')
rejected_adjusted,pValues_adjusted,tempo1,tempo2=statsmodels.sandbox.stats.multicomp.multipletests(tested_pValues,method='fdr_bh')

print 'rejected hypotheses, Bonferroni corrected or FDR-BH adjusted respectively:',sum(rejected_corrected),sum(rejected_adjusted)

print '%s variants have frequency difference.'%sum(rejected_corrected)

# 4.1. saving variables of interest for downstream analysis as a pickled object
jar='changingVariants.%s.pckl'%str(sum(rejected_corrected))
f=open(jar,'w')
pickle.dump([tested_experiments,tested_positions,tested_observedFrequencies,rejected_corrected,tested_statistics,pValues_corrected],f)
f.close()

print '... analysis completed.'
