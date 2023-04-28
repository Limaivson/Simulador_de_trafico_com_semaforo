from src.trafficSimulator import *
import random
from numpy import mean

# Create simulation
sim = Simulation()

RUA0_HORIZONTAL_DE = ((0, 100), (100, 100))
RUA0_1_HORIZONTAL_DE = ((100, 100), (148, 100))
RUA1_HORIZONTAL_DE = ((148, 100), (248, 100))
RUA2_HORIZONTAL_DE = ((248, 100), (300, 100))
RUA3_HORIZONTAL_ED = ((102, 104), (0, 104))
RUA4_HORIZONTAL_ED = ((258, 104), (153, 104))
RUA5_HORIZONTAL_ED = ((300, 104), (258, 104))
RUA3_1_HORIZONTAL_ED = ((153, 104), (102, 104))
# RUA3_2_HORIZONTAL_ED = ((148, 104), (93, 104))

RUA6_HORIZONTAL_DE = ((0, 170), (148, 170))
RUA7_HORIZONTAL_DE = ((150, 170), (248, 170))
RUA8_HORIZONTAL_DE = ((250, 170), (300, 170))
RUA9_HORIZONTAL_ED = ((153, 174), (0, 174))
RUA10_HORIZONTAL_ED = ((258, 174), (153, 174))
RUA11_HORIZONTAL_ED = ((300, 174), (258, 174))

RUA12_HORIZONTAL_DE = ((75, 60), (148, 30))
RUA12_1_HORIZONTAL_DE = ((0, 100), (75, 60))
RUA13_HORIZONTAL_DE = ((148, 30), (248, 30))
RUA14_HORIZONTAL_DE = ((248, 30), (300, 30))

RUA15_VERTICAL_CB = ((150, 0), (150, 28))
RUA16_VERTICAL_CB = ((150, 28), (150, 98))
RUA17_VERTICAL_CB = ((150, 100), (150, 168))
RUA18_VERTICAL_CB = ((150, 168), (150, 200))
RUA19_VERTICAL_CB = ((250, 0), (250, 28))
RUA20_VERTICAL_CB = ((250, 28), (250, 98))
RUA21_VERTICAL_CB = ((250, 100), (250, 168))
RUA22_VERTICAL_CB = ((250, 168), (250, 200))
RUA23_VERTICAL_CB = ((254, 32), (254, 0))
RUA24_VERTICAL_CB = ((254, 107), (254, 32))
RUA25_VERTICAL_CB = ((254, 177), (254, 107))
RUA26_VERTICAL_CB = ((254, 200), (254, 177))

RUA27_DIAG_DE = ((50, 170), (100, 105))

via_41 = ((300, 30), (348, 30))
via_42 = ((351, 0), (351, 28))
via_43 = ((348, 30), (448, 30))
via_44 = ((351, 28), (351, 97.5))
via_45 = ((300, 100), (348, 100))
via_46 = ((348, 100), (448, 100))
via_47 = ((453, 104), (353.5, 104))
via_48 = ((354, 104), (300, 104))
via_49 = ((351, 97), (351, 167.5))
via_49_1 = ((351, 200), (351, 172.5))

via_50 = ((300, 170), (348.5, 170))
via_50_1 = ((350, 174), (300, 174))

via_52 = ((348.5, 170), (448, 170))
via_54 = ((562, 170), (452, 170))
via_55 = ((450, 172), (450, 106))
via_56 = ((560, 104), (453, 104))
via_57 = ((480, 100), (560, 100))
via_58_59 = ((450, 32), (450, 0))
via_59 = ((450, 98), (450, 32))

via_60 = ((450, 30), (480, 97))
via_60_0 = ((480, 97), (481, 100))
via_60_1 = ((562, 101.79), (562, 55))
via_60_2 = ((560.15, 55), (608, 55))
via_60_3 = ((608, 53.15), (608, 103))
via_60_4 = ((609.85, 104.2), (560, 104.2))

via_61 = ((562, 104.2), (562, 171.7))

via_100 = ((550, 100), (560, 100))

# Add multiple roads
sim.create_roads([RUA0_HORIZONTAL_DE, RUA1_HORIZONTAL_DE, RUA2_HORIZONTAL_DE, RUA3_HORIZONTAL_ED, RUA4_HORIZONTAL_ED,
                  RUA5_HORIZONTAL_ED,
                  RUA6_HORIZONTAL_DE, RUA7_HORIZONTAL_DE, RUA8_HORIZONTAL_DE, RUA9_HORIZONTAL_ED, RUA10_HORIZONTAL_ED,
                  RUA11_HORIZONTAL_ED,
                  RUA12_HORIZONTAL_DE, RUA13_HORIZONTAL_DE, RUA14_HORIZONTAL_DE, RUA15_VERTICAL_CB, RUA16_VERTICAL_CB,
                  RUA17_VERTICAL_CB, RUA18_VERTICAL_CB,
                  RUA19_VERTICAL_CB, RUA20_VERTICAL_CB, RUA21_VERTICAL_CB, RUA22_VERTICAL_CB, RUA23_VERTICAL_CB,
                  RUA24_VERTICAL_CB, RUA25_VERTICAL_CB,
                  RUA26_VERTICAL_CB, RUA27_DIAG_DE, RUA3_1_HORIZONTAL_ED, RUA0_1_HORIZONTAL_DE, RUA12_1_HORIZONTAL_DE,
                  via_41, via_42, via_43, via_44, via_45, via_46, via_47, via_48, via_49, via_49_1, via_50, via_50_1,
                  via_52,
                  via_54, via_55, via_56, via_57, via_58_59, via_59, via_60, via_60_0, via_60_1, via_60_2, via_60_3,
                  via_60_4, via_61,

                  ])

sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        [2, {"path": [30, 12, 13, 14, 31, 33, 50, 47, 51, 52, 53, 54, 55, 56, 44, 45, 49, 48]}],
        [2, {"path": [0, 29, 1, 2, 35, 36, 49, 48]}],
        [2, {"path": [26, 29, 1, 2, 35, 36, 49, 48]}],
        [2, {"path": [6, 7, 8, 41, 43, 45, 37, 38, 5, 4, 28, 3]}],
        [2, {"path": [6, 7, 8, 41, 43, 45, 37, 38, 5, 4, 16, 15]}],
        [1, {"path": [0, 29, 1, 2]}],
        [1, {"path": [27, 29, 1, 2]}],
        [1, {"path": [5, 4, 28, 3]}],
        [1, {"path": [26, 25, 24, 23]}],
        [1, {"path": [26, 25, 24, 23]}],
        [1, {"path": [6, 7, 8]}],
        [1, {"path": [6, 7, 17, 18]}],
        [1, {"path": [11, 10, 9]}],
        [1, {"path": [15, 16, 17, 18]}],
        [2, {"path": [30, 12, 13, 14, 20, 21, 22]}],
        [1, {"path": [19, 20, 21, 22]}],
        [1, {"path": [14, 31]}],
    ]
})

sim.create_signal([[0, 28], [27]], time=randint(20, 100))
sim.create_signal([[4, 29], [16]], time=randint(20, 100))
sim.create_signal([[6, 10], [17]], time=randint(20, 100))
sim.create_signal([[30], []], time=randint(20, 100))
sim.create_signal([[15], [12]], time=randint(20, 100))
sim.create_signal([[19, 24], [13]], time=randint(20, 100))
sim.create_signal([[31], [32]], time=randint(20, 100))
sim.create_signal([[35, 37], [34]], time=randint(20, 100))
sim.create_signal([[19, 24], [13]], time=randint(20, 100))
sim.create_signal([[20, 25], [1, 5]], time=randint(20, 100))
sim.create_signal([[19, 24], [13]], time=randint(20, 100))
sim.create_signal([[7, 11], [21, 26]], time=randint(20, 100))
sim.create_signal([[41], [39]], time=randint(20, 100))
sim.create_signal([[43], [44]], time=randint(20, 100))
sim.create_signal([[36, 46], [45]], time=randint(20, 100))
sim.create_signal([[49], [33]], time=randint(20, 100))
sim.create_signal([[50], []], time=randint(20, 100))

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
data = win.run(steps_per_update=5, simulation_time=5*60)

for road, d in data['road data'].items():
    if mean([x[0] for x in d]) > 0:
        print(road)
        print("Car mean amount:", mean([x[0] for x in d]))
        print("Car mean wait:", mean([x[1] for x in d]))
