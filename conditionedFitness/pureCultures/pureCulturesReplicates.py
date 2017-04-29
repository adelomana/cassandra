import sys,datetime
import matplotlib,matplotlib.pyplot

sys.path.append('../lib')
import calculateStatistics

matplotlib.rcParams.update({'font.size':18,'font.family':'Arial','xtick.labelsize':14,'ytick.labelsize':14})

def dataReader1(dataFile):

    generation='single colonies'
    colonyCounts={}
    dilutionFactors={}

    fails=['colony # 13','colony # 14','colony # 15','colony # 18','colony # 19','colony # 20']
        
    with open(dataFile,'r') as f:
        for line in f:
            vector=line.split(',')
            if vector[0] == 'final':

                if vector[1] == 'dilution factor':
                    a=int(vector[2].split('in')[0])
                    b=int(vector[2].split('in')[1])
                    c=int(vector[3].split('in')[0])
                    d=int(vector[3].split('in')[1])
                    dilutionFactors[generation]=[((a+b)/a)**3,((c+d)/c)**3]

                elif 'colony' in vector[1] and vector[1] not in fails:

                    a=int(vector[2])
                    b=int(vector[3])
                    c=int(vector[4])
                    d=int(vector[5])

                    x=dilutionFactors['single colonies'][0]
                    y=dilutionFactors['single colonies'][1]
                    
                    survival_nt=(b*y)/(a*x)
                    survival_t=(d*y)/(c*x)

                    cf=survival_t-survival_nt
                    
                    colonyCounts[vector[1]]=[cf]
                    
    return colonyCounts

def dataReader2(dataFile):

    generation='single colonies'
    colonyCounts={}
    dilutionFactors={}
        
    with open(dataFile,'r') as f:
        for line in f:
            vector=line.split(',')
            
            if vector[0] == 'final':

                if vector[1] == 'dilution factor':
                    a=int(vector[2].split('in')[0])
                    b=int(vector[2].split('in')[1])
                    c=int(vector[3].split('in')[0])
                    d=int(vector[3].split('in')[1])
                    dilutionFactors[generation]=[((a+b)/a)**3,((c+d)/c)**3]

            elif 'plate' in vector[2]:

                if vector[1] != '':
                    colonyName=vector[1]

                if 'colony 30' not in colonyName:

                    if (colonyName == 'colony 8.1' and vector[2] == 'plate # 3') is False:

                        a=int(vector[3])
                        b=int(vector[4])
                        c=int(vector[5])
                        d=int(vector[6])

                        if colonyName not in colonyCounts.keys():
                            colonyCounts[colonyName]=[[a],[b],[c],[d]]
                        else:
                            colonyCounts[colonyName][0].append(a)
                            colonyCounts[colonyName][1].append(b)
                            colonyCounts[colonyName][2].append(c)
                            colonyCounts[colonyName][3].append(d)

    # converting colony counts into cf
    validNames=list(colonyCounts.keys())
    validNames.sort()
    
    converted={}
    for name in validNames:
        print(name)
        treatment=[colonyCounts[name][2],colonyCounts[name][3]]
        nt=[colonyCounts[name][0],colonyCounts[name][1]]
        cf_mu, cf_sd, pvalue = calculateStatistics.main(treatment,nt)
        converted[name]=[cf_mu,cf_sd,pvalue]

    
    return converted

def tprint(value):

    '''
    this function prints a string with formatted time
    '''

    now=datetime.datetime.now()
    formattedNow=now.strftime("%Y-%m-%d %H:%M:%S")

    print('{}\t{}...'.format(formattedNow,value))

    return None

### MAIN

# 0. user defined variables
dataFile1='/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/evol4/APEE4 Colony Counts - pure cultures.csv'
dataFile2='/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/evol4/APEE4 Colony Counts - pure cultures 2.csv'

thePointSize=12

# 1. reading the data
tprint('reading data files')
colonyCounts1=dataReader1(dataFile1)
colonyCounts2=dataReader2(dataFile2)

for name in colonyCounts1.keys():
    print(name,colonyCounts1[name])


# 3. making figures
tprint('building figures')

names=list(colonyCounts2.keys())
names.sort()

x=0
for i in range(len(names)):
    x=x+1
    y=colonyCounts2[names[i]][0]
    z=colonyCounts2[names[i]][1]
    matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='black',ecolor='black',markeredgecolor='black',capsize=0,ms=thePointSize,mew=0)

s10=1.8049188274343546
s11=0.968992248062015
s3=0.7759117813465638
s6=1.6135180045910842
s8=0.68051005551005

x=1
matplotlib.pyplot.plot([x,x+2],[s10,s10],ls='--',color='black')

x=x+3
matplotlib.pyplot.plot([x,x+2],[s11,s11],ls='--',color='black')

x=x+3
matplotlib.pyplot.plot([x,x+2],[s3,s3],ls='--',color='black')

x=x+3
matplotlib.pyplot.plot([x,x+2],[s6,s6],ls='--',color='black')

x=x+3
matplotlib.pyplot.plot([x,x+2],[s8,s8],ls='--',color='black')


matplotlib.pyplot.xticks([i for i in range(len(names))],names,rotation=45)
matplotlib.pyplot.ylabel('Cond. Fit.')

matplotlib.pyplot.tight_layout()

matplotlib.pyplot.savefig('singleColoniesFigure.2.pdf')
