import cmath
from math import pi, sin 
import matplotlib.pyplot as plt

#Zmienne inicjalizacyjne
a = 6; b = 7; c = 3

def fun(x):
    return amplitude * sin(2*pi*f*x+fi)

#Zmienne stałe
amplitude = 1.
fi = c * pi # rad
f = b #Hz
fs = 10000 #Częstliwość próbkowania
q=16

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

def showFunction(functionName, X, Y, saveGraphToFile=False, title=None):
#Funkcja wyświetlająca i zapisująca wyniki do pliku
    plt.plot(X,Y,'r.',markersize=1)
    plt.title(title)
    plt.xlabel('t[s]')
    plt.ylabel(functionName+'(t)')
    if saveGraphToFile:
        plt.savefig(str('../results/'+functionName+'.png'))
    plt.show()

def DFT(X,Y):
    Xk=[]
    N=len(X)
    for n, k in enumerate(X):
        p = (2*cmath.pi)/N
        wN = cmath.cos(p)+1j*cmath.sin(p)
        Xk.append( Y[n]*pow(wN,-k*n) )
    return Xk

X, Y = sampling(0,1/fs,a,fun)
showFunction("s", X, Y, False, title="Sygnał tonu prostego")
Y = DFT(X,Y)
showFunction("s", X, Y, False, title="Sygnał tonu prostego")




