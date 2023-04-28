from src.trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    # Via 40
    ((300, 30), (350, 30)),
    # Via 41
    ((350, 30), (450, 30)),

    # Via 90
    ((450, 30), (500, 100)),

    # Via 100
    ((550, 100), (560, 100)),
    # Via 101
    ((560, 101.79), (560, 55)),
    # Via 102
    ((558, 55), (608, 55)),
    # Via 103
    ((608, 53), (608, 106)),
    # Via 104
    ((608, 104.2), (562, 104.2)),
    # Via 105
    ((562, 104.2), (562, 170)),
    # Via 106
    ((562, 170), (450, 170)),

    # Via 50, indo para a direita
    ((300, 100), (348, 100)),
    # Via 51 indo para a direita
    ((348, 100), (450, 100)),
    # Via 52 indo para a direita
    ((450, 100), (550, 100)),
    # Via 50, indo para a esquerda
    ((350, 104), (300, 104)),
    # Via 51 indo para a esquerda
    ((450, 104), (350, 104)),
    # Via 52 indo para a esquerda
    ((450, 104), (560, 104)),

    # Via 60
    ((300, 170), (350, 170)),
    # Via 61
    ((350, 170), (450, 170)),

    # Via 70 indo para baixo
    ((351, 0), (351, 99)),
    # Via 71 indo para baixo
    ((351, 99), (351, 198)),

    # Via 80
    ((450, 0), (450, 99)),
    # Via 81
    ((450, 99), (450, 198)),

    # 4 Via para a esquerda
    ((50, 0), (50, 98)),

    ((370, 100), (430, 29)),
])

# config = {
#     "cycle": [(False, True), (True, False)],
#     "slow_distance": 40,
#     "slow_factor": 10,
#     "stop_distance": 15,
#     "semaphore_1_time": 2, # tempo de mudança de estado para o semáforo 1
#     "semaphore_2_time": 1 # tempo de mudança de estado para o semáforo 2
# }

decisions = []
sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [4, 1]}],
        [1, {"path": [0, 3]}],
        [1, {"path": [2, 3]}],
        [1, {"path": [2, 3]}],

    ]
})

sim.create_signal([[0], [2]])

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)
