





modelo_carro = str(input("Qual o modelo do carro?: "))
qtd_estoque = int(input("Qual a quantidade de carros desse modelo em estoque?: "))
qtd_alugado = int(input("Qual a quantidade de carros desse modelo que foram alugados no último mês?: "))
vr_locacao = int(input("Qual o valor da locação desse modelo?: "))

estoque = (qtd_estoque - qtd_alugado)
print("Quantidade em estoque:", estoque)
 
vr_total_alugados = (qtd_alugado ** vr_locacao)
print("Valor total por locação", vr_total_alugados)





from time import sleep

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
l.reverse()
for i in l:
        sleep(3)
print ("Fim do programa :)")