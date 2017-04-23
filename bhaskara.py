import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

x1 = (- b + math.sqrt(delta))/(2*a)
x2 = (- b - math.sqrt(delta))/(2*a) 

print("A primeira raiz é ", x1)
print("A segunda raiz é ", x2)

 
