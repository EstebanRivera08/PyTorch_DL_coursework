import matplotlib.pyplot as plt
import numpy as np

# Solicitamos el número de entrada para seguir el algorithmo de collatz
Number_inicial = float(input('Ingresa tu número: '))

# Inicializamos el candidato para empezar el bucle
Number_final = Number_inicial

# Inicializamos la cantidad de pasos elaborados y la lista
Pasos = 0
Lista = [Number_final]

# Mientras el número que tengamos sea diferente de 1 sigue en el bucle del algorithmo

while Number_final != 1 :

    # Verificamos si es par
    if Number_final % 2 == 0 :

        #Si es par se divide en 2
        Number_final = Number_final/2

    # Si no es par (es impar)
    else :

        #Si es impar entonces multiplicamos por 3 y le sumamos 1
        Number_final = Number_final*3 + 1

    # Llevamos el contador de los bucles (pasos) realizados
    Pasos = Pasos + 1

    # Concatenamos los resultados para generar una lista con cada resultado
    Lista += [Number_final]

#Imprimimos los resultados
print('La cantidad de pasos fueron: ' + str(Pasos))
print('Y los resultados en cada uno son: ')
print(Lista)

# Generamos los vectores para graficar
x = np.linspace(0,Pasos,Pasos+1)
y = np.array(Lista)

# Creamos la gráfica de los resultados vs No. de pasos
plt.plot(x,y,'k',x,y,'or')
plt.grid('minor')
plt.ylim((0,np.max(y)+np.max(y)/10))
plt.xlabel('No. Paso')
plt.ylabel('Resultado en el paso')
plt.show()
