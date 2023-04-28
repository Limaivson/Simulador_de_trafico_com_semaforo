import random

class TrafficLight:
    time_min_range = [15,35]
    time_max_range = [35,100]
    coef_range = [0.0000001,0.9999999]

    def __init__(self,time_min:float, time_max:float, coef:float):
        self.__time_min = self.time_min_range[0] + (self.time_min_range[1] - self.time_min_range[0])*time_min/100
        self.__time_max = self.time_max_range[0] + (self.time_max_range[1] - self.time_max_range[0])*time_max/100
        self.__coef = self.coef_range[0] + (self.coef_range[1] - self.coef_range[0])*coef/100
    
    def __repr__(self) -> str:
        return f'TrafficLight(time_min: {self.__time_min}, time_max: {self.__time_max}, coef: {self.__coef})'
    
    def __str__(self) -> str:
        return f'TrafficLight(time_min: {self.__time_min}, time_max: {self.__time_max}, coef: {self.__coef})'

    def get_time_min(self) -> float:
        return self.__time_min
    def get_time_max(self) -> float:
        return self.__time_max
    def get_coef(self) -> float:
        return self.__coef
    
    def set_time_min(self, new_time_min:float):
        self.__time_min = new_time_min
    def set_time_max(self, new_time_max:float):
        self.__time_max = new_time_max
    def set_coef(self, new_coef:float):
        self.__coef = new_coef

    def get_configuration(self) -> list:
        t_max = round(self.__time_max, 10)
        t_min = round(self.__time_min, 10)
        coef = round(self.__coef, 10)
        return [t_max, t_min, coef]

    def __add__(self,other):
        sorting = True
        while sorting:
            x = random.random()
            time_min = self.get_time_min() * x + other.get_time_min() * (1-x)
            x = random.random()
            time_max = self.get_time_max() * x + other.get_time_max() * (1-x)
            x = random.random()
            coef = self.get_coef() * x + other.get_coef() * (1-x)
            sorting = False
            
            if time_min >= time_max:
                sorting = True
            elif (time_min < self.time_min_range[0] or time_min > self.time_min_range[1]):
                sorting = True
            elif (time_max < self.time_max_range[0] or time_max > self.time_max_range[1]):
                sorting = True
            elif (coef < self.coef_range[0] or coef > self.coef_range[1]):
                sorting = True
        return TrafficLight(time_min,time_max,coef)