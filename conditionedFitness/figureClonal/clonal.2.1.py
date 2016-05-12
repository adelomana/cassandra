import matplotlib,numpy,sys,scipy
import matplotlib.pyplot
sys.path.append('/Users/alomana/gDrive2/projects/centers/ap/src/assessmentGraphs/publicationFigures/lib')
import calculateStatistics

### MAIN


matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# clonal 2

xSignal=numpy.array([[166,168,163,185,161],[8,7,14,8,13]])
xNoSignal=numpy.array([[194,201,191,190,175],[21,21,36,22,22]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[137,133,104,121,127],[49,57,56,56,47]])
xNoSignal=numpy.array([[123,112,136,104,95],[59,48,40,53,56]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[86,113,97,121,125],[81,73,66,67,75]])
xNoSignal=numpy.array([[112,101,107,118,108],[79,86,90,83,74]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[165,191,179,216,173],[195,171,153,171,173]])
xNoSignal=numpy.array([[209,167,181,209,189],[149,197,150,144,189]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[176,208,199,197,165],[145,118,135,142,132]])
xNoSignal=numpy.array([[215,250,208,211,210],[135,130,138,139,123]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[181,203,227,223,211],[149,175,147,179,183]])
xNoSignal=numpy.array([[213,185,206,217,213],[156,131,139,144,156]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 100, 150, 200, 250]
y = [cf_mu_0, cf_mu_50, cf_mu_100, cf_mu_150, cf_mu_200, cf_mu_250]
z = [cf_sd_0, cf_sd_50, cf_sd_100, cf_sd_150, cf_sd_200, cf_sd_250]
w = [pvalue_0, pvalue_50, pvalue_100, pvalue_150, pvalue_200, pvalue_250]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='green',ecolor='green',markeredgecolor='green',capsize=0,ms=thePointSize,mew=0)
print y

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

sequencing=[0,250]
top=-0.4
for xpos in sequencing:
    matplotlib.pyplot.scatter(xpos, top, s=400, c='black', marker=r"${\uparrow}$", edgecolors='none')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.4,0.4])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.clonal.2.1.pdf')
