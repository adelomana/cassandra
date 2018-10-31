import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'


# engineered 2.1

xSignal=numpy.array([[180,159,200,176,147],[12,11,5,7,13]])
xNoSignal=numpy.array([[163,166,168,151,182],[23,22,23,16,12]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[153,153,211,163,148],[43,39,37,36,56]])
xNoSignal=numpy.array([[171,152,188,201,194],[78,78,86,80,70]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[123,89,126,133,129],[109,104,124,128,109]])
xNoSignal=numpy.array([[147,117,159,142,156],[142,134,134,143,150]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[146,123,94,113,127],[128,105,152,127,141]])
xNoSignal=numpy.array([[148,161,166,147,145],[175,177,150,151,179]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[130,112,147,148,155],[181,142,162,163,180]])
xNoSignal=numpy.array([[181,157,210,177,166],[155,159,144,140,149]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[151,146,140,135,117],[127,96,139,122,122]])
xNoSignal=numpy.array([[144,134,159,159,142],[108,89,117,140,143]])
cf_mu_250, cf_sd_250, pvalue_250 = calculateStatistics.main(xSignal, xNoSignal)

x = [0, 50, 100, 150, 200, 250]
y = [cf_mu_0, cf_mu_50, cf_mu_100, cf_mu_150, cf_mu_200, cf_mu_250]
z = [cf_sd_0, cf_sd_50, cf_sd_100, cf_sd_150, cf_sd_200, cf_sd_250]
w = [pvalue_0, pvalue_50, pvalue_100, pvalue_150, pvalue_200, pvalue_250]

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

sequencing=[0,200,250]
top=-0.4
for xpos in sequencing:
    matplotlib.pyplot.scatter(xpos, top, s=400, c='black', marker=r"${\uparrow}$", edgecolors='none')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.55,0.55])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.engineered.2.1.pdf')
matplotlib.pyplot.clf()

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'engineered.2.1.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()
