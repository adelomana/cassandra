import pickle
import statsmodels,statsmodels.api
import matplotlib,matplotlib.pyplot
matplotlib.rcParams.update({'font.size':36,'font.family':'Arial','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# 0. user defined variables
jarDir='/Users/adriandelomana/scratch/'

# sustained trajectories
selected=['clonal.2.1','engineered.1.1','engineered.2.2','mutagenized.2.2'] # should be n = 6

# 1. iterate over selected trajectories
allx=[]; ally=[]
for replicate in selected:

    print(replicate)
    
    # read jar file
    jarFile=jarDir+replicate+'.pickle'
    f=open(jarFile,'rb')
    trajectory=pickle.load(f)
    f.close()

    # recover data into a format amenable to plotting
    x=trajectory[0]
    y=trajectory[1]
    z=trajectory[2]

    for a,b in zip(x,y):
        allx.append(a)
        ally.append(b)

    # run lowess over each replicate. if lowess does not work, do correlation. if not pchip
    
    # plot
    matplotlib.pyplot.errorbar(x,y,yerr=z,fmt='o',color='black',ecolor='black',markeredgecolor='black',capsize=0,ms=thePointSize,mew=0,alpha=0.33)


# run lowess over all data
lowess = statsmodels.api.nonparametric.lowess(ally,allx,it=10)
matplotlib.pyplot.plot(lowess[:, 0], lowess[:, 1],color='red',lw=4,zorder=100)

# close figure
matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.44,0.44])
matplotlib.pyplot.xticks([0,100,200,300])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned\nFitness')
#matplotlib.pyplot.text(-20,0.3,'Sustained')
matplotlib.pyplot.text(120,-0.38,'Sustained',color='red')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.sustained.pdf')
