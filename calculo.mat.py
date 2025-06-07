#%%
import math 
A = int(input("Digite o número de A"))
B = int(input("Digite o número de B"))
C = int(input("Digite o número de C"))

Delta = float((B**2) -4 * A * C)

print(f"Delta dos números e: {Delta}")

if Delta <= 0:
    print("Como delta é igual ou menor a zero, X1 e X2 são iguais.")
else:
    x1 = (-B + math.sqrt(Delta)) / (2*A)
    x2 = (-B - math.sqrt(Delta)) / (2*A)

    print(f"O valor de X1 e: {x1}")
    print(f"O valor de x2 e: {x2}")
# %%