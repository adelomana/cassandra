### this scripts performs sequence analysis on S. cerevisiae
import sys,os

def analysis(inputs):

    '''
    This function deals with complete sequence analysis.
    '''

    # 1. cleaning reads with trimmomatic
    print '\t trimming reads with trimmomatic...'
    trimmomaticCleaner(inputs)

    return None

def trimmomaticCleaner(inputs):

    '''
    This function deals with the trimming of the reads using Trimmomatic.
    '''

    path2Adapter='/Users/alomana/projects/ap/seqs/src/adapters/TruSeq3-PE-2.fa'

    print inputs

    logFileLabel=inputs[0].split('_1.fq')[0]+'.messagesFromTrimming.txt'
    inputFile1=inputs[0]
    inputFile2=inputs[1]
    outputFile1a=inputs[0].split('.fq')[0]+'.trimmed.fastq'
    outputFile1b=inputs[0].split('.fq')[0]+'.trimmed.garbage.fastq'
    outputFile2a=inputs[1].split('.fq')[0]+'.trimmed.fastq'
    outputFile2b=inputs[1].split('.fq')[0]+'.trimmed.garbage.fastq'

    cmd='/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -jar /Users/alomana/software/Trimmomatic-0.33/trimmomatic-0.33.jar PE -threads 4 -phred64 -trimlog %s %s %s %s %s %s %s ILLUMINACLIP:%s:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'%(logFileLabel,inputFile1,inputFile2,outputFile1a,outputFile1b,outputFile2a,outputFile2b,path2Adapter)
    os.system(cmd)
    
    return None

### MAIN

# 0. welcome
print 'welcome to the fix to all your problems.'
print

# 1. defining the input files
rootFolder='/proj/omics4tb/alomana/projects/ap/seqs/'
rootFolder='/Users/alomana/projects/ap/seqs/'

inputFolders=[]
inputFolderLabels=['A2','B','D','E2','F','G','H2','I','J2','K','L','M']
inputFolderLabels=['A2']
for element in inputFolderLabels:
    inputFolders.append(rootFolder+element)

inputFiles=[]
for folder in inputFolders:
    target=folder+'/'+'clean_data/'
    files=os.listdir(target)
    pairs=[]
    for file in files:
        if file[-3:] == '.fq':
            pairs.append(target+file)
    inputFiles.append(pairs)

# 2. running the analysis
for inputs in inputFiles:
    print 'starting the analysis of %s'%inputs[0].split('.fq')[0].split('/')[-1]
    analysis(inputs)

print
print '... all your problems are fixed now.'

