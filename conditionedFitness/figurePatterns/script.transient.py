import pickle
import statsmodels,statsmodels.api
import matplotlib,matplotlib.pyplot
matplotlib.rcParams.update({'font.size':36,'font.family':'Arial','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# 0. user defined variables
jarDir='/Users/adriandelomana/scratch/'

# sustained trajectories
selected=['clonal.3.2','engineered.1.2','mutagenized.3.1','mutagenized.3.2','mutagenized.3.3'] 

# 1. iterate over selected trajectories
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

    
    matplotlib.pyplot.plot(x,y,color='blue',lw=2,zorder=100)
    
    # plot
    matplotlib.pyplot.errorbar(x,y,yerr=z,fmt='o',color='black',ecolor='black',markeredgecolor='black',capsize=0,ms=thePointSize,mew=0,alpha=0.33)


# close figure
matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.44,0.44])
matplotlib.pyplot.xticks([0,100,200,300])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned\nFitness')
matplotlib.pyplot.text(120,-0.38,'Transient',color='blue')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.transient.pdf')
