from math import pi, sin
import matplotlib.pyplot as plt
#Zmienne inicjalizacyjne
a = 6; b = 7; c = 3
#Zmienne stałe
amplitude = 1.
omega = c * pi # rad
f = b #Hz
fs = 10000 #Częstliwość próbkowania
q=16

def fun(x):
    return amplitude * sin(2*pi*f*x+omega)


def sampling(begin, step, end, function):
#Funckja próbkująca sygnał
    X  =[]
    Y = []
    tn = begin
    n=0
    while tn <= end:
        tn = begin + (step * n)
        n+=1
        X.append(tn)
        Y.append(function(tn))
    return X, Y

def quantization(X, Y, q):
#Funkcja kwantyzująca
    pow2 = pow(2,q)
    qY=[]
    for i, x in enumerate(X):
        qY.append( round( ((Y[i]+1)/(amplitude*2))*pow2,0 ) )
    return X, qY


def showFunction(functionName, X, Y, saveGraphToFile=False, title=None):
#Funkcja wyświetlająca i zapisująca wyniki do pliku
    plt.plot(X,Y,'r.',markersize=1)
    plt.title(title)
    plt.xlabel('t[s]')
    plt.ylabel(functionName+'(t)')
    if saveGraphToFile:
        plt.savefig(str('../results/'+functionName+'.png'))
    plt.show()


#Main

X, Y = sampling(0,1/fs,a,fun)
showFunction("s", X, Y, True, title="Sygnał tonu prostego")
X, Y = quantization(X,Y,q)
showFunction("q", X, Y, True, title="Skwantyzowana funkcja Zad2")
X, Y = sampling(0,1/(fs/2),a,fun)
X, Y = quantization(X,Y,q/2)
showFunction("q2", X, Y, True, title="Skwantyzowana funkcja Zad3")

