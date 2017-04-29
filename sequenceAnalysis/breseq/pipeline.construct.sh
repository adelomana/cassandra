#!/bin/bash

cd /Users/alomana
source .bash_profile

# running breseq on B (n=50)
time /Applications/breseq-0.30.0-MacOSX-10.7+/bin/breseq -r /Users/alomana/github/cassandra/sequenceAnalysis/breseq/cis.fasta /Users/alomana/scratch/construct/filteredSeqs/B/150218_I1135_FCC634VACXX_L7_B_1.trimmed.fastq /Users/alomana/scratch/construct/filteredSeqs/B/150218_I1135_FCC634VACXX_L7_B_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/scratch/construct/results/B


# running breseq on F (n=200)
time /Applications/breseq-0.30.0-MacOSX-10.7+/bin/breseq -r /Users/alomana/github/cassandra/sequenceAnalysis/breseq/cis.fasta /Users/alomana/scratch/construct/filteredSeqs/F/150218_I1135_FCC634VACXX_L7_F_1.trimmed.fastq /Users/alomana/scratch/construct/filteredSeqs/F/150218_I1135_FCC634VACXX_L7_F_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/scratch/construct/results/F

# running breseq on I (n=150)
time /Applications/breseq-0.30.0-MacOSX-10.7+/bin/breseq -r /Users/alomana/github/cassandra/sequenceAnalysis/breseq/cis.fasta /Users/alomana/scratch/construct/filteredSeqs/I/150218_I1135_FCC634VACXX_L7_I_1.trimmed.fastq /Users/alomana/scratch/construct/filteredSeqs/I/150218_I1135_FCC634VACXX_L7_I_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/scratch/construct/results/I

