import matplotlib,numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# menadione 1

xSignal=numpy.array([[151,179,186,194,186],[114,108,96,127,123]])
xNoSignal=numpy.array([[159,203,192,225,168],[105,119,97,109,119]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[117,115,116,118,130],[61,87,63,85,69]])
xNoSignal=numpy.array([[139,111,100,102,112],[73,46,61,69,62]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[155,156,132],[86,102,120]])
xNoSignal=numpy.array([[170,180,175],[82,89,89]])
cf_mu_190, cf_sd_190, pvalue_190 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[119,79,50,95,83],[136,128,120,142,141]])
xNoSignal=numpy.array([[74,92,96,81,74],[141,97,127,114,132]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 190, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_190, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_190, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_190, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='orange',ecolor='orange',markeredgecolor='orange',capsize=0,ms=thePointSize,mew=0)

matplotlib.pyplot.tight_layout()

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
matplotlib.pyplot.ylim([-0.5,0.5])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])

matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')
matplotlib.pyplot.tight_layout(pad=0.5)
matplotlib.pyplot.savefig('figure.menadione.1.pdf')
matplotlib.pyplot.clf()

# menadione 2

xSignal=numpy.array([[188,179,157,189,175],[102,120,94,96,99]])
xNoSignal=numpy.array([[192,197,198,173,223],[84,87,76,95,85]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[135,142,146,110,134],[100,92,110,105,111]])
xNoSignal=numpy.array([[125,159,123,129,116],[75,79,71,66,63]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[151,151,174],[58,74,64]])
xNoSignal=numpy.array([[104,117,125],[86,93,94]])
cf_mu_190, cf_sd_190, pvalue_190 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[59,94,79,100,83],[91,114,104,115,109]])
xNoSignal=numpy.array([[89,57,50,71,97],[108,120,103,116,106]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 190, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_190, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_190, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_190, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='orange',ecolor='orange',markeredgecolor='orange',capsize=0,ms=thePointSize,mew=0)

for i in range(len(w)):
    if y[i] > 0.:
        sp=y[i]+0.1
    else:
        sp=y[i]-0.1
    if w[i] < 0.05 and w[i] >= 0.01:
        matplotlib.pyplot.scatter(x[i], sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
    if w[i] < 0.01:
        matplotlib.pyplot.scatter(x[i]-3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
        matplotlib.pyplot.scatter(x[i]+3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
        
matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')
matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.5,0.5])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')
matplotlib.pyplot.tight_layout(pad=0.5)
matplotlib.pyplot.savefig('figure.menadione.2.pdf')
matplotlib.pyplot.clf()

# menadione 3

xSignal=numpy.array([[199,159,173,153,207],[95,108,110,100,98]])
xNoSignal=numpy.array([[148,190,124,145,146],[99,76,91,95,72]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[107,154,115,143,142],[110,99,107,112,99]])
xNoSignal=numpy.array([[109,122,135,152,133],[76,65,89,100,80]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[150,155,198],[117,129,137]])
xNoSignal=numpy.array([[184,186,202],[123,153,166]])
cf_mu_190, cf_sd_190, pvalue_190 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[129,164,194,157,186],[182,213,203,163,207]])
xNoSignal=numpy.array([[203,195,149,187,128],[180,187,196,188,194]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 190, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_190, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_190, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_190, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='orange',ecolor='orange',markeredgecolor='orange',capsize=0,ms=thePointSize,mew=0)

for i in range(len(w)):
    if y[i] > 0.:
        sp=y[i]+0.1
    else:
        sp=y[i]-0.1
    if w[i] < 0.05 and w[i] >= 0.01:
        matplotlib.pyplot.scatter(x[i], sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
    if w[i] < 0.01:
        matplotlib.pyplot.scatter(x[i]-3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')
        matplotlib.pyplot.scatter(x[i]+3, sp, s=75, c='black', marker=r"${*}$", edgecolors='none')

matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')
matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.5,0.5])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')
matplotlib.pyplot.tight_layout(pad=0.5)
matplotlib.pyplot.savefig('figure.menadione.3.pdf')
matplotlib.pyplot.clf()
