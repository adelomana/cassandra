#!/bin/bash

cd /Users/alomana
source .bash_profile

# 1.1 running breseq on the fist condition, A2
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_A2_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_A2_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/A2

# 1.2 running breseq on the fist condition, B
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_B_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_B_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/B

# 1.3 running breseq on the fist condition, D
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_D_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_D_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/D

# 1.4 running breseq on the fist condition, E2
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_E2_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_E2_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/E2

# 1.5 running breseq on the fist condition, F
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_F_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_F_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/F

# 1.6 running breseq on the fist condition, G
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_G_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L7_G_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/G

# 1.7 running breseq on the fist condition, H2
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_H2_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_H2_2.trimmed.fastq --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/H2

# 1.8 running breseq on the fist condition, I
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_I_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_I_2.trimmed.fastq --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/I

# 1.9 running breseq on the fist condition, J2
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_J2_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_J2_2.trimmed.fastq --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/J2

# 1.10 running breseq on the fist condition, K
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_K_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_K_2.trimmed.fastq --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/K

# 1.11 running breseq on the fist condition, L
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_L_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_L_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/L

# 1.12 running breseq on the fist condition, M
nice -n 20 /Users/alomana/software/breseq-0.26.0-MacOSX/bin/breseq -r /Users/alomana/projects/ap/seqs/src/genome/BY4741_Toronto_2012/BY4741_Toronto_2012.gff /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_M_1.trimmed.fastq /Users/alomana/projects/ap/seqs/data/150218_I1135_FCC634VACXX_L8_M_2.trimmed.fastq -j 4 --polymorphism-prediction -o /Users/alomana/projects/ap/seqs/results/toronto/M

