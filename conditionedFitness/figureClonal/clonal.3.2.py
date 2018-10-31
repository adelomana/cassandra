import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'

# clonal 2

xSignal=numpy.array([[189, 181, 186, 169, 176],[50, 55, 53, 47, 65]])
xNoSignal=numpy.array([[155, 168, 173, 196, 175],[63, 76, 59, 66, 75]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[154, 154, 148, 152, 125],[99, 122, 105, 98, 97]])
xNoSignal=numpy.array([[149, 178, 159, 144, 148],[78, 110, 95, 91, 104]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[189, 182, 184, 193, 164],[106, 127, 136, 138, 120]])
xNoSignal=numpy.array([[233, 185, 218, 205, 199],[153, 124, 125, 126, 169]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[199, 199, 202, 258, 205],[175, 158, 142, 146, 130]])
xNoSignal=numpy.array([[214, 205, 215, 174, 227],[176, 153, 171, 167, 170]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[273, 239, 260, 269, 231],[175, 187, 161, 184, 187]])
xNoSignal=numpy.array([[263, 271, 248, 292, 252],[204, 198, 202, 171, 188]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[217, 190, 243, 208, 192],[190, 184, 176, 174, 196]])
xNoSignal=numpy.array([[249, 218, 255, 254, 217],[177, 191, 162, 172, 176]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[274, 254, 237, 243, 284],[187, 181, 153, 156, 197]])
xNoSignal=numpy.array([[283, 289, 268, 255, 280],[202, 177, 195, 209, 173]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 100, 150, 200, 250, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_100, cf_mu_150, cf_mu_200, cf_mu_250, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_100, cf_sd_150, cf_sd_200, cf_sd_250, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_100, pvalue_150, pvalue_200, pvalue_250, pvalue_300]

matplotlib.pyplot.errorbar(x,y,yerr=z,fmt=':o',color='green',ecolor='green',markeredgecolor='green',capsize=0,ms=thePointSize,mew=0)

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

matplotlib.pyplot.savefig('figure.clonal.3.2.pdf')

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'clonal.3.2.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()
