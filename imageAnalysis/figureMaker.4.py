### this is the final script to make the graphs on distribution shifts

import sys,scipy,matplotlib,numpy
from matplotlib import pyplot
from scipy import stats

sys.path.append('../lib')
import library
import thresholdsCase1

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})

### MAIN

# 0. defining variables
case='case.1'
generations=['n0','n50','n100','n150','n200','n250']
thresholds=thresholdsCase1.definer()

### working on each experiment

x=[0,1,2,3,4,5]
eps=0.0
barWidth=0.33

for i in range(len(thresholds)):

    # 1. reading data
    print
    print 'reading the data...'

    before=library.dataReader(case,generations[i],thresholds[i][0],'without')
    after=library.dataReader(case,generations[i],thresholds[i][1],'with')

    averagesBefore=[numpy.mean(element) for element in before]
    averagesAfter=[numpy.mean(element) for element in after]
    
    print averagesBefore
    print averagesAfter

    statistic,pvalue=scipy.stats.mannwhitneyu(averagesBefore,averagesAfter)

    print 'statistics:',statistic,pvalue

    xPos=x[i]-barWidth/2.
    increment=numpy.mean(averagesAfter)-numpy.mean(averagesBefore)
    noise=numpy.sqrt(numpy.var(averagesBefore)+numpy.var(averagesAfter))
    matplotlib.pyplot.bar(xPos,increment,width=barWidth,color='black',edgecolor='None')
    matplotlib.pyplot.errorbar(xPos+barWidth/2.,increment,yerr=noise,fmt='None',ecolor='black',lw=2)

####
matplotlib.pyplot.hlines(y=0, xmin=0., xmax=5., colors='k', linestyles='--')
matplotlib.pyplot.text(0,0.275,'(*)',fontsize=22,horizontalalignment='center')
matplotlib.pyplot.text(3,0.275,'(**)',fontsize=22,horizontalalignment='center')
matplotlib.pyplot.text(4,0.275,'(*)',fontsize=22,horizontalalignment='center')
matplotlib.pyplot.text(5,0.275,'(*)',fontsize=22,horizontalalignment='center')

matplotlib.pyplot.xticks([0,1,2,3,4,5],['0','50','100','150','200','250'])

matplotlib.pyplot.xlim([-0.5,5.5])
matplotlib.pyplot.ylim([-0.5,0.35])
matplotlib.pyplot.yticks([-0.30,-0.15,0,0.15,0.30])

matplotlib.pyplot.xlabel('generation')
matplotlib.pyplot.ylabel(r'$\Delta$signal (perox.)')

matplotlib.pyplot.tight_layout()

matplotlib.pyplot.savefig('../figures/finalFigure4.pdf')

    

print
print '... completed.'
    
