import sys

inputFileName='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/Saccharomyces_cerevisiae.R64-1-1.34.gff3'
maskedGFF='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/Saccharomyces_cerevisiae.R64-1-1.34.masked.gff3'

# 1. finding all elements
allElements=[]
with open(inputFileName,'r') as f:
    for i in range(18):
        next(f)

    for line in f:
        vector=line.split('\t')

        if len(vector) > 2:
            element=vector[2]
            if element not in allElements:
                allElements.append(element)

print(allElements)

# 2. making a masked GFF
maskedElements=[ 'ncRNA_gene','tRNA_gene','snoRNA_gene','snoRNA','snRNA_gene','snRNA','rRNA_gene','rRNA']
h=open(maskedGFF,'w')
with open(inputFileName,'r') as f:
    for i in range(18):
        next(f)

    for line in f:
        vector=line.split('\t')

        if len(vector) > 2:
            feature=vector[2]
            if feature in maskedElements:
                h.write(line)
            
h.close()
