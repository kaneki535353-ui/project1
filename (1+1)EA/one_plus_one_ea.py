import random

#define the (1+1)EA algorithm on onemax
def one_plus_one_ea_onemax(n, max_iterations):
    #random initial solution
    x=[random.randint(0, 1) for _ in range(n)]
    iteration=0
    while iteration<max_iterations:
        iteration=iteration+1
        #each bit is flipped independently with probability 1/n
        y=x.copy()
        for i in range(n):
            if random.random()<1/n:
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




#define the (1+1)EA algorithm on leadingones
def leading_ones(x):
    fitness=0
    for bit in x:
        if bit == 1:
            fitness=fitness+1
        else:
            break
    return fitness  

def one_plus_one_ea_leadingones(n, max_iterations):
    #random initial solution
    x=[random.randint(0, 1) for _ in range(n)]
    iteration=0
    while iteration<max_iterations:
        iteration=iteration+1
        #each bit is flipped independently with probability 1/n
        y=x.copy()
        for i in range(n):
            if random.random()<1/n:
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