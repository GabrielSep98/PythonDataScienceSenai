#%%

nome = input("Qual o nome do veiculo ? ")
preco = float(input("Qual o preço do veiculo ?"))
desc = int(input("Selecione o desconto = 1- 60% | 2- 30% ou qualquer outro número para 0% de Desconto"))

if desc ==1:
    calc = preco - (preco*60)/100
elif desc == 2:
    calc=preco - (preco*30)/100
else:
    print("Digite uma opção valida")

print(f"O nome do veiculo e: {nome}")
print(f"O preço e: {calc}")

# %%
