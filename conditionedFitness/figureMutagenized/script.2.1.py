import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'

# mutagenized 2.1

xSignal=numpy.array([[182,151,190,165,156],[25,33,24,35,24]])
xNoSignal=numpy.array([[137,147,175,175,139],[46,42,39,36,34]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[130,114,90,113,126],[28,20,22,25,20]])
xNoSignal=numpy.array([[128,131,120,121,129],[29,37,47,25,40]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[82,83,107,90,56],[67,52,45,56,55]])
xNoSignal=numpy.array([[82,104,88,87,80],[57,69,76,83]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[196,174,163,169,192],[155,157,159,146,155]])
xNoSignal=numpy.array([[158,147,154,146,130],[156,176,175,139,144]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[164,166,178,187,182],[153,121,159,141,134]])
xNoSignal=numpy.array([[237,212,194,210,189],[142,166,131,157,151]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[188,175,180,209,148],[154,126,146,120,179]])
xNoSignal=numpy.array([[200,181,181,188,192],[120,160,168,147,153]])
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

matplotlib.pyplot.savefig('figure.mutagenized.2.1.pdf')
matplotlib.pyplot.clf()

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'mutagenized.2.1.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()
