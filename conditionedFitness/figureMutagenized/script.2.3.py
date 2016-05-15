import matplotlib,numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# mutagenized 2.3

xSignal=numpy.array([[205,162,175,200,150],[35,33,50,48,45]])
xNoSignal=numpy.array([[190,166,175,145,139],[47,49,33,31,36]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[126,116,139,114,112],[55,53,56,54,46]])
xNoSignal=numpy.array([[115,143,135,123,142],[60,70,62,71,65]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[97,126,132,140,168],[124,105,124,114]])
xNoSignal=numpy.array([[139,130,157,132,120],[113,150,116,95,127]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[161,149,143,154,140],[155,134,131,167,151]])
xNoSignal=numpy.array([[148,176,172,184,185],[141,172,160,146,140]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[198,149,151,203,168],[133,143,147,139,144]])
xNoSignal=numpy.array([[193,187,195,183,171],[147,149,147,145,136]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[154,177,177,176,160],[159,176,177,172,179]])
xNoSignal=numpy.array([[171,161,220,194,180],[142,170,143,150,162]])
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

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.4,0.4])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.mutagenized.2.3.pdf')
matplotlib.pyplot.clf()
