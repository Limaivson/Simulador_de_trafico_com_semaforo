class TrafficSignal:

    ID = 0

    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()
        self.id = TrafficSignal.ID
        TrafficSignal.ID += 1

        self.open = {r[0]: False for r in self.roads}

        self.next_instruction_time = -float('inf')

    def set_default_config(self):
        self.cycle = [(False, True), (True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 10

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    def current_cycle(self, road):
        return self.open[road]

    def update(self, t, dt):
        if t - dt < self.next_instruction_time:
            return

        car_wait_times = [[c.wait_time for c in road[0].vehicles] for road in self.roads]
        car_amounts = [len(road[0].vehicles) for road in self.roads]
        open_time, road_index = self.genetic(car_wait_times, car_amounts, t)
        self.next_instruction_time = t + open_time
        self.open = {r[0]: False for r in self.roads}
        self.open[self.roads[road_index][0]] = True

    @staticmethod
    def genetic(wait_times, amounts, t):
        max_amount = max(amounts)
        max_amount_index = amounts.index(max_amount)
        min_time = 10
        weight = 1
        min_time += max_amount * weight
        print(f"Wait = {min_time}, at t = {t}")
        return min_time, max_amount_index
