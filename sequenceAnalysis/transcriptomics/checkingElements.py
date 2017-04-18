# read coding transcripts
codingTranscripts=[]
fileName='/Volumes/omics4tb/alomana/projects/ap/seqs/transcriptomics/annotation/orf_coding_all_R64-2-1_20150113.fasta'
with open(fileName,'r') as f:
    for line in f:
        vector=line.split()
        if vector[0][0] == '>':
            geneName=vector[0].replace('>','')
            codingTranscripts.append(geneName)
print(len(codingTranscripts))
          
# read non-coding transcripts
noncodingTranscripts=[]
fileName='/Volumes/omics4tb/alomana/projects/ap/seqs/transcriptomics/annotation/rna_coding_R64-2-1_20150113.fasta'
with open(fileName,'r') as f:
    for line in f:
        vector=line.split()
        if vector[0][0] == '>':
            geneName=vector[0].replace('>','')
            noncodingTranscripts.append(geneName)
print(len(noncodingTranscripts))

c=list(set(codingTranscripts) & set(noncodingTranscripts))

print(c)
