import os,sys

'''
this script finds the clean FASTQ files and calls STAR for the reads alignment.
'''

def genomeIndexer():

    '''
    this function creates the genome index. Should be run only once.
    '''

    flag1=' --runMode genomeGenerate'
    flag2=' --runThreadN %s'%numberOfThreads
    flag3=' --genomeDir %s'%genomeIndexDir
    flag4=' --genomeFastaFiles %s'%genomeFastaFile
    flag5=' --sjdbGTFfile %s'%genomeAnnotationFile
    flag6=' --sjdbGTFtagExonParentTranscript Parent --sjdbOverhang 75 --genomeSAindexNbases 8'

    cmd=STARexecutable+flag1+flag2+flag3+flag4+flag5+flag6

    print('')
    print(cmd)
    print('')
    os.system(cmd)

    return None

def STARcalling(tag):

    '''
    this function calls STAR
    '''
    
    finalDir=bamFilesDir+tag+'/'
    if os.path.exists(finalDir) == False:
        os.mkdir(finalDir)

    read1=['{}_L00{}_R1_001.paired.forward.fastq'.format(readsFilesDir+tag,i+1,readsFilesDir+tag,i+1) for i in range(4)]
    read2=['{}_L00{}_R2_001.paired.reverse.fastq'.format(readsFilesDir+tag,i+1,readsFilesDir+tag,i+1) for i in range(4)]
    sampleString=','.join(read1) + ' ' + ','.join(read2)

    flag1=' --genomeDir %s'%genomeIndexDir
    flag2=' --runThreadN %s'%numberOfThreads
    flag3=' --readFilesIn %s'%sampleString   
    flag4=' --outFileNamePrefix %s'%finalDir
    flag5=' --outFilterType BySJout --outFilterMultimapNmax 20 --alignSJoverhangMin 8 --alignSJDBoverhangMin 1 --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000 --outSAMstrandField intronMotif --outFilterIntronMotifs RemoveNoncanonical --outSAMtype BAM SortedByCoordinate --limitBAMsortRAM 5357465103'

    cmd='time '+STARexecutable+flag1+flag2+flag3+flag4+flag5
    
    print('')
    print(cmd)
    print('')
    os.system(cmd)
    
    return None

# 0. defining several input/output paths
readsFilesDir='/proj/omics4tb/alomana/projects/ap/data/transcriptomics/cleanFASTQ/'
bamFilesDir='/proj/omics4tb/alomana/projects/ap/data/transcriptomics/BAM/'
STARexecutable='/proj/omics4tb/alomana/software/STAR-2.5.2b/bin/Linux_x86_64/STAR'
genomeIndexDir='/proj/omics4tb/alomana/projects/ap/data/transcriptomics/starIndex'
genomeFastaFile='/proj/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/S288C_reference_sequence_R64-2-1_20150113.fsa'              
genomeAnnotationFile='/proj/omics4tb/alomana/projects/ap/data/transcriptomics/annotation/saccharomyces_cerevisiae_R64-2-1_20150113.minimal.gff'   
numberOfThreads=16

# 1. recover the clean FASTQ files
print('reading FASTQ files...')
allTags=[]
allFiles=os.listdir(readsFilesDir)
for element in allFiles:
    if '_L001_R1_001.paired.forward.fastq' in element:
        tag=element.split('_L001_R1_001.paired.forward.fastq')[0]
        allTags.append(tag)

allTags.sort()

# 2. making genome indexes
print('making genome index...')
genomeIndexer()
       
# 3. calling STAR
print('calling STAR...')
for tag in allTags:
    STARcalling(tag)
