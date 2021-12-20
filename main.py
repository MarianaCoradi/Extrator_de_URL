
url = "http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real" #URL com mais parâmetros

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao] #Fatiamaneto tendo o "?" como referência de forma dinâmica


url_parametros = url[indice_interrogacao+1:]#Caractere após o ? até o fim da URL
print(url_parametros)

parametro_de_busca = 'moedaOrigem'
indice_parametro_de_busca = url_parametros.find(parametro_de_busca)
print(indice_parametro_de_busca)

indice_do_valor = indice_parametro_de_busca + len(parametro_de_busca) + 1
valor = url_parametros[indice_do_valor:]
print(valor)