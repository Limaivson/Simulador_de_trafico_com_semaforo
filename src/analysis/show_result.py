import json
from numpy import mean
import matplotlib.pylab as plt


results = {'with ai': {}, 'without ai': {}}

with open('results_with_ai.json', 'r') as f_with_ai:
    with open('results_no_ai.json', 'r') as f_without_ai:
        data_ai = json.load(f_with_ai)
        data_no_ai = json.load(f_without_ai)
        for i in range(60):
            road = f"Road {i}"
            total_wait = []
            total_amount = []
            for sim in data_ai:
                if road in data_ai[sim]:
                    total_wait.append(float(data_ai[sim][road][1]))

            if total_wait:
                total_wait = mean(total_wait)
            else:
                total_wait = 0

            results['with ai'][i] = total_wait

            total_wait = []
            total_amount = []
            for sim in data_no_ai:
                if road in data_no_ai[sim]:
                    total_wait.append(float(data_no_ai[sim][road][1].replace("Car mean wait: ", "")))

            if total_wait:
                total_wait = mean(total_wait)
            else:
                total_wait = 0

            results['without ai'][i] = total_wait

    results_ai = sorted(results['with ai'].items())  # sorted by key, return a list of tuples
    results_default = sorted(results['without ai'].items())

    x_with, y_with = zip(*results_ai)  # unpack a list of pairs into two tuples
    x_without, y_without = zip(*results_default)

    plt.plot(x_with, y_with, label="Com Algoritmo")
    plt.plot(x_without, y_without, label="Sem Algoritmo")
    plt.ylim((0, 55))
    plt.legend()
    plt.title("Comparação de tempos de espera médios")
    plt.grid()
    plt.show()
