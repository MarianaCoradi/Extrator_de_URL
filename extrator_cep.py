#Aprendendo expressões regulares
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression --RegEx

# CEP 5 dígitos + hífen (opcional) + 3 dígitos

#Compilação de um padrão com o re.compile():
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") #Coloca o ? Na frente do hifen para mostra q ele é opcional

#A busca do padrão feito no re.compile em um endereço com o .search()
busca = padrao.search(endereco) #retorna Match ou None e None é naturalemnte False no if

if busca:
    cep = busca.group()#Extraindo a string q bateu com busca realizada por aquele padrão
    print(cep)