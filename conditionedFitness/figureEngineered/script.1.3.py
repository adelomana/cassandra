import numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# engineered 1.3

xSignal=numpy.array([[187,130,129,138,122],[64,59,71,70,68]])
xNoSignal=numpy.array([[166,150,165,167,152],[73,78,80,93,85]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[146,111,117,99,127],[80,74,71,59,59]])
xNoSignal=numpy.array([[103,124,98,138,120],[88,79,72,61,56]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[106,104,76],[60,76,87]])
xNoSignal=numpy.array([[108,102,112],[57,66,66]])
cf_mu_180, cf_sd_180, pvalue_180 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[109,93,80,87,98],[111,140,123,124,125]])
xNoSignal=numpy.array([[79,86,90,54,86],[96,112,118,102,115]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 180, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_180, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_180, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_180, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='blue',ecolor='blue',markeredgecolor='blue',capsize=0,ms=thePointSize,mew=0)

for i in range(len(w)):
    if y[i] > 0.:
        sp=y[i]+z[i]+0.02
    else:
        sp=y[i]-z[i]-0.02
    if w[i] < 0.05 and w[i] >= 0.01:
        matplotlib.pyplot.scatter(x[i], sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
    if w[i] < 0.01:
        matplotlib.pyplot.scatter(x[i]-3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
        matplotlib.pyplot.scatter(x[i]+3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')

matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.55,0.55])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.engineered.1.3.pdf')
matplotlib.pyplot.clf()
