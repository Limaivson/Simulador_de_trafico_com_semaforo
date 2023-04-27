class TrafficLight:
    def __init__(self, t_max: float, t_min: float, coef: float) -> None:
        self.t_max = t_max
        self.t_min = t_min
        self.coef = coef

    def get_time_min(self) -> float:
        return self.t_min

    def get_time_max(self) -> float:
        return self.t_max

    def get_coef(self) -> float:
        return self.coef

    