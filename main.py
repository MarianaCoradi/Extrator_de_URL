
url = "http://bytebank.com/cambio?moedaOrigem=real" #URL com o http://
print(url)


indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao] #Fatiamaneto tendo o "?" como referência de forma dinâmica
print(url_base)

url_parametros = url[indice_interrogacao+1:]#Caractere após o ? até o fim da URL
print(url_parametros)