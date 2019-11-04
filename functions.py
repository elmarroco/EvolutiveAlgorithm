from numpy import linalg as LA

def function1(agent1, agent2):
    aux = [0] * len(agent1)
    for i in range(len(agent1)):
        aux[i] = agent1[i] ^ agent2[i]
    return LA.norm(aux)
