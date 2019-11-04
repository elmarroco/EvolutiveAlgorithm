import sys
import random

# Local Imports
import Population as POP
import Agent as AG
import utilities as util


# Population Size
popSize = int(sys.argv[1])

# Agent Size
agentSize = int(sys.argv[2])

# Number of generations
numGen = int(sys.argv[3])

matrix = util.randInt(0, 1, popSize, agentSize)

# Creating Population
Pop = POP.Population(popSize, matrix, agentSize)

# Solution Agent
sol = []
for i in range(agentSize):
    sol.append(bool(input(f"Enter the component [{i}] = ")))


# Evaluate Population
Pop.evaluatePopulation(sol)

print(f"Generation 0")
Pop.printPopulation()

for i in range(numGen-1):
    print(f"Generation {i+1}")
    # X-one-Point
    Pop.xOnePoint(popSize)
    # BitWise Mutation
    Pop.bitWiseMutation()
    # Evaluate Population
    Pop.evaluatePopulation(sol)
    # Sort Population
    Pop.sortPopulation()
    # Removing Weak Agents
    Pop.removeWeak(popSize)
    Pop.printPopulation()
