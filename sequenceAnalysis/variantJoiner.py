### this script recovers all mutations from 3 different callers

import sys
sys.path.append('lib')
import breseqReader,GATKreader,varscanReader

def isAnnotationVariant(variant,filtredVariants1):

    flag=False
    toMatch=[variant[0],variant[2],variant[3],variant[-2]] # vartype,chr,pos,caller
    foundSet=[]

    for fv in filtredVariants1:

        putative=[fv[0],fv[2],fv[3],fv[-2]]
        putativeFreq=fv[6]

        if toMatch == putative and putativeFreq >= annotationThreshold:
            tube=fv[1]
            if tube not in foundSet:
                foundSet.append(tube)

    if len(foundSet) == 12:
        flag=True
    if len(foundSet) > 12:
        print variant
        count=0
        for element in foundSet:
            count=count+1
            print '\t',count,'\t',element
        print foundSet,len(foundSet)
        print 'error from isAnnotationVariant. Exiting...'
        sys.exit()

    return flag

##### MAIN

# 0. defining general variables
tubes=['A2','B','D','E2','F','G','H2','I','J2','K','L','M']
resolution=0.01
annotationThreshold=1.-resolution

# 1. retrieving variants
print 'retrieving the variants...'

# 1.1. retrieving breseq variants
print '\t retrieving breseq variants...'
breseqVariants=breseqReader.main(tubes)
print '\t %s variants detected.\n'%len(breseqVariants)

# 1.2. retrieving GATK variants
print '\t retrieving GATK variants...'
GATKvariants=GATKreader.main(tubes)
print '\t %s variants detected.\n'%len(GATKvariants)

# 1.3. retrieving varscan variants
print '\t retrieving varscan variants...'
varscanVariants=varscanReader.main(tubes)
print '\t %s variants detected.\n'%len(varscanVariants)

# 2. filtering variants
print 'filtering variants...'
variants=breseqVariants+GATKvariants+varscanVariants

print 'working with a full set of %s variants.'%len(variants)

# 2.1. remove low frequency variants (v < resolution)
print '\n\t removing low frequency variants (v < %s)...'%('%.3f'%resolution)
filtredVariants1=[]
for variant in variants:
    freq=variant[6]
    if freq >= resolution: 
        filtredVariants1.append(variant)
print '\t %s with substantial frequency.'%len(filtredVariants1)

# 2.2. remove annotation/ancestral variants (v_all > annotationThreshold)
print '\n\t removing annotation variants (v_all > %s)...'%('%.3f'%annotationThreshold)
filtredVariants2=[]
for variant in filtredVariants1:
    flag=isAnnotationVariant(variant,filtredVariants1)
    if flag == False:
        filtredVariants2.append(variant)
print '\t %s non annotation variants.'%len(filtredVariants2)

# 2.3. removing variants that are not in at least two data sets
filtredVariants3=[]

# create a list of all positions
locations=[]
for variant in filtredVariants2:
    loc=variant[:4]
    locations.append(loc)

# create a list of positions that have at least one counts. make it unique list
selectedLocations=[]
for location in locations:
    if locations.count(location) >= 1:
        selectedLocations.append(location)
uniqueSelectedLocations=list(set(selectedLocations))

print 'detected %s unique variant from at least 1 callers...'%len(uniqueSelectedLocations)

# create a list with variants of the unique locations
filtredVariants3=[]
for location in uniqueSelectedLocations:
    for variant in filtredVariants2:
        if location == variant[:4]:
            filtredVariants3.append(variant)
print 'about to write %s variants into a file...'%len(filtredVariants3)

# 3. saving the biologically relevant variants
print 'saving to a file...'
outputFile='joinedVariants.txt'
g=open(outputFile,'w')
for variant in filtredVariants3:
    for term in variant:
        g.write('%s\t'%term)
    g.write('\n')
g.close()

print '... analysis completed.'
