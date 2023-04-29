from traffic_light import TrafficLight

class Car():
    def __init__(self, dist: float) -> None:
        self.stopped = False
        self.dist = dist
        self.max_vel = 30/3.6 # km/h -> m/s
        self.acceleration = 6/3.6 # km/h² -> m/s²
        self.vel = 0
        self.time_stopped = 0

    def stop(self):
        self.stopped = True
        self.vel = 0

    def go(self):
        self.stopped = False

    def iterate(self, iter_time: float):
        if not self.stopped:
            self.dist -= self.vel * iter_time
            if self.vel < self.max_vel:
                self.vel += self.acceleration * iter_time
            if self.vel > self.max_vel:
                self.vel = self.max_vel
        else:
            self.time_stopped += iter_time


class Street():
    def __init__(self, iter_time: float, street_comp: float, red_light: bool, max_vel: float = 30/3.6) -> None:
        self.cars = []
        self.iter_time = iter_time
        self.street_comp = street_comp
        self.red_light = red_light
        self.max_vel = max_vel
        self.waves = []
        self.waves_ref = []
    
    def summon_car(self) -> None:
        self.cars.append(Car(self.street_comp))

    def turn(self) -> None:
        self.red_light = not self.red_light
        if not self.red_light:
            for car in self.cars:
                car.go()

    def iterate(self, iter_time: float) -> None:
        last_car_dist = 0
        empty_waves = []
        for wave in self.waves:
            wave[1] -= self.max_vel
            if wave[1] <= self.street_comp:
                self.summon_car()
                wave[1] += 5
                wave[0] -= 1
            if wave[0] <= 0:
                empty_waves.append(wave)
        for wave in empty_waves:
            self.waves.remove(wave)
        empty_waves = []
        for wave in self.waves_ref:
            wave[1] -= self.max_vel
            if wave[1] <= 0:
                empty_waves.append(wave)
        for wave in empty_waves:
            self.waves_ref.remove(wave)
        exit = []
        for car in self.cars:
            car.iterate(iter_time)
            if self.red_light:
                if car.dist <= 10:
                    car.stop()
                    car.dist = 10
                if car.dist <= last_car_dist + 5:
                    car.stop()
                    car.dist = last_car_dist + 5
                last_car_dist = car.dist
            elif car.dist <= 0:
                exit.append(car)
        stopped_time = 0
        for car in exit:
            stopped_time += car.time_stopped
            self.cars.remove(car)
        return {
            "stopped time" : stopped_time,
            "car count"    : len(exit)
        }

    def car_count(self) -> int:
        stopped_cars = 0
        for car in self.cars:
            if car.stopped:
                stopped_cars += 1
        return stopped_cars
    
    def wave(self, car_qtd: int, dist: float, factor: float = 0.5) -> None:
        if car_qtd > 0:
            dist += self.street_comp + 10 # distance from closest street entrance
            self.waves.append([car_qtd * factor, dist])
            self.waves_ref.append([car_qtd * factor, dist])
    
    def stopped_time_sum(self) -> float:
        time = 0
        for car in self.cars:
            if car.stopped:
                time += car.time_stopped
        return time
    
    def transit_impact(self) -> float:
        impact = self.stopped_time_sum()
        for wave in self.waves_ref:
            impact += wave[0] * 10 * 100 / (100 + wave[1])
        return impact
    
    def __str__(self):
        if self.red_light:
            return "---RED--- Cars: " + str(len(self.cars)) + " - Stopped: " + str(self.car_count())
        else:
            return "--GREEN-- Cars: " + str(len(self.cars)) + " - Stopped: " + str(self.car_count())