### this script creates the figures for the assessment for the third evolutionary experiment

import matplotlib,numpy,scipy
import matplotlib.pyplot,scipy.stats

matplotlib.rcParams['pdf.fonttype']=42 # this cryptical line is necessary for Illustrator compatibility of text saved as pdf

def grapher(results,generations,myTitles):

    ap1=results[0]
    sd1=results[1]
    ap2=results[2]
    sd2=results[3]

    fig=matplotlib.pyplot.figure()
    ax1=fig.add_subplot(111)
    ax2=fig.add_subplot(111)
    thePointSize=8
    matplotlib.rcParams.update({'font.size':24,'font.family':'Times New Roman','xtick.labelsize':24,'ytick.labelsize':24})

    cf30=[]
    cf0=[]

    for cellLine in ap1.keys():

        print cellLine

        fig = matplotlib.pyplot.figure()

        ax1 = fig.add_subplot(1,1,1)

        y1=ap1[cellLine]
        y2=ap2[cellLine]
        z1=sd1[cellLine]
        z2=sd2[cellLine]
        
        resistanceMean0=[element[0] for element in results[4][cellLine]]
        resistanceSds0=[element[1] for element in results[4][cellLine]]
        resistanceMean1=[element[0] for element in results[5][cellLine]]
        resistanceSds1=[element[1] for element in results[5][cellLine]]
        resistanceMean2=[element[0] for element in results[6][cellLine]]
        resistanceSds2=[element[1] for element in results[6][cellLine]]

        ax1.errorbar(generations,y1,yerr=z1,fmt=':o',color='black',ecolor='black',markeredgecolor='black',capsize=0,ms=thePointSize,mew=2)

        ax1.errorbar(generations,y2,yerr=z2,fmt=':o',color='black',ecolor='black',markeredgecolor='black',markerfacecolor='white',capsize=0,ms=thePointSize,mew=2)
        
        ax1.plot([0,300],[0,0],'--',color='black')
        ax1.set_xlim([-25,325])
        ax1.set_ylim([-0.5,0.5])
        ax1.set_yticks([-0.25,0.0,0.25])
        ax1.set_xlabel('Generation')
        ax1.set_ylabel('Conditioned Fitness')
        if cellLine[1] == '1':
            ax1.legend(['$\Delta$t = 30 min','$\Delta$t = 0 min'],loc=4,fontsize=27)

        ax2=ax1.twinx()
        ax2.errorbar(generations,resistanceMean0,yerr=resistanceSds0,fmt=':o',color='red',ecolor='red',markeredgecolor='red',markerfacecolor='white',capsize=0,ms=6,mew=1)
        #ax2.errorbar(t,resistanceMean1,yerr=resistanceSds1,fmt=':o',color='red',ecolor='red',markeredgecolor='red',markerfacecolor='white',capsize=0,ms=6,mew=1)
        #ax2.errorbar(t,resistanceMean2,yerr=resistanceSds2,fmt=':o',color='magenta',ecolor='magenta',markeredgecolor='magenta',markerfacecolor='white',capsize=0,ms=6,mew=1)
        ax2.set_ylim([0,2])
        ax2.set_yticks([0,0.5,1])
        ax2.set_xlim([-25,325])
        ax2.set_ylabel('FOA Resistance',color='red')
        ax2.tick_params(axis='y', colors='red')
        fig.suptitle(myTitles[cellLine],fontsize=26,y=0.995,x=0.53)
        fig.set_tight_layout(True)
        fig.savefig('%s.pdf'%cellLine)
        fig.clf()

        for i in range(len(y1)):
            cf30.append(y1[i])
            cf0.append(y2[i])
            
    fig.clf()

    # building a correlation plot of cf at time 0 and 30 min
    print len(cf30)
    coef,pValue=scipy.stats.pearsonr(cf30,cf0)
    print coef,pValue
    
    matplotlib.pyplot.plot(cf30,cf0,'ok')

    matplotlib.pyplot.plot(cf30, numpy.poly1d(numpy.polyfit(cf30, cf0, 1))(cf30), lw=1, color='red')

    matplotlib.pyplot.xlim([-0.4,0.4])
    matplotlib.pyplot.ylim([-0.4,0.4])
    matplotlib.pyplot.xlabel('CF(t=30)')
    matplotlib.pyplot.ylabel('CF(t=0)')

    # aspect
    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.axes().set_aspect('equal')

    matplotlib.pyplot.savefig('timeCorrelationFigure.pdf')
    matplotlib.pyplot.clf()              

    return None

def fileReader(generations):

    meanTrajectoriesA={};sdsTrajectoriesA={};meanTrajectoriesB={};sdsTrajectoriesB={};resistance0={};resistance1={};resistance2={}
    for cellLine in cellLines:
        
        meanTrajectoriesA[cellLine]=[]
        sdsTrajectoriesA[cellLine]=[]
        meanTrajectoriesB[cellLine]=[]
        sdsTrajectoriesB[cellLine]=[]
        resistance0[cellLine]=[]
        resistance1[cellLine]=[]
        resistance2[cellLine]=[]
        
        for generation in generations:
            inputFile='data/colony counts APEE3 - generation %s.tsv'%str(generation)
            with open(inputFile,'r') as f:
                lines=f.readlines()
                for line in lines:
                    vector=line.split()
                    if vector[0] == cellLine:

                        c30pre=[int(element) for element in vector[1].split(',')]
                        c30post=[int(element) for element in vector[2].split(',')]
                        m30pre=[int(element) for element in vector[3].split(',')]
                        m30post=[int(element) for element in vector[4].split(',')]
                        c0pre=[int(element) for element in vector[5].split(',')]
                        c0post=[int(element) for element in vector[6].split(',')]
    
                        s0=numpy.median(m30post)/numpy.median(m30pre)
                        s1=numpy.median(c30post)/numpy.median(c30pre)
                        s2=numpy.median(c0post)/numpy.median(c0pre)

                        sigma0=numpy.sqrt((numpy.var(m30pre)/5.)+(numpy.var(m30post)/5.))/numpy.median(m30pre)
                        sigma1=numpy.sqrt((numpy.var(c30pre)/5.)+(numpy.var(c30post)/5.))/numpy.median(c30pre)
                        sigma2=numpy.sqrt((numpy.var(c0pre)/5.)+(numpy.var(c0post)/5.))/numpy.median(c0pre)

                        ap1=s1-s0
                        ap2=s2-s0

                        sigmaAP1=numpy.sqrt((sigma0**2)/10. + (sigma1**2)/10.)
                        sigmaAP2=numpy.sqrt((sigma0**2)/10. + (sigma2**2)/10.)

                        print cellLine,generation
                        #print s0,s1,s2
                        #print sigma0,sigma1,sigma2
                        #print ap1,ap2
                        #print sigmaAP1,sigmaAP2
                        print 'c30pre',c30pre
                        print 'c30post',c30post
                        print 'm30pre',m30pre
                        print 'm30post',m30post

                        meanTrajectoriesA[cellLine].append(ap1)
                        meanTrajectoriesB[cellLine].append(ap2)
                        sdsTrajectoriesA[cellLine].append(sigmaAP1)
                        sdsTrajectoriesB[cellLine].append(sigmaAP2)
                        resistance0[cellLine].append([s0,sigma0])
                        resistance1[cellLine].append([s1,sigma1])
                        resistance2[cellLine].append([s2,sigma2])
                        
    return [meanTrajectoriesA,sdsTrajectoriesA,meanTrajectoriesB,sdsTrajectoriesB,resistance0,resistance1,resistance2]

# 0. variables
generations=[0,50,100,150,200,250,300]
cellLines=['M1','M2','M3','U1','U2','U3']
myTitles={}
myTitles['M1']='BY4741::URA3 mutagenized # 1'
myTitles['M2']='BY4741::URA3 mutagenized # 2'
myTitles['M3']='BY4741::URA3 mutagenized # 3'
myTitles['U1']='BY4741::URA3 unmutagenized # 1'
myTitles['U2']='BY4741::URA3 unmutagenized # 2'
myTitles['U3']='BY4741::URA3 unmutagenized # 3'

# 1. reading the files
results=fileReader(generations)

# 2. building the graphs
grapher(results,generations,myTitles)
