import utilities as util
import functions as fun


class Agent:
    def __init__(self, array, size):
        self.x = array
        self.fitness = 0

    def evaluate(self, agent):
        self.fitness = fun.function1(self.x, agent)

    def printAgent(self):
        for i in range(len(self.x)):
            print(f"x[{i}] = {self.x[i]}")
        print(f"Fitness = {self.fitness}")

    def xOnePoint(self, agent):
        A, B = util.split_list(self.x)
        C, D = util.split_list(agent.x)
        return Agent([*A, *C], len(self.x)), Agent([*B,*D], len(self.x))

    def bitWise(self):
        prob = 1/len(self.x)
        for i in range(len(self.x)):
            if(util.flown() <= prob):
                if(self.x[i]):
                    self.x[i] = 0
                else:
                    self.x[i] = 1
