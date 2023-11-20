import requests


def promedio(x):
    total = 0
    for i in range(len(x)):
        total = total + x[i]

    for i in range(len(x)):
        y = (x[i] * 100) / total
        print("El valor ", i+1, "representa el ", y, "%")





        
