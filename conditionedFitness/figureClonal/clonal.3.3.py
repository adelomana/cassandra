import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'

# clonal 2

xSignal=numpy.array([[175, 153, 186, 189, 157],[37, 59, 46, 67, 70]])
xNoSignal=numpy.array([[200, 202, 224, 194, 193],[71, 66, 71, 87, 60]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[25, 28, 19, 18, 16],[0, 9, 4, 9, 1]])
xNoSignal=numpy.array([[24, 16, 29, 17, 23],[4, 7, 5, 3, 4]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[96, 97, 94, 127, 80],[32, 36, 36, 42, 36]])
xNoSignal=numpy.array([[104, 137, 110, 128, 113],[52, 36, 32, 50, 41]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[204, 223, 199, 249, 193],[141, 131, 125, 154, 139]])
xNoSignal=numpy.array([[171, 217, 240, 200, 168],[166, 192, 163, 196, 170]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[197, 216, 224, 219, 208],[181, 182, 186, 179, 116]])
xNoSignal=numpy.array([[261, 227, 229, 188, 236],[179, 169, 174, 183, 164]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[226, 214, 222, 224, 211],[235, 199, 177, 199, 184]])
xNoSignal=numpy.array([[223, 230, 215, 273, 245],[204, 199, 247, 220, 204]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[222, 235, 253, 234, 189],[175, 160, 194, 156, 178]])
xNoSignal=numpy.array([[212, 222, 246, 228, 220],[191, 192, 198, 217, 199]])
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

matplotlib.pyplot.savefig('figure.clonal.3.3.pdf')

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'clonal.3.3.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()
