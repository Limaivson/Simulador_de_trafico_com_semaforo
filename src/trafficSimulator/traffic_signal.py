from gen_algorithm.api import TrafficManager, Street


class TrafficSignal:
    def __init__(self, roads, config={}, time=70):
        # Initialize roads
        self.roads = roads
        self.time = time
        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

        if len(self.roads[1]) > 0:
            streets = [Street(max(street.length for street in streets), 8) for streets in self.roads]
            self.manager: TrafficManager = TrafficManager(streets, self.current_cycle_index)
        else:
            self.manager = None

        self.next_instruction_time = -float('inf')

    def set_default_config(self):
        self.cycle = [(False, True), (True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim, t=None, dt=None):
        """
        self.next_instruction_time = t + open_time
        self.open = {r: False for road in self.roads for r in road}
        if road_index[1] < 0:
            self.open = {r: False for road in self.roads for r in road}
            return
        for road in self.find_group(self.roads[road_index[0]][road_index[1]]):
            self.open[road] = True"""

        if self.manager is None:
            cycle_length = self.time
            k = (sim.t // cycle_length) % 2
            self.current_cycle_index = int(k)
            return

        if t is None or dt is None:
            raise ValueError("t and dt must be informed if TrafficManager is being used")

        if t - dt < self.next_instruction_time:
            return

        street_index, green_time = self.update_algorithm(sim)
        self.current_cycle_index = (street_index + 1) % 2
        self.next_instruction_time = t + green_time

    def update_algorithm(self, sim):
        car_wait_times = [sum(c.wait_time for r in road for c in r.vehicles) for road in self.roads]
        car_amounts = [sum(len(r.vehicles) for r in road) for road in self.roads]
        for i in range(len(car_amounts)):
            self.manager.street_wait_time_actualization(car_wait_times[i], i)
            self.manager.street_car_count_actualization(car_amounts[i], i)

        street_index, green_time, *_, = self.manager.select_opened_way(sim.t)

        return street_index, green_time
