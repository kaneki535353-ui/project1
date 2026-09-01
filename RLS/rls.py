import random

#define the random local search algorithm on onemax
def rls_onemax(n, max_iterations):
    #random initial solution
    x=[random.randint(0, 1) for _ in range(n)]
    iteration=0
    while iteration<max_iterations:
        iteration=iteration+1
        #randomly select one bit to flip
        i=random.randrange(n)
        y=x.copy()
        y[i]=1-y[i]
        #Selection
        if sum(y)>=sum(x):
            x=y
        #stop if the optimal solution is found
        if sum(x)==n:
            break
    #check whether optimum was found
    if sum(x)==n:
        success=True
    else:
        success=False
    return iteration, success




#define the random local search algorithm on leadingones
def leading_ones(x):
    fitness=0
    for bit in x:
        if bit == 1:
            fitness=fitness+1
        else:
            break
    return fitness  

def rls_leadingones(n, max_iterations):
    #random initial solution
    x=[random.randint(0, 1) for _ in range(n)]
    iteration=0
    while iteration<max_iterations:
        iteration=iteration+1
        #randomly select one bit to flip
        i=random.randrange(n)
        y=x.copy()
        y[i]=1-y[i]
        #Selection
        if leading_ones(y)>=leading_ones(x):
            x=y
        #stop if the optimal solution is found
        if leading_ones(x)==n:
            break
    #check whether optimum was found
    if leading_ones(x)==n:
        success=True
    else:
        success=False
    return iteration, success