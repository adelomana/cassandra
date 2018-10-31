import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'

# clonal 2

xSignal=numpy.array([[187, 144, 166, 171, 158],[77, 78, 60, 61, 49]])
xNoSignal=numpy.array([[170, 143, 163, 141, 162],[56, 35, 45, 73, 42]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[200, 171, 173, 176, 199],[174, 176, 147, 186, 197]])
xNoSignal=numpy.array([[203, 218, 231, 210, 210],[124, 125, 130, 161, 145]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[153, 154, 124, 167, 157],[126, 161, 115, 114, 110]])
xNoSignal=numpy.array([[187, 179, 175, 160, 150],[127, 151, 115, 133, 89]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[188, 207, 186, 183, 193],[155, 162, 161, 160, 145]])
xNoSignal=numpy.array([[202, 185, 237, 217, 186],[136, 162, 139, 151, 146]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[183, 202, 205, 214, 213],[200, 144, 185, 159, 168]])
xNoSignal=numpy.array([[255, 221, 218, 213, 235],[221, 201, 185, 176, 166]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[230, 236, 189, 235, 235],[177, 202, 174, 195, 182]])
xNoSignal=numpy.array([[247, 227, 246, 219, 246],[181, 201, 182, 202, 181]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[239, 240, 257, 231, 241],[214, 186, 165, 174, 164]])
xNoSignal=numpy.array([[238, 219, 255, 269, 213],[197, 211, 184, 198, 212]])
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

matplotlib.pyplot.savefig('figure.clonal.3.1.pdf')

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'clonal.3.1.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()

