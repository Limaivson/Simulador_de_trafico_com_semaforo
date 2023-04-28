from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((0, 100), (148, 100)),
    ((148, 100), (300, 100)),
    
    ((150, 0), (150, 98)),
    ((150, 98), (150, 200)),
])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, 1]}],
        [1, {"path": [0, 3]}],
        [1, {"path": [2, 3]}],
        [1, {"path": [2, 3]}]
    ]
})

sim.create_signal([[0], [2]])

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
data = win.run(steps_per_update=5)
print(data)
print(100 * (data['wait time'] / data['cars generated'] / data['simulation time']))
for road, d in data['road data'].items():
    print(road)
    print("Car mean amount:", mean([x[0] for x in d]))
    print("Car mean wait:", mean([x[1] for x in d]))
