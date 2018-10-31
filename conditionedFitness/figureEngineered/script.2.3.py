import matplotlib,numpy,sys,scipy,pickle
import matplotlib.pyplot
sys.path.append('../lib')
import calculateStatistics

### MAIN

matplotlib.rcParams.update({'font.size':36,'font.family':'Times New Roman','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

jarDir='/Users/adriandelomana/scratch/'


# engineered 2.3

xSignal=numpy.array([[177,158,203,174,122],[11,7,19,10,11]])
xNoSignal=numpy.array([[165,136,175,171,177],[15,19,16,19,14]])
cf_mu_0, cf_sd_0, pvalue_0 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[207,210,192,190,198],[78,86,61,76,53]])
xNoSignal=numpy.array([[218,206,189,203,209],[111,101,112,121,113]])
cf_mu_50, cf_sd_50, pvalue_50 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[115,112,121,124,114],[91,100,95,100]])
xNoSignal=numpy.array([[129,166,128,111,121],[105,87,110,88,104]])
cf_mu_100, cf_sd_100, pvalue_100 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[130,144,161,162,143],[177,144,174,157,159]])
xNoSignal=numpy.array([[194,206,150,190,165],[147,159,168,157,138]])
cf_mu_150, cf_sd_150, pvalue_150 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[197,195,242,244,211],[128,121,117,177,142]])
xNoSignal=numpy.array([[252,263,241,252,223],[122,158,128,145,130]])
cf_mu_200, cf_sd_200, pvalue_200 = calculateStatistics.main(xSignal, xNoSignal)

xSignal=numpy.array([[164,170,156,170,179],[151,134,153,131,123]])
xNoSignal=numpy.array([[157,196,173,178,181],[154,165,180,178,182]])
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

sequencing=[0,150]
top=-0.4
for xpos in sequencing:
    matplotlib.pyplot.scatter(xpos, top, s=400, c='black', marker=r"${\uparrow}$", edgecolors='none')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.55,0.55])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned Fitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.engineered.2.3.pdf')
matplotlib.pyplot.clf()

# save processed data alternative plotting
trajectory=[x,y,z]
jarFile=jarDir+'engineered.2.3.pickle'
f=open(jarFile,'wb')
pickle.dump(trajectory,f)
f.close()

