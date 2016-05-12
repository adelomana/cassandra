import os,sys

def indelsReader(tubes,path2Samples):

    referenceFile='/Volumes/WINDOW/ap/gatk/BY4741/output/A2/indels_finalProduct.txt'
    detectedVariants=[]

    for tube in tubes:

        with open(referenceFile,'r') as f:
            f.next()
            for line in f:
                vector=line.split('\t')
                if vector[8] == 'true': # it is a variant that passed the filters
                    sysName=vector[12]

                    dataFile=path2Samples+tube+'_specific_indels.vcf'
                    with open(dataFile,'r') as ff:
                        for ffline in ff:
                            ffvector=ffline.split('\t')
                            if vector[0] == ffvector[0]:
                                if vector[1] == ffvector[1]:

                                    allValues=ffvector[9].split(':')[1].split(',')
                                    allFloatValues=[float(element) for element in allValues]

                                    a=allFloatValues[0]
                                    b=sum(allFloatValues[1:])

                                    if a+b == 0.:
                                        freq=0.
                                    else:
                                        freq=b/(a+b)

                                    if freq > 0.:

                                        # vartype
                                        vartype='indel'

                                        # chr, chr, pos, ref, alt
                                        chr=ffvector[0]
                                        pos=int(ffvector[1])
                                        ref=ffvector[3]
                                        alt=ffvector[4]

                                        # keeping a minimalistic annotation
                                        standName=''
                                        description=''

                                        # caller and functional effect
                                        caller='GATK'
                                        functionalEffect=vector[10]

                                        variant=(vartype,tube,chr,pos,ref,alt,freq,sysName,standName,description,caller,functionalEffect)
                                        detectedVariants.append(variant)

    return detectedVariants

def main(tubes):

    # 0. first call
    variants=[]

    # 1. define some variables
    path2Samples='/Volumes/WINDOW/ap/gatk/BY4741/tmp/'

    # 2. detecting SNPs and indels
    x=snpsReader(tubes,path2Samples)
    y=indelsReader(tubes,path2Samples)
    variants=x+y

    return variants

def snpsReader(tubes,path2Samples):

    referenceFile='/Volumes/WINDOW/ap/gatk/BY4741/output/A2/SNPs_finalProduct.txt'
    detectedVariants=[]

    for tube in tubes:

        with open(referenceFile,'r') as f:
            f.next()
            for line in f:
                vector=line.split('\t')
                if vector[8] == 'true': # it is a variant that passed the filters
                    sysName=vector[12]

                    dataFile=path2Samples+tube+'_specific_snps.vcf'
                    with open(dataFile,'r') as ff:
                        for ffline in ff:
                            ffvector=ffline.split('\t')
                            if vector[0] == ffvector[0]:
                                if vector[1] == ffvector[1]:

                                    a=float((ffvector[9].split(':')[1].split(',')[0]))
                                    b=float((ffvector[9].split(':')[1].split(',')[1]))

                                    if a+b == 0.:
                                        freq=0.
                                    else:
                                        freq=b/(a+b)

                                    if freq > 0.:

                                        # vartype
                                        vartype='SNP'

                                        # chr, chr, pos, ref, alt
                                        chr=ffvector[0]
                                        pos=int(ffvector[1])
                                        ref=ffvector[3]
                                        alt=ffvector[4]

                                        # keeping a minimalistic annotations
                                        standName=''
                                        description=''

                                        # caller and functional effect
                                        caller='GATK'
                                        functionalEffect=vector[10]

                                        variant=(vartype,tube,chr,pos,ref,alt,freq,sysName,standName,description,caller,functionalEffect)
                                        detectedVariants.append(variant)

    return detectedVariants
