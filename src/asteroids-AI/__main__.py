from env.Game import Game
import numpy as np
from algo.NeuralNetwork import NeuralNet
from algo.Population import *


pop = Population(10)
i = 2
while True:
    print(f"\n \nGeneration: {i}")
    pop.play()
    pop.find_best_agent()

    pop.natural_selection()
    pop.generate()
    pop.best_fitness = 0
    i += 1

