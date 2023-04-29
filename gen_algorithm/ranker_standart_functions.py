def green_time(time_min: float, time_max: float, coef: float, cars_count: int, waves_impact: float) -> float:
    try:
        cars_count *= 0.5
        cars_count += waves_impact
        time_delta = time_max - time_min
        time = time_min + time_delta * (coef**(1/cars_count))
        # print(time)
        return time
    except:
        # print(time_min)
        return time_min

def opening_light_selector(street_list: list) -> tuple:
    bigger_impact = 0
    worst_street = street_list[0] if street_list[0].red_light else street_list[1]
    for street in street_list:
        if not street.red_light:
            street.turn()
        elif street.transit_impact() > bigger_impact:
            bigger_impact = street.stopped_time_sum()
            worst_street = street
    car_count = worst_street.car_count()
    waves = worst_street.waves_ref
    worst_street.turn()
    return (car_count, waves)