# cassandra
Computational tool for the study of adaptive prediction emergence.  

1. define a set of n graphs. each graph is boolean network. activations and repressions are random and uniform.
2. define a set of m inputs and outputs. the number of inputs equals the number of outputs equals the number of nodes.  
3. define a subset of nodes which are "readers" and a subset of nodes that are "recievers". define the probability of being a  reader/reciever. a reader can be activated/repressed by a given signal.  
4. define best fitting response. for each input there will be a beneficial output. fitness will be the sum of good responses. 
5. evaluate the population under each EF.  
6. select.  
7. repeat iterations.  
8. equilibrate to high fitness of a inputs and outputs.  
9. define a new enviroment with previous EFs but now there is a new coupled pattern. new fitness should maintain the previous abilities, plus learn the new coupled EFs. consider a high benefit for the association of this new pattern.  
10. evaluate how emerges along time.  
