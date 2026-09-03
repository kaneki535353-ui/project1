import matplotlib.pyplot as plt

from one_plus_one_ea_changing_rate import one_plus_one_ea_onemax2

n=100

c_values = [0.1, 0.2, 0.5, 1, 1.5, 2, 2.5, 3]

average_runtimes=[]

for c in c_values:
    runtimes=[]
    max_iteration= n ** 3
    #run 20 times
    for run in range(20):
        iteration, success=one_plus_one_ea_onemax2(n, c, max_iteration)
        if success:
            runtimes.append(iteration)

#calculate average runtime
    if len(runtimes)>0:
        average_runtime=sum(runtimes)/len(runtimes)
    else:
        average_runtime=None

    print(
        "c=",c,
        "Successful runs=",len(runtimes),
         "Average runtime=",average_runtime
    )
    average_runtimes.append(average_runtime)

#plot
plt.plot(c_values, average_runtimes)

plt.xlabel("c")
plt.ylabel("Average runtime")

plt.title("(1+1)EA on OneMax")
plt.show()