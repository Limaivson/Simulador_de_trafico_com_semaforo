from traffic_sim import Street

def green_time(time_min: float, time_max: float, coef: float, cars_count: int) -> float:
    try:
        cars_count *= 0.5
        time_delta = time_max - time_min
        time = time_min + time_delta * (coef**(1/cars_count))
        print(time)
        return time
    except:
        print(time_min)
        return time_min

def opengin_light_selector(street_list: list) -> Street:
    bigger_stopped_time = 0
    worst_street = street_list[0] if street_list[0].red_light else street_list[1]
    for street in street_list:
        if not street.red_light:
            street.turn()
        elif street.stopped_time_sum() > bigger_stopped_time:
            bigger_stopped_time = street.stopped_time_sum()
            worst_street = street
    car_count = worst_street.car_count()
    worst_street.turn()
    return car_count