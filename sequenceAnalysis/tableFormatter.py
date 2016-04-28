### this script builds the final table of significant variants

import sys,pickle
sys.path.append('lib')
import breseqReader,GATKreader,varscanReader

def annotationReader(sysName):

    '''
    this function reads info about the gene, obtained from xx
    '''

    found=False

    # reading annotation
    infoFile='annotation.2.txt'
    with open(infoFile,'r') as f:
        f.next()
        for line in f:
            vector=line.split('\t')
            if vector[1] == sysName:
                found=True
                if vector[3] != '':
                    geneName=vector[3]
                else:
                    geneName=sysName
                geneFunction=vector[4].replace('\n','').split(';')[0]

    # making sure annotation is retrieved
    if found == False:
        print 'annotation not found. exiting...'
        sys.exit()

    return geneName,geneFunction

def geneInfoRetriever(uLoc):

    '''
    this function retrieves gene name from a chromosome location
    '''

    found=False
    #print uLoc
    for variant in allVariants:
        putative=(variant[0],variant[2],variant[3])
        if uLoc == putative:
            found=True
            #print variant
            #print
            sysName=variant[7]
            if '_CDS' in sysName:
                sysName=sysName.split('_CDS')[0]
            if '_BY4741' in sysName:
                sysName=sysName.split('_BY4741')[0]
                
            mutation='|'.join((variant[4],variant[5]))

            effect=variant[11]
            if 'aaChange' in effect:
                effect=variant[11].split('_')[1]
            break

    if found == False:
        print uLoc
        print 'variant not recovered. exiting...'
        sys.exit()

    # converting sysName into geneName
    geneName,geneFunction=annotationReader(sysName)
    
    return geneName,geneFunction,mutation,effect

# 0. user defined variables
outputFile='formattedTable.305.txt'

experimentLabels={}
experimentLabels['exp1']='E2'
experimentLabels['exp2']='E4'
experimentLabels['exp3']='E6'
experimentLabels['exp4']='M2'
experimentLabels['exp5']='C1'

bases=['A','C','G','T','O']

# 1. recovering data
print 'recovering data...'

# 1.1. recovering changing variants...
print 
jar='changingVariants.305.pckl'
f=open(jar,'r')
[tested_experiments,tested_positions,tested_observedFrequencies,rejected_corrected,tested_statistics,pValues_corrected]=pickle.load(f)
f.close()

print '%s variants recovered.'%sum(rejected_corrected)

# 1.2. retrieving breseq variants
print 'retrieving breseq variants...'
tubes=['A2','B','D','E2','F','G','H2','I','J2','K','L','M']
breseqVariants=breseqReader.main(tubes)
GATKvariants=GATKreader.main(tubes)
varscanVariants=varscanReader.main(tubes)
allVariants=breseqVariants+GATKvariants+varscanVariants
print '%s variants recovered.'%len(allVariants)
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

        line2Write=[]

        # experiment
        element=tested_experiments[i]
        line2Write.append(experimentLabels[element])

        # type of variant,chr,position
        uLoc=tested_positions[i]
        for element in uLoc:
            line2Write.append(str(element))

        # gene name, gene function, variant frequency, mutation and effect
        geneName,geneFunction,mutation,effect=geneInfoRetriever(uLoc)
        line2Write.append(geneName)
        line2Write.append(geneFunction)
        line2Write.append(mutation)
        line2Write.append(effect)

        # frequency of variants
        tableOfFrequencies=tested_observedFrequencies[i]
        for genotype in tableOfFrequencies:
            for j in range(len(genotype)):
                baseFreq=genotype[j]
                base=bases[j]
                v=baseFreq/sum(genotype)
                printingValue=str('%s(%.3f)'%(base,v))
                #line2Write.append(printingValue)

        # computed frequencies
        if uLoc[0] == 'indel':
            finalGenotype=tableOfFrequencies[-1]
            dominantIndex=finalGenotype.index(max(finalGenotype))
        elif uLoc[0] == 'SNP':
            dominantBase=mutation.split('|')[1]
            if dominantBase == 'A':
                dominantIndex=0
            elif dominantBase == 'C':
                dominantIndex=1
            elif dominantBase == 'G':
                dominantIndex=2
            elif dominantBase == 'T':
                dominantIndex=3
            else:
                print 'error from computing dominant base. exiting...'
                sys.exit()            
        else:
            print 'error from computing frequencies. exiting...'
            sys.exit()

        for genotype in tableOfFrequencies:
            v=genotype[dominantIndex]/sum(genotype)
            printingValue=str('%.3f'%v)
            line2Write.append(printingValue)

        # p-value
        value=str('%.3e'%pValues_corrected[i])
        line2Write.append(value)

        #
        string2Write='\t'.join(line2Write)
        g.write('%s\n'%string2Write)

        #### make sure you check that the number of reads are more than xx

g.close()

print '... table formatted.'
print 'analysis completed'
