import numpy as np

def solucaoExata(r, t):
    No = 4 * pow(10, 9)  # População inicial N0
    x = np.zeros(t)  # inicializa um array com tamanho de n
    y = np.zeros(t)

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

def getErrorEulerExplicito(r, h, t):
    e = eulerExplicito(r, h, t)

    error = np.abs(solucaoExata(r, t) - e)
    return error

def getErrorEulerImplicito(r, h, t):
    e = eulerImplicito(r, h, t)

    error = np.abs(solucaoExata(r, t) - e)
    return error

def getDadosExplicito():
    f = open("dadosExplicito.csv", "w")

    hs = [1, 2, 5, 10]
    logh = np.zeros(4)
    erroh = np.zeros(4)

    x = 0
    y = 0
    for i in range(0, len(hs)):
        e = getErrorEulerExplicito(0.01, hs[i], 500)
        f.writelines(str(np.log(hs[i])) + "," + str(np.log(e)) + "\n")
        logh[i] = np.log(hs[i])
        erroh[i] = np.log(e)

        x += logh[i]
        y += erroh[i]

    # mínimos quadrados
    x = x / 4.0
    y = y / 4.0
    print("x e y explicito: ", x, y)

    som = 0
    somax = 0
    for i in range(0, 4):
        som += (logh[i]*erroh[i])
        somax += pow(logh[i], 2)

    som = som - 4*(x*y)
    somax = somax - 4*pow(x, 2)
    a = som / somax
    b = y - a*x

    print("resultado a e b explicito:", a, b)

    f.close()



def getDadosImplicito():
    f = open("dadosImplicito.csv", "w")

    hs = [1, 2, 5, 10]
    logh = np.zeros(4)
    erroh = np.zeros(4)

    x = 0
    y = 0
    for i in range(0, len(hs)):
        e = getErrorEulerImplicito(0.01, hs[i], 500)
        f.writelines(str(np.log(hs[i])) + "," + str(np.log(e)) + "\n")
        logh[i] = np.log(hs[i])
        erroh[i] = np.log(e)

        x += logh[i]
        y += erroh[i]
        print(logh[i], erroh[i])

    # mínimos quadrados
    x = x / 4.0
    y = y / 4.0
    print("x e y: ", x, y)
    som = 0
    somax = 0
    for i in range(0, 4):
        som += (logh[i]*erroh[i])
        somax += pow(logh[i], 2)

    som = som - 4*(x*y)
    somax = somax - 4*pow(x, 2)
    a = som / somax
    b = y - a*x

    print("resultado a e b implicito:", a, b)


getDadosExplicito()
getDadosImplicito()