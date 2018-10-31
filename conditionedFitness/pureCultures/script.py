import sys,datetime
import matplotlib,matplotlib.pyplot

matplotlib.rcParams.update({'font.size':18,'font.family':'Arial','xtick.labelsize':14,'ytick.labelsize':14})

def dataReader():

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

                    print(vector)

                    a=int(vector[2])
                    b=int(vector[3])
                    c=int(vector[4])
                    d=int(vector[5])

                    x=dilutionFactors['single colonies'][0]
                    y=dilutionFactors['single colonies'][1]
                    
                    survival_nt=(b*y)/(a*x)
                    survival_t=(d*y)/(c*x)

                    cf=survival_t-survival_nt
                    
                    print(a,b,c,d)
                    print('survival_t',survival_t)
                    print('survival_nt',survival_nt)
                    print('cf',cf)
                    print('')

                    colonyCounts[vector[1]]=[cf,survival_nt]
                    
    return colonyCounts


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
dataFile='/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/evol4/APEE4 Colony Counts - pure cultures.csv'
dataFile='/Users/adriandelomana/Google Drive/projects/centers/ap/src/assessmentGraphs/evol4/APEE4 Colony Counts - pure cultures.csv'

# 1. reading the data
tprint('reading data files')
colonyCounts=dataReader()

# 3. making figures
tprint('building figures')

exponential=['colony # 21','colony # 22','colony # 23','colony # 24','colony # 25','colony # 26','colony # 27','colony # 28','colony # 29','colony # 30']

n50=['colony # 1','colony # 2','colony # 3','colony # 4','colony # 5']

cf50=[]; cf300=[]

for colony in colonyCounts.keys():

    print(colony,colonyCounts[colony])

    x=colonyCounts[colony][0]

    if colony in n50:
        cf50.append(x)
    else:
        cf300.append(x)
        
# building the graph
clonalCFs=[-0.068974033701179882,0.071254510811961769,-0.091336423581641291]

pos1=[1 for element in clonalCFs]
pos2=[2 for element in cf50]
pos3=[3 for element in cf300]

mean50=0.21970559001182866
mean300=0.3357718732989069

matplotlib.pyplot.plot(pos1,clonalCFs,marker='o',color='green',alpha=0.5,markersize=10,lw=0,mew=0)
matplotlib.pyplot.plot(pos2,cf50,marker='o',color='black',alpha=0.5,markersize=10,lw=0,mew=0)
matplotlib.pyplot.plot(pos3,cf300,marker='o',color='black',alpha=0.5,markersize=10,lw=0,mew=0)

cf300.sort()
print(cf300)

matplotlib.pyplot.plot([2-0.05,2+0.05],[mean50,mean50],'-',color='blue',lw=3)
matplotlib.pyplot.plot([3-0.05,3+0.05],[mean300,mean300],'-',color='blue',lw=3)

matplotlib.pyplot.ylabel('Conditioned Fitness')
matplotlib.pyplot.xlim([0.5,3.5])

matplotlib.pyplot.xticks([1,2,3],['C1-3 n=0','E2 n=50', 'E1 n=300'])

matplotlib.pyplot.savefig('singleColoniesFigure.pdf')
