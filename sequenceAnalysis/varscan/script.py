### this script calls varscan based on the GATK mapping results
import os,sys

# 0. defining variables
tubes=['A2','B','D','E2','F','G','H2','I','J2','K','L','M']
path2Bam='/Volumes/WINDOW/ap/gatk/BY4741/tmp/150218_I1135_FCC634VACXX_L*'
genomePath='/Users/alomana/gDrive2/projects/ap/src/gatk/genome/BY4741_Toronto_2012.fasta' # path to the fa file of the genome reference file
outputDir='/Volumes/WINDOW/ap/varscan'+'/output'

javaPath='/usr/bin/java'
varscanPath='/Users/alomana/software/varscan/VarScan.v2.3.9.jar'
samtoolsPath='/usr/local/bin/samtools'
snpEffPath='/Users/alomana/software/snpEff/snpEff.jar'

# 1. calling varscan
print
print 'welcome to the varscan pipeline...'
print

for tube in tubes:

    print '\t analysing tube %s'%tube

    bamFile=path2Bam+'_'+tube+'/file_recalibrated.bam'

    cmd1='%s mpileup -B -f %s  %s | %s -jar %s pileup2snp --min-coverage 50 --min-var-freq 0.15 --output-vcf 1 > %s/varscanResults_%s_snp.vcf'%(samtoolsPath,genomePath,bamFile,javaPath,varscanPath,outputDir,tube)
    cmd2='%s mpileup -B -f %s  %s | %s -jar %s pileup2indel --min-coverage 50 --min-var-freq 0.15 --output-vcf 1 > %s/varscanResults_%s_indel.vcf'%(samtoolsPath,genomePath,bamFile,javaPath,varscanPath,outputDir,tube)
    
    print
    print cmd1
    print
    os.system(cmd1)
    print
    print cmd2
    print
    os.system(cmd2)

    # 2. filtering SNPs
    print '\t filtering SNPs around indels...'

    cmd='%s -jar %s filter %s/varscanResults_%s_snp.vcf --indel-file %s/varscanResults_%s_indel.vcf --output-file %s/varscanResultsFiltered_%s_snp.vcf'%(javaPath,varscanPath,outputDir,tube,outputDir,tube,outputDir,tube)
    
    print
    print cmd
    print
    os.system(cmd)
    print

    # 3. fixing the vcf format for SnpEff
    print '\t fixing VCF format for SnpEff...'
    inputFile='%s/varscanResultsFiltered_%s_snp.vcf'%(outputDir,tube)
    outputFile='%s/varscanResultsFilteredFixed_%s_snp.vcf'%(outputDir,tube)

    f=open(inputFile,'r')
    g=open(outputFile,'w')

    f.next()
    for line in f:
        vector=line.split()
        vector.insert(4,'ADLfix')
        g.write('\t'.join(vector))
        g.write('\n')
    
    f.close()
    g.close()

    inputFile='%s/varscanResults_%s_indel.vcf'%(outputDir,tube)
    outputFile='%s/varscanResultsFixed_%s_indel.vcf'%(outputDir,tube)

    f=open(inputFile,'r')
    g=open(outputFile,'w')

    f.next()
    for line in f:
        vector=line.split()
        vector.insert(4,'ADLfix')
        g.write('\t'.join(vector))
        g.write('\n')
    
    f.close()
    g.close()

    # 4. annotating with SnpEff SNPs and indels

    os.mkdir('%s/%s'%(outputDir,tube))
    
    print '\t annotating with SnpEff...'

    cmd1='%s -Xmx2g -jar %s -v -s %s/%s/snps.annotated.summary.html sce.BY4741.toronto %s/varscanResultsFilteredFixed_%s_snp.vcf > %s/varscanResultsAnnotated_%s_snp.vcf'%(javaPath,snpEffPath,outputDir,tube,outputDir,tube,outputDir,tube)
    cmd2='%s -Xmx2g -jar %s -v -s %s/%s/indels.annotated.summary.html sce.BY4741.toronto %s/varscanResultsFixed_%s_indel.vcf > %s/varscanResultsAnnotated_%s_indels.vcf'%(javaPath,snpEffPath,outputDir,tube,outputDir,tube,outputDir,tube)

    print cmd1
    print
    os.system(cmd1)
    print
    print cmd2
    print
    os.system(cmd2)
    print

    # 5. final annotation with SnpSift
    print '\t final annotation with SnpSift...'

    path2script=snpEffPath.split('/snpEff.jar')[0]
    
    cmd1='cat %s/varscanResultsAnnotated_%s_snp.vcf | perl %s/scripts/vcfEffOnePerLine.pl | %s -jar %s/SnpSift.jar extractFields - CHROM POS REF ALT AF AC DP MQ "ANN[*].ALLELE" "ANN[*].EFFECT" "ANN[*].IMPACT" "ANN[*].GENE" "ANN[*].GENEID" "ANN[*].FEATURE" "ANN[*].BIOTYPE" "ANN[*].RANK" "ANN[*].HGVS_C" "ANN[*].HGVS_P" "ANN[*].CDNA_POS" "ANN[*].CDNA_LEN" "ANN[*].CDS_POS" "ANN[*].CDS_LEN" "ANN[*].AA_POS" "ANN[*].AA_LEN" "ANN[*].DISTANCE" "ANN[*].ERRORS"  > %s/finalProduct_SNPs_%s.txt'%(outputDir,tube,path2script,javaPath,path2script,outputDir,tube)

    cmd2='cat %s/varscanResultsAnnotated_%s_indels.vcf | perl %s/scripts/vcfEffOnePerLine.pl | %s -jar %s/SnpSift.jar extractFields - CHROM POS REF ALT AF AC DP MQ "ANN[*].ALLELE" "ANN[*].EFFECT" "ANN[*].IMPACT" "ANN[*].GENE" "ANN[*].GENEID" "ANN[*].FEATURE" "ANN[*].BIOTYPE" "ANN[*].RANK" "ANN[*].HGVS_C" "ANN[*].HGVS_P" "ANN[*].CDNA_POS" "ANN[*].CDNA_LEN" "ANN[*].CDS_POS" "ANN[*].CDS_LEN" "ANN[*].AA_POS" "ANN[*].AA_LEN" "ANN[*].DISTANCE" "ANN[*].ERRORS"  > %s/finalProduct_indels_%s.txt'%(outputDir,tube,path2script,javaPath,path2script,outputDir,tube)

    print
    print cmd1
    print
    os.system(cmd1)
    print
    print cmd2
    print
    os.system(cmd2)
    print        

print '... done.'
