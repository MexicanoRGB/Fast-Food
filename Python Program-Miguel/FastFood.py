print('1 - Hamburger - R$10,00')
print('2 - Batata Frita - R$5,00')
print('3 - Refrigerante - R$4,00')
print('4 - Sorvete - R$2,00')

opcao = int(input('Digite o nº da opção desejada:'))
quantidade = int(input('Digite a quantidade desejada:'))
nome = str(input('Digite o nome do cliente:'))

if opcao == 1:
    print('Hamburger sendo preparado para', nome)
    print('Tempo de espera 8 minutos')
    total = quantidade * 10
    print('Total: R$',total)
if opcao == 2:
    print('Batata Frita sendo preparado para', nome)
    print('Tempo de espera 5 minutos')
    total = quantidade * 5
    print('Total: R$',total)
if opcao == 3:
    print('Batata Frita sendo preparado para', nome)
    print('Tempo de espera 1 minutos')
    total = quantidade * 4
    print('Total: R$',total)
if opcao == 4:
    print('Batata Frita sendo preparado para', nome)
    print('Tempo de espera 2 minutos')
    total = quantidade * 2
    print('Total: R$',total)