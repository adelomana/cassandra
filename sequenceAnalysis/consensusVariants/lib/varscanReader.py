import os,sys

def indelsReader(tubes,path2Samples):

    detectedVariants=[]

    for tube in tubes:
        dataFile=path2Samples+'varscanResultsAnnotated_%s_indels.vcf'%tube

        with open(dataFile,'r') as f:
            f.next()
            f.next()
            f.next()
            f.next()
            f.next()
            for line in f:
                vector=line.split('\t')

                # vartype
                vartype='indel'

                # chr, chr, pos, ref, alt,freq
                chr=vector[0]
                pos=int(vector[1])
                ref=vector[2]
                alt=vector[-1].replace('\n','')
                freq=float(vector[7].split(';')[0].replace('%',''))/100.

                # keeping a minimalistic annotation
                sysName=vector[7].split('|')[3]
                standName=''
                description=''

                # caller and functional effect
                caller='varscan'
                functionalEffect=vector[7].split('|')[1]

                variant=(vartype,tube,chr,pos,ref,alt,freq,sysName,standName,description,caller,functionalEffect)
                detectedVariants.append(variant)

    return detectedVariants

def main(tubes):

    # 0. first call
    variants=[]

    # 1. define some variables
    path2Samples='/Volumes/WINDOW/ap/varscan/output/'

    # 2. detecting SNPs and indels
    x=snpsReader(tubes,path2Samples)
    y=indelsReader(tubes,path2Samples)
    variants=x+y

    # 3. removing variants detected twice with different frequency
    toRemove=[]
    for variant in variants:
        toMatch=variant[:6]
        initialFreq=variant[6]
        for putative in variants:
            if toMatch == putative[:6] and initialFreq != putative[6]:
                if initialFreq > putative[6]:
                    toRemove.append(putative)
                else:
                    toRemove.append(variant)
    # removing
    toRemove=list(set(toRemove))
    for element in toRemove:
        variants.remove(element)

    return variants

def snpsReader(tubes,path2Samples):

    detectedVariants=[]

    for tube in tubes:
        dataFile=path2Samples+'varscanResultsAnnotated_%s_snp.vcf'%tube

        with open(dataFile,'r') as f:
            f.next()
            f.next()
            f.next()
            f.next()
            f.next()
            for line in f:
                vector=line.split('\t')

                # vartype
                vartype='SNP'

                # chr, chr, pos, ref, alt,freq
                chr=vector[0]
                pos=int(vector[1])
                ref=vector[2]
                alt=vector[-1].replace('\n','')
                freq=float(vector[7].split(';')[0].replace('%',''))/100.

                # keeping a minimalistic annotation
                sysName=vector[7].split('|')[3]
                standName=''
                description=''

                # caller and functional effect
                caller='varscan'
                functionalEffect=vector[7].split('|')[1]

                variant=(vartype,tube,chr,pos,ref,alt,freq,sysName,standName,description,caller,functionalEffect)
                detectedVariants.append(variant)

    return detectedVariants
