import Agent as AG


class Population:
    def __init__(self, popSize, matrix, agentSize):
        self.x = []
        for i in range(popSize):
            self.x.append(AG.Agent(matrix[i], agentSize))

    def evaluatePopulation(self, sol):
        for i in range(len(self.x)):
            self.x[i].evaluate(sol)

    def addAgent(self, agent):
        self.x.append(agent)

    def printPopulation(self):
        for i in range(len(self.x)):
            self.x[i].printAgent()

    def xOnePoint(self, popSize):
        for i in range(int(popSize/2)):
            newAgent1, newAgent2 = self.x[i].xOnePoint(self.x[i+(int(popSize/2))])
            self.addAgent(newAgent1)
            self.addAgent(newAgent2)

    def bitWiseMutation(self):
        for i in range(len(self.x)):
            self.x[i].bitWise()

    def sortPopulation(self):
        self.x.sort(key=lambda z: z.fitness)

    def removeWeak(self, popSize):
        self.x = self.x[:popSize]
        