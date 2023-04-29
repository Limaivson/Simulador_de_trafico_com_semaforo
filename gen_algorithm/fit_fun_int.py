from ranker_standart_functions import *
from model_traffic_light import TrafficLight
from traffic_sim import Street
from math import ceil
from random import randint

def fitness_func(light_control: TrafficLight, ways: int, with_print: bool = False):
    time_min  = light_control.get_time_min()
    time_max  = light_control.get_time_max()
    coef      = light_control.get_coef()
    iter_time = 3 # seccond
    sim_time  = 3600 # secconds
    summon_time = 2 # secconds
    summon_iter = ceil(summon_time / iter_time) # summons a car for each summon_iter count
    iter_count = ceil(sim_time / iter_time)
    streets   = []
    green = randint(1, ways)
    for street in range(ways):
        length = randint(50, 150)
        if with_print: print(f"Street {street}: {length}m")
        if street == green:
            streets.append(Street(iter_time, length, False))
        else:
            streets.append(Street(iter_time, length, True))
    if with_print: input()

    green_time_iterations = ceil(time_min/iter_time)
    total_wait_time = 0
    total_car_count = 0
    changes = 0

    for iteration in range(iter_count):
        if green_time_iterations == 0:
            selection = opening_light_selector(streets)
            car_count, waves = selection[0], selection[1]
            t_green = green_time(time_min, time_max, coef, car_count, waves)
            if with_print: print(t_green)
            green_time_iterations = ceil(t_green / iter_time)
            changes += 1
        if randint(1, 1000) < 15:
            cars_num = randint(1, 30)
            light_distance = randint(0, 300)
            factor = randint(30, 100)/100
            street_selected = randint(0,len(streets)-1)
            streets[street_selected].wave(cars_num,
                                          light_distance,
                                          factor)
            if with_print: print(f"A wave with {cars_num} cars is comming at {light_distance}m from street {street_selected} with a chance of {100*factor}% to each car reache the traffic light.")
        for street in streets:
            exited_cars = street.iterate(iter_time)
            total_wait_time += exited_cars["stopped time"]
            total_car_count += exited_cars["car count"]
            if with_print: print(str(street) + "\t", end="")
        if with_print: print()
        if iteration % summon_iter == 0:
            streets[randint(0,len(streets)-1)].summon_car()
        green_time_iterations -= 1

    for street in streets:
        if not street.red_light:
            street.red_light = True
        total_car_count += street.car_count()
        total_wait_time += street.stopped_time_sum()
    if with_print: print(total_wait_time)
    if with_print: print(total_car_count)
    if with_print: print(changes)
    if with_print: print(100 * total_wait_time / (total_car_count * sim_time))
    return 100 * (total_wait_time + 200*changes) / (total_car_count * sim_time)

if __name__ == "__main__":
    print(fitness_func(TrafficLight(22.18105513493764, 53.77203347341702, 0.3444758415378191), 4, True))