from email.policy import strict
import random

A=[1,2,3,4,5]
i=0

for i in range(5):
    A[i]=random.randint(0,9)
    print (A[i]);
varInput= int (input("Ingrese un valor: "))
print(varInput)

for i in range (5):
    if A[i] > varInput:
        print("El valor del arreglo es mayor")
    else:
        print("El valor del arreglo es menor")

    