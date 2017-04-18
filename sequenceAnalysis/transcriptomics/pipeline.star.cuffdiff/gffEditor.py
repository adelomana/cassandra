import sys


inputFileName='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/saccharomyces_cerevisiae_R64-2-1_20150113.gff'
minimalGFF='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/saccharomyces_cerevisiae_R64-2-1_20150113.minimal.gff'

selectedElements=['gene', 'CDS', 'mRNA']

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

# 2. making a minimal gff with "exon" instead of "CDS"
g=open(minimalGFF,'w')
with open(inputFileName,'r') as f:
    for i in range(18):
        next(f)

    for line in f:
        vector=line.split('\t')

        if len(vector) > 2:
            feature=vector[2]
            if feature in selectedElements:
                newLine=line.replace('CDS','exon')
                g.write(newLine)
            
g.close()
