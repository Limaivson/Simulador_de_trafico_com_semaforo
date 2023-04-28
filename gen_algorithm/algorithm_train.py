from fitness_function import fitness_func
from model_traffic_light import TrafficLight
from random import randint


def initial_pop(matrix_size: int):
    t_min_change = (TrafficLight.time_min_range[1] - TrafficLight.time_min_range[0]) / (matrix_size - 1)
    t_max_change = (TrafficLight.time_max_range[1] - TrafficLight.time_max_range[0]) / (matrix_size - 1)
    coef_change  = (TrafficLight.coef_range[1]     - TrafficLight.coef_range[0])     / (matrix_size - 1)

    initial_population = []

    t_min = TrafficLight.time_min_range[0]
    for i in range(matrix_size):
        t_max = TrafficLight.time_max_range[0]
        for j in range(matrix_size):
            coef = TrafficLight.coef_range[0]
            for k in range(matrix_size):
                initial_population.append(TrafficLight(t_min, t_max, coef))
                coef += coef_change
            t_max += t_max_change
        t_min += t_min_change

    return initial_population

def rank(population: list, train_type: int) -> list:
    """Rank of the population for the worst resulto to the better"""
    score_holder = {}
    for individual in population:
        score = fitness_func(individual, train_type)
        score_holder[score] = individual
    score_list = list(score_holder.keys())
    score_list.sort(reverse=True)
    ranked_list = []
    for i in range(len(score_list)):
        ranked_list.append(score_holder[score_list[i]])
    return ranked_list

def cruze(population: list) -> list:
    """Generates the nex population"""
    chances = []
    for i in range(len(population)):
        if i == 0:
            chances.append(1)
        else:
            chance = chances[-1] + 2**i
            chances.append(chance)

    new_population = []

    while len(new_population) < len(population) - 2:
        ind_1 = 0
        ind_2 = 0
        while ind_1 == ind_2:
            draw = randint(1, chances[-1])
            for index in range(len(chances)):
                if draw > chances[index]:
                    ind_index = index + 1
                elif draw == chances[index]:
                    ind_index = index
            ind_1 = population[ind_index]

            draw = randint(1, chances[-1])
            for index in range(len(chances)):
                if draw > chances[index]:
                    ind_index = index + 1
                elif draw == chances[index]:
                    ind_index = index
            ind_2 = population[ind_index]
        new_population.append(ind_1 + ind_2)
    
    new_population.append(population[-2])
    new_population.append(population[-1])

    return(new_population)

def train(train_type: int, matrix_size: int) -> TrafficLight:
    population = initial_pop(matrix_size)
    population = rank(population, train_type)
    perpetuation = 0
    gen = 1

    while perpetuation < 10:
        better_ind = population[-1]
        population = cruze(population)
        population = rank(population, train_type)
        if population[-1].get_configuration() == better_ind.get_configuration():
            perpetuation += 1
        else:
            perpetuation = 0
        gen += 1
        print("Gen:", gen, "\tPerp:", perpetuation)
        print(f"\t{better_ind}\t{fitness_func(better_ind, train_type)}\n")

    return better_ind

if __name__ == "__main__":
    with open("results_2.log", "r") as archive:
        text = archive.read()
    for i in range(10):
        ind = train(2, 7)
        text = text + str(ind) + " ---- Pontuation: " + str(fitness_func(ind, 2)) + "\n"
        print(text)
        with open("results_2.log", "w") as archive:
            archive.write(text)
    with open("results_3.log", "r") as archive:
        text = archive.read()
    for i in range(10):
        ind = train(3, 7)
        text = text + str(ind) + " ---- Pontuation: " + str(fitness_func(ind, 3)) + "\n"
        print(text)
        with open("results_3.log", "w") as archive:
            archive.write(text)
    with open("results_4.log", "r") as archive:
        text = archive.read()
    for i in range(10):
        ind = train(4, 7)
        text = text + str(ind) + " ---- Pontuation: " + str(fitness_func(ind, 4)) + "\n"
        print(text)
        with open("results_4.log", "w") as archive:
            archive.write(text)
    
    # print(TrafficLight(15,20,1)+TrafficLight(20,60,0))