import numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'

# engineered 1.1

xSignal=numpy.array([[237,201,217,181,171],[91,86,74,67,71]])
xNoSignal=numpy.array([[191,207,153,176,222],[87,133,109,103,100]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[138,140,125,136,103],[73,74,65,67,58]])
xNoSignal=numpy.array([[133,117,124,123,108],[66,73,55,60,65]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[123,148,108],[138,134,122]])
xNoSignal=numpy.array([[114,121,133],[114,121,100]])
cf_mu_190, cf_sd_190, pvalue_190 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[99,100,84,106,100],[133,139,115,126,127]])
xNoSignal=numpy.array([[74,116,124,130,112],[103,94,115,111,118]])
cf_mu_300, cf_sd_300, pvalue_300 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 190, 300]
y = [cf_mu_0, cf_mu_50, cf_mu_190, cf_mu_300]
z = [cf_sd_0, cf_sd_50, cf_sd_190, cf_sd_300]
w = [pvalue_0, pvalue_50, pvalue_190, pvalue_300]

print(y)

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

matplotlib.pyplot.savefig('figure.engineered.1.1.pdf')
matplotlib.pyplot.clf()

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'engineered.1.1.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()
