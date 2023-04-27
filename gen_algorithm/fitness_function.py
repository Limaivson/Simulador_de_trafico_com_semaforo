from ranker_standart_functions import *
from traffic_light import TrafficLight
from traffic_sim import Street
from math import ceil
from random import randint

def ff(light_control: TrafficLight, ways: int):
    time_min  = light_control.get_time_min()
    time_max  = light_control.get_time_max()
    coef      = light_control.get_coef()
    iter_time = 1 # seccond
    sim_time  = 3600 # secconds
    summon_time = 2 # secconds
    summon_iter = ceil(summon_time / iter_time) # summons a car for each summon_iter count
    iter_count = ceil(sim_time / iter_time)
    streets   = []
    green = randint(1, ways)
    for street in range(ways):
        length = randint(200, 500)
        # print(f"Street {street}: {length}m")
        if street == green:
            streets.append(Street(iter_time, length, False))
        else:
            streets.append(Street(iter_time, length, True))
    # input()

    green_time_iterations = ceil(time_min/iter_time)
    total_wait_time = 0
    total_car_count = 0

    for iteration in range(iter_count):
        if green_time_iterations == 0:
            car_count = opengin_light_selector(streets)
            green_time_iterations = ceil(green_time(time_min, time_max, coef, car_count) / iter_time)
        for street in streets:
            exited_cars = street.iterate(iter_time)
            total_wait_time += exited_cars["stopped time"]
            total_car_count += exited_cars["car count"]
            # print(str(street) + "\t", end="")
        # print()
        if iteration % summon_iter == 0:
            streets[randint(0,len(streets)-1)].summon_car()
        green_time_iterations -= 1

    for street in streets:
        if not street.red_light:
            street.red_light = True
        total_car_count += street.car_count()
        total_wait_time += street.stopped_time_sum()
    # print(total_wait_time)
    # print(total_car_count)

    return 100 * total_wait_time / (total_car_count * sim_time)

if __name__ == "__main__":
    print(ff(TrafficLight(50, 10, 0.01), 3))