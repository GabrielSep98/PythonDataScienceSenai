#%%
operacao= int(input("Escolha a operação Matematica: 1= Soma, 2= Subtração, 3-Multiplicação,4-Dividir"))
num1 = float(input("Digite o primeiro numero"))
num2 = float(input("Digite outro numero"))

if operacao == 1:
    resultado = num1+num2
elif operacao == 2:
    resultado = num1-num2
elif operacao == 3:
    resultado = num1*num2
else:
    resultado = num1/num2

print(f"O resultado e: {resultado}")

# %%
