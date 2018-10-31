import pickle,sys
import statsmodels,statsmodels.api
import matplotlib,matplotlib.pyplot
matplotlib.rcParams.update({'font.size':36,'font.family':'Arial','xtick.labelsize':28,'ytick.labelsize':28})
thePointSize=12

# 0. user defined variables
jarDir='/Users/adriandelomana/scratch/'

# sustained trajectories
clonal=['clonal.2.1','clonal.3.1','clonal.3.2','clonal.3.3']
engineered=['engineered.1.1','engineered.1.2','engineered.1.3','engineered.2.1','engineered.2.2','engineered.2.3'] 
mutagenized=['mutagenized.2.1','mutagenized.2.2','mutagenized.2.3','mutagenized.3.1','mutagenized.3.2','mutagenized.3.3'] 

selected=clonal+mutagenized+engineered

print(selected,len(selected))

# 1. iterate over selected trajectories
generalTrend={}
generalTrend[0]=[]
generalTrend[50]=[]
generalTrend[100]=[]
generalTrend[150]=[]
generalTrend[200]=[]
generalTrend[250]=[]
generalTrend[300]=[]

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

    for i in range(len(x)):
        assigned=None
        for defined in generalTrend.keys():
            if abs(defined-x[i]) < 25:
                assigned=defined
        generalTrend[assigned].append(y[i])

# make the figure
positions=list(generalTrend.keys())
positions.sort()
fitnessValues=[]
for position in positions:
    fitnessValues.append(generalTrend[position])

bp=matplotlib.pyplot.boxplot(fitnessValues,positions=positions,patch_artist=True,widths=20)

# close figure
matplotlib.pyplot.plot([0,300],[0,0],'--',color='black')

matplotlib.pyplot.xlim([-25,325])
matplotlib.pyplot.ylim([-0.44,0.44])
matplotlib.pyplot.xticks([0,100,200,300],[0,100,200,300])
matplotlib.pyplot.yticks([-0.4,-0.2,0,0.2,0.4])
matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Conditioned\nFitness')

matplotlib.pyplot.tight_layout(pad=0.5)

matplotlib.pyplot.savefig('figure.all.pdf')
