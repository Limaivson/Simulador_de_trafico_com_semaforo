import json
from numpy import mean
import matplotlib.pylab as plt


results = {'mean amount': {}, 'mean wait': {}}


with open('results_no_ai.json', 'r') as f:
    data = json.load(f)
    for i in range(60):
        total_wait = []
        total_amount = []
        road = f"Road {i}"
        for sim in data:
            if road in data[sim]:
                total_wait.append(float(data[sim][road][1].replace('Car mean wait: ', '')))
                total_amount.append(float(data[sim][road][0].replace('Car mean amount: ', '')))

        if total_wait:
            total_wait = mean(total_wait)
        else:
            total_wait = 0

        if total_amount:
            total_amount = mean(total_amount)
        else:
            total_amount = 0

        results['mean wait'][i] = total_wait
        results['mean amount'][i] = total_amount

    lists = sorted(results['mean wait'].items())  # sorted by key, return a list of tuples

    x, y = zip(*lists)  # unpack a list of pairs into two tuples

    plt.plot(x, y)
    plt.title("Wait Times")
    plt.grid()
    plt.show()
    
    lists = sorted(results['mean amount'].items())  # sorted by key, return a list of tuples

    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    
    plt.plot(x, y)
    plt.title("Vehicle Amount")
    plt.grid()
    plt.show()
    # plt.savefig('wait_times')
