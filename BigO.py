#Hecho por Antonio Valdés Hernández
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = np.ones_like(x)  
y1 = np.log(x)        
y2 = x                
y3 = x * np.log(x)    
y4 = x**2             
y5 = 2**x             

plt.plot(x,y,label='O(1)') #Constante
plt.plot(x,y1,label='O(log n)') #Logaritimica
plt.plot(x,y2, label='O(n)') #Lineal
plt.plot(x,y3, label='O(n log n)') #Lienal Logaritmica
plt.plot(x,y4, label='O(n^2)') #Cuadratica
plt.plot(x,y5, label='O(2^n)') #Exponencial
plt.xlabel('Elementos')
plt.ylabel('Operaciones')
plt.title('Notación Big O')
plt.legend()
plt.grid(True)
plt.show()
