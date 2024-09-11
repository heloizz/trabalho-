import time

# faltou criar a função
# esse código vai pedir o nome do usuário 
nome = input (" Escreva seu nome")
print("bem-vindo,", nome + "!")

print("Como posso te ajudar hoje?")

print("1 - exames")
print("2 - consulta")
print("3 - prescrição médica")


opcao = int(input("digite o número desejado"))
if opcao == 1:
    print("digite o seu cpf")
elif opcao == 2:
    print("verificar datas diponíveis")
elif opcao == 3:
    print("digite o seu cpf")

else: print("opção não encontrada")

