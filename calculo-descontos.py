#Entrada de dados
valor_compra=float(input("Qual o valor total de sua compra? R$ "))

#Cálculo do desconto
if valor_compra < 200:
    desconto=valor_compra*0.05 #5% de desconto
elif valor_compra < 300:
    desconto=valor_compra*0.1  #10% de desconto
else:
    desconto=valor_compra*0.15 #15% de desconto

#Saída de dados
print(f"O valor do desconto é: {desconto:.2f} reais, e o valor final da compra é: {valor_compra - desconto:.2f} reais.")