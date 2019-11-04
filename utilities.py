import numpy as np
import time


def randInt(low, high, popSize, agentSize):
    np.random.seed(int(time.time()))
    return np.random.randint(2, size=(popSize, agentSize))

def flown():
    np.random.seed(int(time.time()))
    return np.random.uniform()

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
