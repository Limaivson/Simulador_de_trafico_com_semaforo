from traffic_light import TrafficLight

class Car():
    def __init__(self, dist: float) -> None:
        self.stopped = False
        self.dist = dist
        self.max_vel = 40/3.6 # km/h -> m/s
        self.acceleration = 8/3.6 # km/h² -> m/s²
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
    def __init__(self, iter_time: float, street_comp: float, red_light: bool) -> None:
        self.cars = []
        self.iter_time = iter_time
        self.street_comp = street_comp
        self.red_light = red_light
    
    def summon_car(self) -> None:
        self.cars.append(Car(self.street_comp))

    def turn(self) -> None:
        self.red_light = not self.red_light
        if not self.red_light:
            for car in self.cars:
                car.go()

    def iterate(self, iter_time: float) -> None:
        last_car_dist = 0
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
    
    def stopped_time_sum(self) -> float:
        time = 0
        for car in self.cars:
            if car.stopped:
                time += car.time_stopped
        return time
    
    def __str__(self):
        if self.red_light:
            return "---RED--- Cars: " + str(len(self.cars)) + " - Stopped: " + str(self.car_count())
        else:
            return "--GREEN-- Cars: " + str(len(self.cars)) + " - Stopped: " + str(self.car_count())