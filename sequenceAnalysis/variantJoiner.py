### reads the mutations of breseq, GATK and varscan. It selects for 0.2 to call it a mutation. Quantifies how many mutations are called by each one (bar graph) at the level of SNPs and indels. Prints a list with all the variants by priority (based on number of callers recovering the variant.

import sys
import breseqReader,GATKreader,varscanReader

def isIncreasingVariant(variant,filtredVariants2,variants):

    listOfSelectedVariants=[]
    tubeCorrespondance={}
    tubeCorrespondance['exp1']=['A2','B','D']
    tubeCorrespondance['exp2']=['E2','F','G']
    tubeCorrespondance['exp3']=['H2','I']
    tubeCorrespondance['exp4']=['J2','K']
    tubeCorrespondance['exp5']=['L','M']
    variantTube=variant[1]
    variantFreq=variant[6]
    positiveTubes=[tubeCorrespondance[element][1] for element in tubeCorrespondance.keys()]
    lostTubes=['D','G']

    # 1. recovering variants increasing at AP+
    #print 'checking variants increasing in AP+...'
    
    # check that is a variant in AP+
    if variantTube in positiveTubes:
        #print variant
        # find the n0 tube
        n0tube=''
        for key in tubeCorrespondance.keys():
            if variantTube in tubeCorrespondance[key]:
                n0tube=tubeCorrespondance[key][0]
                workingTrajectory=key
        if n0tube == '':
            print 'error from isIncreasingVariant at n0Tube'
            sys.exit()
        #print n0tube
        # find the mutation at n0
        found=False
        toMatch=[variant[0],n0tube,variant[2],variant[3],variant[4],variant[5],variant[-2]] # vartype,tube,chr,pos,ref,alt,caller
        for putative in variants: # it should be variants, this is important to check that there is truly an increase of 0.2
            putativeMatch=[putative[0],putative[1],putative[2],putative[3],putative[4],putative[5],putative[-2]]
            if toMatch == putativeMatch:
                #print 'almost found but need to check freq',putativeMatch
                #print putative
                #print variant
                diff=variantFreq-putative[6] # putative[6] is the freq at n0
                #print diff,variantFreq,putative[6]
                if isinstance(diff, float) == False:
                    print 'error'
                    sys.exit()
                if diff < increaseThreshold:
                    found=True
        #print found

        # recover the variants of the experiment if no variant is found at n0
        if found == False and variantFreq > increaseThreshold:
            possibleTubes=tubeCorrespondance[workingTrajectory]
            #print possibleTubes
            toMatch=[variant[0],variant[2],variant[3],variant[4],variant[5],variant[-2]] # vartype,chr,pos,ref,alt,caller
            for putative in filtredVariants2:
                putativeMatch=[putative[0],putative[2],putative[3],putative[4],putative[5],putative[-2]]
                if toMatch == putativeMatch:
                    if putative[1] in possibleTubes:
                        listOfSelectedVariants.append(putative)
                        #print 'appending...'
                        #print putative

    # 2. recovering variants changing between AP+ and AP-: if there is an increase ==> general resistance; if decrease ==> causal of lost of AP
    #print 'checking variants changing between AP+ and AP-...'
    # check that is a variant in AP lost
    if variantTube in lostTubes:

        # find the previous tube
        if variantTube == 'D':
            previousTube='B'
            workingTrajectory='exp1'
        elif variantTube == 'G':
            previousTube='F'
            workingTrajectory='exp2'
        else:
            print 'error from isIncreasingVariant at previous tube recovering'
        #print '\t second',previousTube
        # find the mutation in that previous tube. define if it increased or decreased increaseThreshold.
        toRetrieve=False
        toMatch=[variant[0],previousTube,variant[2],variant[3],variant[4],variant[5],variant[-2]] # vartype,tube,chr,pos,ref,alt,caller
        for putative in filtredVariants2:
            putativeMatch=[putative[0],putative[1],putative[2],putative[3],putative[4],putative[5],putative[-2]]
            if toMatch == putativeMatch:
                #print '\t second',' almost found but need to check freq',putativeMatch
                #print '\t second',putative
                #print '\t second',variant
                diff=abs(variantFreq-putative[6]) # putative[6] is the freq at the previous tube
                if diff > increaseThreshold:
                    toRetrieve=True
        #print '***! second',toRetrieve

        # recover all variants of the experiment if they increased or decreased 0.20.
        if toRetrieve == True:
            possibleTubes=tubeCorrespondance[workingTrajectory]
            #print '***! second',possibleTubes
            toMatch=[variant[0],variant[2],variant[3],variant[4],variant[5],variant[-2]] # vartype,chr,pos,ref,alt,caller
            for putative in filtredVariants2:
                putativeMatch=[putative[0],putative[2],putative[3],putative[4],putative[5],putative[-2]]
                if toMatch == putativeMatch:
                    if putative[1] in possibleTubes:
                        listOfSelectedVariants.append(putative)
                        #print '***!',putative
       
    #print

    return listOfSelectedVariants

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

# create a list of positions that have at least two counts. make it unique list
selectedLocations=[]
for location in locations:
    if locations.count(location) >= 2:
        selectedLocations.append(location)
uniqueSelectedLocations=list(set(selectedLocations))

print 'detected %s unique variant from at least 2 callers...'%len(uniqueSelectedLocations)

# create a list with variants of the
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
