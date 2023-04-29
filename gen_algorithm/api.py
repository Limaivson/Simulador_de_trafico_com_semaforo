from model_traffic_light import TrafficLight
from ranker_standart_functions import *

class TrafficManager(TrafficLight):
    def __init__(self, streets: list, green_light_street_index: int):
        if len(streets) == 2:
            self.time_min = 24.14554469930662
            self.time_max = 52.40986013052539
            self.coef = 0.26209022477400057
        elif len(streets) == 3:
            self.time_min = 17.826259409273877
            self.time_max = 39.300010200854835
            self.coef = 0.02668265548981178
        elif len(streets) == 4:
            self.time_min = 15.733329155406558
            self.time_max = 37.02171034938587
            self.coef = 0.001
        super().__init__(self.time_min, self.time_max, self.coef)
        self.streets = streets
        self.green_light_street_index = green_light_street_index

    def street_wait_time_actualization(self, wait_time: float, street_index: int) -> None:
        self.streets[street_index].wait_time_actualization(wait_time)

    def street_car_count_actualization(self, count: int, street_index: int) -> None:
        self.streets[street_index].car_count_actualization(count)

    def car_wave(self, wave_count: int, street_index: int, time_simulation: float) -> None:
        self.streets[street_index].car_wave(wave_count, time_simulation)

    def select_opened_way(self, time_simulation: float) -> int:
        """Returns [street_index, green_time, wave_count], needs to call next traffic lights car_wave method for this wave."""
        worst_impact = 0
        for street_index in range(len(self.streets)):
            if street_index != self.green_light_street_index:
                # street impact method
                impact = self.streets[street_index].get_wait_time()
                for wave in self.streets[street_index].get_waves():
                    impact += wave.get_count() * 10 * 100 / (100 + wave.get_dist(time_simulation))
                if impact > worst_impact:
                    worst_street_index = street_index
                    worst_impact = impact
        waves_impact = 0
        for wave in self.streets[worst_street_index].get_waves():
            waves_impact += wave.get_count()
        time_green = green_time(self.time_min, 
                                self.time_max, 
                                self.coef, self.streets[worst_street_index].get_car_count(),
                                waves_impact)
        return (worst_street_index, time_green, self.coef, self.streets[worst_street_index].get_car_count())




class Street:
    def __init__(self, street_comp: float, avg_vel: float) -> None:
        self.__street_comp = street_comp
        self.__waves = []
        self.__car_count = 0
        self.__wait_time = 0
        self.__avg_vel = avg_vel

    def wait_time_actualization(self, wait_time: float) -> None:
        self.__wait_time = wait_time

    def street_car_count_actualization(self, count: int) -> None:
        self.__car_count = count

    def car_wave(self, wave_count, time_simulation) -> None:
        self.__waves.append(Wave(wave_count, self.__street_comp, self.__avg_vel, time_simulation))

    def get_car_count(self) -> int:
        return self.__car_count
    
    def get_waves(self) -> list:
        return self.__waves




class Wave:
    def __init__(self, count: int, street_comp: float, avg_vel: float, time_simulation: float) -> None:
        self.count = count
        self.street_comp = street_comp
        self.avg_vel = avg_vel
        self.time_simulation = time_simulation

    def get_count(self) -> int:
        return self.count
    
    def get_dist(self, time_simulation: float) -> float:
        return self.street_comp - self.avg_vel * (self.time_simulation - time_simulation)