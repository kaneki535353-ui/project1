import matplotlib.pyplot as plt

from rls import rls_onemax 

n_values=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

all_runtimes = []
average_runtime_nlogn=[]

for n in n_values:
    runtimes=[]
    max_iteration= n ** 3
    #run 20 times
    for run in range(20):
        iteration, success=rls_onemax(n, max_iteration)
        if success:
            runtimes.append(iteration)

#calculate average runtime
    if len(runtimes)>0:
        average_runtime=sum(runtimes)/len(runtimes)
    else:
        average_runtime=None

    print(
        "n=",n,
        "Successful runs=",len(runtimes),
         "Average runtime=",average_runtime
    )
    average_runtime_nlogn.append(average_runtime)
    all_runtimes.append(runtimes)

#plot
plt.plot(n_values, average_runtime_nlogn)

plt.xlabel("n")
plt.ylabel("Average runtime")

plt.title("Random Local Search on OneMax")
plt.show()


#Plot the boxplot
plt.boxplot(all_runtimes, tick_labels=n_values)
plt.xlabel("n")
plt.ylabel("Runtime")
plt.title("RLS on OneMax - Runtime Distribution")
plt.show()