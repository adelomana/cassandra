import os,sys

def main(tubes):

    # 0. first call
    variants=[]

    # 1. define the files to read
    homeDir=os.getenv("HOME")
    path2Files=homeDir+'/gDrive2/projects/centers/ap/results/breseq/toronto/'

    # 2. going through the samples
    for tube in tubes:
        tubeVariants=tubeReader(tube,path2Files)
        variants=variants+tubeVariants

    return variants

def tubeReader(tube,path2Files):

    inputFile=path2Files+tube+'.txt'
    listening=True
    tubeVariants=[]

    with open(inputFile,'r') as f:
        f.next()
        f.next()
        f.next()
        f.next()
        f.next()
        for line in f:
            vector=line.split('\t')

            if len(vector) > 0:
                if vector[0] == 'Unassigned missing coverage evidence\n':
                    listening=False

            if len(vector) > 5 and listening == True:

                # dealing with vartype
                item=vector[3][0]
                if item == 'A' or item == 'T' or item == 'G' or item == 'C':
                    vartype='SNP'
                    ref=item
                    alt=vector[3].split('\xe2\x86\x92')[1]
                else:
                    vartype='indel'
                    ref=''
                    alt=vector[3]

                # dealing with chr
                chr=vector[1]
                chr=chr.replace('\xe2\x80\x91','-')

                # dealing with pos
                pos=int(vector[2].replace(',',''))

                # dealing freq
                freq=float(vector[4].replace('%',''))/100.

                # dealing with systematic name
                sysName=''
                wx=vector[6]
                wx=wx.replace('\xe2\x86\x92',' ')
                wx=wx.replace('\xe2\x86\x90',' ')
                wx=wx.replace('\xe2\x86\x91',' ')
                wx=wx.replace('\xe2\x80\x93',' ')
                wx=wx.replace('_CDS',' ')
                wx=wx.replace('[',' ')
                wx=wx.replace(']',' ')
                wx=wx.replace('/',' ')
                names=wx.split()
                if len(names) == 0:
                    pass
                elif len(names) == 1:
                    sysName=names[0]
                elif len(names) == 2:
                    if names[0] == '':
                        sysName=names[1]
                    elif names[1] == '':
                        sysName=names[0]
                    else:
                        if vector[5] != '':
                            tempo=vector[5].split()[1].replace('(','')
                            tempo=tempo.replace('\xe2\x80\x91','')
                            tempo=tempo.replace('\xe2\x80\x93','')
                            tempo=tempo.replace(')','')
                            vtempo=tempo.split('/')
                            itempo=[abs(int(element)) for element in vtempo]
                            if itempo[0] < itempo[1]:
                                sysName=names[0]
                            else:
                                sysName=names[1]
                        else:
                            sysName=names[0]
                            print 'WARNING: strange formatting detected. Returning sysName',sysName
                else:
                    print names
                    print 'error from breseqReader while figuring out the sysName.'
                    sys.exit()
                sysName=sysName.replace('\xe2\x80\x91','-')

                # establishing the functional effect
                functionalEffect=''
                if vector[5].find('coding') != -1:
                    functionalEffect='coding'
                elif vector[5].find('intergenic') != -1:
                    functionalEffect='intergenic'
                elif vector[5].find('noncoding') != -1:
                    functionalEffect='noncoding'
                else:
                    if len(vector[5].split()) > 1:
                        transition=vector[5].split()[0]
                        if transition[0] == transition[-1]:
                            functionalEffect='synonymous_%s'%transition
                        else:
                            functionalEffect='aaChange_%s'%transition


                # going for minimal annotations
                standName=''
                description=''
                caller='breseq'

                variant=(vartype,tube,chr,pos,ref,alt,freq,sysName,standName,description,caller,functionalEffect)
                tubeVariants.append(variant)

    return tubeVariants
