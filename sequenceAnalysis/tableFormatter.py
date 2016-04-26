### this script builds the final table of significant variants

import sys,pickle
sys.path.append('lib')
import breseqReader

def geneNameRetriever(uLoc):

    '''
    this function retrieves gene name from a chromosome location
    '''

    print uLoc
    print breseqVariants

    return geneName

# 0. user defined variables
outputFile='formattedTable.txt'

experiments=['exp5','exp4','exp1','exp2','exp3']
experimentLabels={}
experimentLabels['exp1']='E2'
experimentLabels['exp2']='E4'
experimentLabels['exp3']='E6'
experimentLabels['exp4']='M2'
experimentLabels['exp5']='C1'

tubes=['A2','B','D','E2','F','G','H2','I','J2','K','L','M']

# 1. recovering data
print 'recovering data...'

# 1.1. recovering changing variants...
print 
jar='changingVariants.pckl'
f=open(jar,'r')
[tested_experiments,tested_positions,tested_observedFrequencies,rejected_corrected,tested_statistics,pValues_corrected]=pickle.load(f)
f.close()

# 1.2. retrieving breseq variants
print 'retrieving breseq variants...'
breseqVariants=breseqReader.main(tubes)

print 'data recovered.'
print

# 2. performing the formatting
print 'formatting table...'

'''
experiment
type of variant
chr
position
frequency variants
gene name
p-value
gene function
effect
'''

g=open(outputFile,'w')

for i in range(len(pValues_corrected)):
    if rejected_corrected[i] == True:
        
        # 2. formatting the table with the following fields

        # experiment
        element=tested_experiments[i]
        g.write(experimentLabels[element])
        g.write('\t')

        # type of variant,chr,position
        uLoc=tested_positions[i]
        for element in uLoc:
            g.write(str(element))
            g.write('\t')

        # frequency of variants
        tableOfFrequencies=tested_observedFrequencies[i]
        for genotype in tableOfFrequencies:
            for base in genotype:
                v=base/sum(genotype)
                printingValue=str('%.3f'%v)
                g.write(printingValue)
                g.write('\t')

        # gene name
        geneName=geneNameRetriever(uLoc)
        g.write(geneName)
        g.write('\t')

        # p-value
        value=str('%.3e'%pValues_corrected[i])
        g.write(value)
        g.write('\t')

        # gene function

        # effect

        #
        g.write('\n')
        sys.exit()

g.close()

print '... table formatted.'
print 'analysis completed'
