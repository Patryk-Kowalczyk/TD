import math
import matplotlib.pyplot as plt

#Zmienne stałe
a=6; b=7; c=3


#Funckja obliczająca mijsca zerowe funkcji kwadratowe
def check():
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(x1,' ',x2)
    elif delta==0:
        x = -b / (2*a)
        print(x)
    else:
        print('Brak rozwiazan')

#Definicja poszczegolnych funkcji
def x(t):
    return a * (t * t) + b * t + c
def y(t):
    return 2 * x(t) * x(t) + 12 + math.cos(t)
def z(t):
    return math.sin(2*math.pi*7*t) * x(t) - 0.2 * math.log10(abs(y(t))+math.pi)
def u(t):
    return math.sqrt(abs(y(t)*y(t)*z(t)))- 1.8 * math.sin(0.4 * t * z(t)*x(t))
def v(t):
    if t>=0 and t<.22:
        return (1 - 7*t) * math.sin((2*math.pi*t*10)/(t+.04))
    elif t >= .22 and t<.7:
        return .63 * t * math.sin(125*t)
    elif t>=.7 and t <=1:
        return math.pow(t,-.662) + .77 * math.sin(8*t)
    else:
        return None
def p1(t):
    sum = 0;
    for n in range(1,3):
        sum += (( math.cos(12*t*(n*n)) + math.cos(16*t*n) )/ ( n*n ))
    return sum
def p2(t):
    sum = 0;
    for n in range(1,5):
        sum += (( math.cos(12*t*(n*n)) + math.cos(16*t*n) )/ ( n*n ))
    return sum
def p3(t):
    sum = 0;
    for n in range(1,67):
        sum += (( math.cos(12*t*(n*n)) + math.cos(16*t*n) )/ ( n*n ))
    return sum


def showFunction(functionName, begin, step, end, function, saveGraphToFile=False):
#Funkcja wyświetlająca i zapisująca wyniki do pliku
    tn = begin
    n = 0
    X=[]
    FX=[]
    while tn <= end:
        tn = begin + (step * n)
        n+=1
        X.append(tn)
        FX.append(function(tn))
    plt.plot(X,FX,'r.')
    plt.xlabel('t[s]')
    plt.ylabel(functionName+'(t)')
    if saveGraphToFile:
        plt.savefig(str('../results/'+functionName+'.png'))
    plt.show()
    

check()
step = 1/22050
showFunction("x",-10,1/100,10,x,True)
showFunction("y",0,step,1,y,True)
showFunction("z",0,step,1,z,True)
showFunction("u",0,step,1,u,True)
showFunction("v",0,step,1,v,True)
showFunction("p2",0,step,1,p1,True)
showFunction("p4",0,step,1,p2,True)
showFunction("p67",0,step,1,p3,True)



