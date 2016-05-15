import matplotlib,numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# mutagenized 2.2

xSignal=numpy.array([[190,167,136,200,172],[34,43,49,47,46]])
xNoSignal=numpy.array([[173,159,157,179,167],[48,45,44,41,27]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[157,114,152,136,160],[29,39,41,36,43]])
xNoSignal=numpy.array([[151,121,144,158,156],[69,71,64,80,58]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[139,114,133,153,121],[115,114,140,129,158]])
xNoSignal=numpy.array([[129,105,120,129,120],[149,140,119,98,115]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[137,136,129,164,179],[144,140,122,160,154]])
xNoSignal=numpy.array([[174,182,177,167,160],[139,134,153,139,132]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[155,148,149,145,146],[146,118,127,105,132]])
xNoSignal=numpy.array([[202,211,151,170,174],[110,132,105,109,118]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[159,180,164,185,167],[169,177,166,151,171]])
xNoSignal=numpy.array([[192,196,215,181,161],[148,161,158,123]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 100, 150, 200, 250]
y = [cf_mu_0, cf_mu_50, cf_mu_100, cf_mu_150, cf_mu_200, cf_mu_250]
z = [cf_sd_0, cf_sd_50, cf_sd_100, cf_sd_150, cf_sd_200, cf_sd_250]
w = [pvalue_0, pvalue_50, pvalue_100, pvalue_150, pvalue_200, pvalue_250]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='red',ecolor='red',markeredgecolor='red',capsize=0,ms=thePointSize,mew=0)

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

sequencing=[0,150]
top=-0.4
for xpos in sequencing:
    matplotlib.pyplot.scatter(xpos, top, s=400, c='black', marker=r"${\uparrow}$", edgecolors='none')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.4,0.4])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.mutagenized.2.2.pdf')
matplotlib.pyplot.clf()
