import sys

'''
# is caffeine effect different in evolved? is it more similar to evolved FOA response (compared to naive, so it’s more resistant)?
# is it caffeine+FOA different in evolved? 

# for each cell line:
1) define the effect of caffeine.
2) define the effect of FOA.
3) define the effect of FOA + caffeine.
4) define a core effect over the 3 naive lines to define the above.

2) define if caffeine effect is different in the evolved line with respect to the naive one.
if it is the same in all 3 lines, that is the AP effect. Is that effect similar to FOA response in the evolved (but not the naive?) if so, that would be interesting (FOA resistance).

3) checked if 2 is true in the caffeine+FOA, i.e., similar effect in the evolved but not the naive, is actually similar to the "resisntace" effect, i.e., the differential response to FOA in the evolved but not naive strain
'''

### MAIN
cuffdiffDir='/Volumes/omics4tb/alomana/projects/ap/data/transcriptomics/cuffdiff/'

tubes=['l1','l2','l3']
evolution=['naive','evolved']
hypotheses=['h1','h2','h3','h4']

# 1. CAFFEINE EFFECTS
# 1.1. define caffeine effect for each line.
caffeineEffect={} # caffeineEffect[line1/line2/line3][naive/evolved][up/down]=[list of genes]

for tube in tubes:
    for state in evolution:
        for h in hypotheses:
            
            if tube not in caffeineEffect.keys():
                caffeineEffect[tube]={}
            if state not in caffeineEffect[tube].keys():
                caffeineEffect[tube][state]={}
            if h not in caffeineEffect[tube][state].keys():
                caffeineEffect[tube][state][h]=[]

            fileName='{}{}.{}.{}/gene_exp.diff'.format(cuffdiffDir,tube,state,h)
            with open(fileName,'r') as f:
                next(f)
                for line in f:
                    vector=line.split('\t')
                    if vector[-1] == 'yes\n':
                        geneName=vector[0].replace('gene:','')
                        caffeineEffect[tube][state][h].append(geneName)
# 1.2. defining consistent effect
caffeineEffectIntersectNaive= list(set(caffeineEffect['l1']['naive']['h1']) & set(caffeineEffect['l2']['naive']['h1']) & set(caffeineEffect['l3']['naive']['h1']))
caffeineEffectUnionNaive=list(set(caffeineEffect['l1']['naive']['h1']) | set(caffeineEffect['l2']['naive']['h1']) | set(caffeineEffect['l3']['naive']['h1']))
print('caffeine effect naive intersect: {} genes, out of {} {} {} genes per line.'.format(len(caffeineEffectIntersectNaive), len(caffeineEffect['l1']['naive']['h1']), len(caffeineEffect['l2']['naive']['h1']), len(caffeineEffect['l3']['naive']['h1'])))
print('caffeine effect naive union: {} genes.'.format(len(caffeineEffectUnionNaive)))

current=list(set(caffeineEffect['l1']['naive']['h1']) & set(caffeineEffect['l2']['naive']['h1']))
print('intersect l1 and l2: {} genes.'.format(len(current)))

current=list(set(caffeineEffect['l1']['naive']['h1']) & set(caffeineEffect['l3']['naive']['h1']))
print('intersect l1 and l3: {} genes.'.format(len(current)))

current=list(set(caffeineEffect['l2']['naive']['h1']) & set(caffeineEffect['l3']['naive']['h1']))
print('intersect l2 and l3: {} genes.'.format(len(current)))

union23=list(set(caffeineEffect['l2']['naive']['h1']) | set(caffeineEffect['l3']['naive']['h1']))
unique1=[element for element in caffeineEffect['l1']['naive']['h1'] if element not in union23]
print('unique1: {} genes.'.format(len(unique1)))

union13=list(set(caffeineEffect['l1']['naive']['h1']) | set(caffeineEffect['l3']['naive']['h1']))
unique2=[element for element in caffeineEffect['l2']['naive']['h1'] if element not in union13]
print('unique2: {} genes.'.format(len(unique2)))

union12=list(set(caffeineEffect['l1']['naive']['h1']) | set(caffeineEffect['l2']['naive']['h1']))
unique3=[element for element in caffeineEffect['l3']['naive']['h1'] if element not in union12]
print('unique3: {} genes.'.format(len(unique3)))

print('core DETs...')          
for element in caffeineEffectIntersectNaive:
    print(element)

print('specific DETs...')
for tube in tubes:
    print(tube)
    DETs=caffeineEffect[tube]['naive']['h1']
    for DET in DETs:
        print(DET)
        
# 1.3. define caffeine effects in evolved lines and see how different they are to naive
caffeineEffectIntersectEvolved= list(set(caffeineEffect['l1']['evolved']['h1']) & set(caffeineEffect['l2']['evolved']['h1']) & set(caffeineEffect['l3']['evolved']['h1']))
print('caffeine effect evolved intersect: {} genes, out of {} {} {} genes per line'.format(len(caffeineEffectIntersectEvolved),len(caffeineEffect['l1']['evolved']['h1']), len(caffeineEffect['l2']['evolved']['h1']), len(caffeineEffect['l3']['evolved']['h1'])))
caffeineEffectUnionEvolved=list(set(caffeineEffect['l1']['evolved']['h1']) | set(caffeineEffect['l2']['evolved']['h1']) | set(caffeineEffect['l3']['evolved']['h1']))
print('caffeine effect evolved union: {} genes.'.format(len(caffeineEffectUnionEvolved)))

current=list(set(caffeineEffect['l1']['evolved']['h1']) & set(caffeineEffect['l2']['evolved']['h1']))
print('intersect l1 and l2: {} genes.'.format(len(current)))

current=list(set(caffeineEffect['l1']['evolved']['h1']) & set(caffeineEffect['l3']['evolved']['h1']))
print('intersect l1 and l3: {} genes.'.format(len(current)))

current=list(set(caffeineEffect['l2']['evolved']['h1']) & set(caffeineEffect['l3']['evolved']['h1']))
print('intersect l2 and l3: {} genes.'.format(len(current)))

union23=list(set(caffeineEffect['l2']['evolved']['h1']) | set(caffeineEffect['l3']['evolved']['h1']))
unique1=[element for element in caffeineEffect['l1']['evolved']['h1'] if element not in union23]
print('unique1: {} genes.'.format(len(unique1)))

union13=list(set(caffeineEffect['l1']['evolved']['h1']) | set(caffeineEffect['l3']['evolved']['h1']))
unique2=[element for element in caffeineEffect['l2']['evolved']['h1'] if element not in union13]
print('unique2: {} genes.'.format(len(unique2)))

union12=list(set(caffeineEffect['l1']['evolved']['h1']) | set(caffeineEffect['l2']['evolved']['h1']))
unique3=[element for element in caffeineEffect['l3']['evolved']['h1'] if element not in union12]
print('unique3: {} genes.'.format(len(unique3)))

for element in caffeineEffectIntersectEvolved:
    print(element)

# 1.4. define evolved-specific effect
caffeineEffectEvolvedSpecific=[element for element in caffeineEffectIntersectEvolved if element not in caffeineEffectIntersectNaive]
print('caffeine effects evolved-specific (core): {}'.format(caffeineEffectEvolvedSpecific))

# 1.5. line by line, which are DETs not present in naive core?
for tube in tubes:
    new=[element for element in caffeineEffect[tube]['evolved']['h1'] if element not in caffeineEffectUnionNaive]
    print('{}, {} evolved-specific DETs in caffeine.'.format(tube,len(new)))
    for element in new:
        print(element)




