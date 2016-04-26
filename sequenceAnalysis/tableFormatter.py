### this script builds the final table of significant variants

import sys,pickle

# 0. user defined variables
outputFile='formattedTable.txt'

# 1. recovering data
print 'recovering data...'

jar='changingVariants.pckl'
f=open(jar,'r')
[tested_experiments,tested_positions,tested_observedFrequencies,rejected_corrected,tested_statistics,pValues_corrected]=pickle.load(f)
f.close()

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
header=['experiment','variantType','chr','position']
stringHeader='\t'.join(header)
g.write(stringHeader)
g.write('\n')

for i in range(len(pValues_corrected)):
    if rejected_corrected[i] == True:
        
        # 2. formatting the table with the following fields

        # experiment
        element=tested_experiments[i]
        g.write(element)
        g.write('\t')

        # type of variant,chr,position
        (a,b,c)=tested_positions[i]
        print a,b,c
        sys.exit()

        # frequency of variants
        tableOfFrequencies=vector[3]
        print list(tableOfFrequencies)

        # gene name

        # p-value

        # gene function

        # effect

        #
        g.write('\n')
        sys.exit()

g.close()
