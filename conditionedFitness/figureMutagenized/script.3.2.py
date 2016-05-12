import matplotlib,numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics, dataReader3rdExperiment

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# mutagenized 3.2

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=0, label='M2')
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=50, label='M2')
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=100, label='M2')
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=150, label='M2')
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=200, label='M2')
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=250, label='M2')
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

xSignal, xNoSignal = dataReader3rdExperiment.main(generation=300, label='M2')
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 100, 150, 200, 250, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_100, cf_mu_150, cf_mu_200, cf_mu_250, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_100, cf_sd_150, cf_sd_200, cf_sd_250, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_100, pvalue_150, pvalue_200, pvalue_250, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='red',ecolor='red',markeredgecolor='red',capsize=0,ms=thePointSize,mew=0)

print max(y),y

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
matplotlib.pyplot.ylim([-0.4,0.4])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.mutagenized.3.2.pdf')
matplotlib.pyplot.clf()
