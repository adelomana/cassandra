import sys,numpy,matplotlib,random,scipy
from matplotlib import pyplot
from scipy import stats
from scipy import interpolate

def dataReader(case,generation,workingThresholds,treatment):

    '''
    this function calls the fileReader function.
    '''

    distributions=[]
    for i in range(len(workingThresholds)):

        thresholdCito=workingThresholds[i][0]
        thresholdPero=workingThresholds[i][1]
        path='../data/'+case+'/'+generation+'/'+treatment+'/image'+str(i+1)+'.txt'

        distribution=fileReader(path,thresholdCito,thresholdPero)
        distributions.append(distribution)
    
    return distributions

def dataReaderSum(case,generation,workingThresholds,treatment):

    '''
    this function calls the fileReader function.
    '''

    distributions=[[],[]]
    for i in range(len(workingThresholds)):

        thresholdCito=workingThresholds[i][0]
        thresholdPero=workingThresholds[i][1]
        path='../data/'+case+'/'+generation+'/'+treatment+'/image'+str(i+1)+'.txt'

        distribution=fileReaderSum(path,thresholdCito,thresholdPero)
        distributions[0]=distributions[0]+distribution[0]
        distributions[1]=distributions[1]+distribution[1]
    
    return distributions

def dataReaderWithFigures_deprec(case,generation,workingThresholds,treatment):

    '''
    this function calls the fileReaderWithFigures function
    '''

    for i in range(len(workingThresholds)):

        thresholdCito=workingThresholds[i][0]
        thresholdPero=workingThresholds[i][1]
        path='../data/'+case+'/'+generation+'/'+treatment+'/image'+str(i+1)+'.txt'

        fileReaderWithFigures(path,thresholdCito,thresholdPero)

    return None

def fileReader(path,thresholdCito,thresholdPero):

    '''
    this function reads each specific image file.
    '''

    # 1. defining variables
    
    print '\t analyzing',path,'with thresholds',thresholdCito,thresholdPero

    citoSignal=[]
    peroSignal=[]

    # 2. reading the data file
    with open(path,'r') as f:
        for line in f:
            vector=line.split()
            v=[]
            for pixel in vector:
            
                if int(pixel) < thresholdCito:
                    p=0
                elif thresholdCito <= int(pixel) < thresholdPero:
                    p=1
                elif int(pixel) >= thresholdPero:
                    p=2
                else:
                    print pixel
                    print 'error a'
                    sys.exit()

                if p == 1:
                    citoSignal.append(int(pixel))

                if p == 2:
                    peroSignal.append(int(pixel))

    # 3. treating data
    logCito=numpy.log10(citoSignal)
    logPero=numpy.log10(peroSignal)
    distribution=logPero-numpy.mean(logCito)

    ### alternative distributions
    #distribution=numpy.log10(peroSignal-numpy.mean(citoSignal))
    #distribution=numpy.array(peroSignal)-numpy.mean(citoSignal)
    #distribution=logPero-numpy.mean(logCito)
    #distribution=peroSignal/numpy.mean(citoSignal)
    #distribution=numpy.log10(peroSignal/numpy.mean(citoSignal))
        
    return distribution

def fileReaderSum(path,thresholdCito,thresholdPero):

    '''
    this function reads each specific image file.
    '''

    # 1. defining variables
    
    print '\t analyzing',path,'with thresholds',thresholdCito,thresholdPero

    citoSignal=[]
    peroSignal=[]

    # 2. reading the data file
    with open(path,'r') as f:
        for line in f:
            vector=line.split()
            v=[]
            for pixel in vector:
            
                if int(pixel) < thresholdCito:
                    p=0
                elif thresholdCito <= int(pixel) < thresholdPero:
                    p=1
                elif int(pixel) >= thresholdPero:
                    p=2
                else:
                    print pixel
                    print 'error a'
                    sys.exit()

                if p == 1:
                    citoSignal.append(int(pixel))

                if p == 2:
                    peroSignal.append(int(pixel))

    # 3. treating data
    logCito=list(numpy.log10(citoSignal))
    logPero=list(numpy.log10(peroSignal))
    distribution=[logCito,logPero]
        
    return distribution

def histogrammer(theData):

    '''
    this function creates a histogram.
    '''

    n,bins=numpy.histogram(theData,bins=int(numpy.sqrt(len(theData))))

    x=[]
    halfBin=(bins[1]-bins[0])/2.
    for bin in bins:
        center=bin+halfBin
        x.append(center)
    x.pop()

    y=[]
    y=numpy.array(n)
    y=list(y/float(sum(y)))

    return x,y

def histoPlotter(before,after,outputFileName):

    '''
    this function creates the final figures
    '''

    matplotlib.rc('xtick', labelsize=22) 
    matplotlib.rc('ytick', labelsize=22)
    matplotlib.rc('font',size=28)
    matplotlib.rc('legend',fontsize=22)
    
    blueDotsx=[]
    blueDotsy=[]
    
    for element in before:
        x,y=histogrammer(element)
        for i in range(len(x)):
            blueDotsx.append(x[i])
            blueDotsy.append(y[i])
        matplotlib.pyplot.plot(x,y,'.',color='blue',mec='None',alpha=0.25)

    inter=scipy.interpolate.UnivariateSpline(blueDotsx,blueDotsy)
    xnew=numpy.linspace(min(blueDotsx),max(blueDotsx),num=100,endpoint=True)
    matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='blue',lw=2,label='before caffeine')
    
    redDotsx=[]
    redDotsy=[]
    
    for element in after:
        x,y=histogrammer(element)
        for i in range(len(x)):
            redDotsx.append(x[i])
            redDotsy.append(y[i])
        matplotlib.pyplot.plot(x,y,'.',color='red',mec='None',alpha=0.5)

    inter=scipy.interpolate.UnivariateSpline(redDotsx,redDotsy)
    xnew=numpy.linspace(min(redDotsx),max(redDotsx),num=100,endpoint=True)
    matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='red',lw=2,label='after caffeine')

    matplotlib.pyplot.legend(frameon='False')
    matplotlib.pyplot.xlabel('log P - log C signal')
    matplotlib.pyplot.ylabel('p')
    theTitle=outputFileName.split('.')[-2]
    matplotlib.pyplot.title(theTitle)

    matplotlib.pyplot.xlim([0.1,1.8])
    matplotlib.pyplot.ylim([-0.025,0.35])

    matplotlib.pyplot.tight_layout()
    
    matplotlib.pyplot.savefig(outputFileName)
    matplotlib.pyplot.clf()
   
    return None

def individualHistoPlotter(before,after,outputFileName):

    '''
    this function creates figures with single data to model fits.
    '''

    count=0
    integralsBefore=[]
    integralsAfter=[]
    
    
    
    for element in before:
        x,y=histogrammer(element)
        matplotlib.pyplot.plot(x,y,'.',color='blue',mec='None',alpha=0.25)

        inter=scipy.interpolate.UnivariateSpline(x,y,k=5,s=1e-3)
        integral=inter.integral(min(x),max(x))
        integralsBefore.append(integral)
        xnew=numpy.linspace(min(x),max(x),num=100,endpoint=True)
        matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='blue')

        matplotlib.pyplot.xlabel('log peroxisomal signal')
        matplotlib.pyplot.ylabel('p')
        matplotlib.pyplot.xlim([0,1.8])
        matplotlib.pyplot.ylim([-0.033,0.33])

        count=count+1
        newName=outputFileName.replace('.pdf','_blue_%s.pdf'%count)
        matplotlib.pyplot.savefig(newName)
        matplotlib.pyplot.clf()

    count=0
    for element in after:
        x,y=histogrammer(element)
        matplotlib.pyplot.plot(x,y,'.',color='red',mec='None',alpha=0.25)

        inter=scipy.interpolate.UnivariateSpline(x,y,k=5,s=1e-3)
        integral=inter.integral(min(x),max(x))
        integralsAfter.append(integral)
        xnew=numpy.linspace(min(x),max(x),num=100,endpoint=True)
        matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='red')

        matplotlib.pyplot.xlabel('log peroxisomal signal')
        matplotlib.pyplot.ylabel('p')
        matplotlib.pyplot.xlim([0,1.8])
        matplotlib.pyplot.ylim([-0.033,0.33])

        count=count+1
        newName=outputFileName.replace('.pdf','_red_%s.pdf'%count)
        matplotlib.pyplot.savefig(newName)
        matplotlib.pyplot.clf()

    print '### ',outputFileName
    print '### before',integralsBefore
    print '### after',integralsAfter
    print
   
    return None

def multipleHistoPlotter(before,after,outputFileName):

    '''
    this function creates figures with multiple histograms, one for each image.
    '''

    matplotlib.rc('xtick', labelsize=22) 
    matplotlib.rc('ytick', labelsize=22)
    matplotlib.rc('font',size=28)

    integralsBefore=[]
    integralsAfter=[]
    
    for element in before:
        x,y=histogrammer(element)
        matplotlib.pyplot.plot(x,y,'.',color='blue',mec='None',alpha=0.25)

        inter=scipy.interpolate.UnivariateSpline(x,y,k=5,s=1e-3)
        integral=inter.integral(min(x),max(x))
        integralsBefore.append(integral)
        xnew=numpy.linspace(min(x),max(x),num=100,endpoint=True)
        matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='blue')

    for element in after:
        x,y=histogrammer(element)
        matplotlib.pyplot.plot(x,y,'.',color='red',mec='None',alpha=0.25)

        inter=scipy.interpolate.UnivariateSpline(x,y,k=5,s=1e-3)
        integral=inter.integral(min(x),max(x))
        integralsAfter.append(integral)
        xnew=numpy.linspace(min(x),max(x),num=100,endpoint=True)
        matplotlib.pyplot.plot(xnew,inter(xnew),'-',color='red')

    matplotlib.pyplot.xlabel('log P - log C signal')
    matplotlib.pyplot.ylabel('p')

    theTitle=outputFileName.split('.')[-2]
    matplotlib.pyplot.title(theTitle)

    matplotlib.pyplot.xlim([0.1,1.8])
    matplotlib.pyplot.ylim([-0.025,0.35])

    matplotlib.pyplot.tight_layout()

    matplotlib.pyplot.savefig(outputFileName)
    matplotlib.pyplot.clf()

    print '### ',outputFileName
    print '### before',integralsBefore
    print '### after',integralsAfter
    print
   
    return None

def statisticalTestRunner(before,after,case,generation):

    '''
    this function performs a Mann-Whitney U test.
    '''

    a=[]
    b=[]

    for element in before:
        for sub in element:
            a.append(sub)
    for element in after:
        for sub in element:
            b.append(sub)

    statistic,pvalue=scipy.stats.mannwhitneyu(a,b)

    print 'statistics on case',case,'and generation',generation,':',statistic,pvalue
    print 'mean before',numpy.mean(a)
    print 'mean after',numpy.mean(b)

    return None
