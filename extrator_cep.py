#Aprendendo expressões regulares
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression --RegEx

# CEP 5 dígitos + hífen (opcional) + 3 dígitos

#Compilação de um padrão com o re.compile():
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") #Colocando o hifen de 0-9 nos conjuntos nos mostra que os dígitos de 0 ATÉ 9 são válidos ...
#...e o {numero} na frente nos mostra o quantificadores, que são quantos conjuntos daquilo irá repetir

#A busca do padrão feito no re.compile em um endereço com o .search()
busca = padrao.search(endereco) #retorna Match ou None e None é naturalemnte False no if

if busca:
    cep = busca.group()#Extraindo a string q bateu com busca realizada por aquele padrão
    print(cep)