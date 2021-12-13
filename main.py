
url = "bytebank.com/cambio?moedaOrigem=real" #Simplificando a URL para o exemplo de faciamento de string
print(url)

url_base = url[0:19] #Fatiamaneto tendo o "?" como referência, porém se adionarmos o http ou mudar a url as posições irão mudar
print(url_base)

url_parametros = url[20:36]
print(url_parametros)