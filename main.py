
url = "http://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real" #URL com mais parâmetros

# Separa base e parâmetros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_de_busca = 'quantidade'
indice_parametro_de_busca = url_parametros.find(parametro_de_busca)
indice_do_valor = indice_parametro_de_busca + len(parametro_de_busca) + 1
indice_do_e_comercial = url_parametros.find("&", indice_do_valor) #Irá verificar se existe o & apartir do meu indice_do_valor, se não achar...
#... quer dizer que é o meu ultimo parametro e o find irá retorna -1
if indice_do_e_comercial == -1 :
    valor = url_parametros[indice_do_valor:]
else:
    valor = url_parametros[indice_do_valor:indice_do_e_comercial]
print(valor)