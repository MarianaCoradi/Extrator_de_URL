#Aprendendo expressões regulares
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression --RegEx

# CEP 5 dígitos + hífen (opcional) + 3 dígitos

#Compilação de um padrão com o re.compile():
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #Colocando um limite, ou seja, que o hifen pode aparece de zero até uma vez, para esse exemplo faz o mesmo que o ?

#A busca do padrão feito no re.compile em um endereço com o .search()
busca = padrao.search(endereco) #retorna Match ou None e None é naturalemnte False no if

if busca:
    cep = busca.group()#Extraindo a string q bateu com busca realizada por aquele padrão
    print(cep)