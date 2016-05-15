import numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# engineered 1.2

xSignal=numpy.array([[216,212,180,196,190],[49,50,59,60,61]])
xNoSignal=numpy.array([[195,186,164,228,159],[87,76,80,94,92]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[152,147,102,110,127,],[104,73,92,76,89]])
xNoSignal=numpy.array([[126,155,145,126,145],[72,60,61,61,67]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[116,124,87],[123,114,134]])
xNoSignal=numpy.array([[148,142,144],[125,94,104]])
cf_mu_190, cf_sd_190, pvalue_190 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[116,105,88,83,78],[96,126,135,118,118]])
xNoSignal=numpy.array([[79,81,101,92,114],[147,132,111,112,109]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 190, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_190, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_190, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_190, pvalue_300]

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

sequencing=[0,50,300]
top=-0.4
for xpos in sequencing:
    matplotlib.pyplot.scatter(xpos, top, s=400, c='black', marker=r"x", edgecolors='none')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.55,0.55])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.engineered.1.2.pdf')
matplotlib.pyplot.clf()
