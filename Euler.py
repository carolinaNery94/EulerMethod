import numpy as np

def solucaoExata(r, t=100):
    No = 4 * pow(10, 9)  # População inicial N0
    x = np.zeros(100)  # inicializa um array com tamanho de n
    y = np.zeros(100)

    # f = open("exata.csv", "w")
    for i in range(0, t):  # percorre o for de 0 até 101
        exact = No * pow((np.e), r * i)
        y[i] = exact  # salvando no vetor x
        x[i] = i
        # f.writelines(str(x[i]) + "," + str(y[i]) + "\n")
    return y[i-1]
    # f.close()


def eulerImplicito(r, h, t=100):
    z = np.zeros(t)
    No = 4 * pow(10, 9)  # População inicial N0
    tempo = 0
    i = 0

    # f = open("imp-" + str(h) + ".csv", "w")
    while tempo < t:
        ns = (No / float(1 - r * h))
        z[i] = ns
        No = ns
        # f.writelines(str(tempo) + "," + str(ns) + "\n")
        i += 1
        tempo += h
    return z[i-1]

    # f.close()


def eulerExplicito(r, h, t=100):
    z = np.zeros(t)
    No = 4 * pow(10, 9)  # População inicial N0
    tempo = 0
    i = 0

    # f = open("exp-" + str(h) + ".csv", "w")
    while tempo < t:
        ns = No * float(1 + (r * h))
        z[i] = ns
        No = ns
        # f.writelines(str(tempo) + "," + str(ns) + "\n")
        i += 1
        tempo += h
    return z[i-1]

    # f.close()

def getErrorEulerExplicito(r, h, t=50):
    e = eulerExplicito(r, h, 50)

    error = np.abs(e - solucaoExata(r, t))
    print(error)
    return error

def getErrorEulerImplicito(r, h, t=100):
    e = eulerImplicito(r, h, t)

    error = np.abs(e - solucaoExata(r, t))
    return error

def getDadosExplicito():
    f = open("dadosExplicito.csv", "w")

    hs = [1, 2, 5, 10]
    logh = np.zeros(4)
    erroh = np.zeros(4)

    for i in range(0, len(hs)):
        e = getErrorEulerExplicito(0.01, hs[i], 50)
        f.writelines(str(np.log(hs[i])) + "," + str(np.log(e)) + "\n")
        logh[i] = np.log(hs[i])
        erroh[i] = np.log(e)
    f.close()
    A = np.vstack([logh, np.ones(len(logh))]).T
    m, c = np.linalg.lstsq(A, erroh)[0]
    print(m, c)


def getDadosImplicito():
    f = open("dadosImplicito.csv", "w")

    hs = [1, 2, 5, 10]
    logh = np.zeros(4)
    erroh = np.zeros(4)

    for i in range(0, len(hs)):
        e = getErrorEulerImplicito(0.01, hs[i], 50)
        f.writelines(str(np.log(hs[i])) + "," + str(np.log(e)) + "\n")
        logh[i] = np.log(hs[i])
        erroh[i] = np.log(e)
    f.close()
    A = np.vstack([logh, np.ones(len(logh))]).T
#   T faza transposta
    m, c = np.linalg.lstsq(A, erroh)[0]
    print(m, c)


getDadosExplicito()
getDadosImplicito()