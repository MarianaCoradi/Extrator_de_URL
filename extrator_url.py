import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):

        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro_de_busca = self.get_url_parametros().find(parametro_de_busca)
        indice_do_valor = indice_parametro_de_busca + len(parametro_de_busca) + 1
        indice_do_e_comercial = self.get_url_parametros().find("&", indice_do_valor)

        if indice_do_e_comercial == -1:
             valor = self.get_url_parametros()[indice_do_valor:]
        else:
             valor = self.get_url_parametros()[indice_do_valor:indice_do_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL Geral: " + self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, outro_objeto):
        return self.url == outro_objeto.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url2 = "http://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url2)

print(extrator_url == extrator_url_2)

print("\nO tamanho da URL: {}\n" .format(len(extrator_url)))
print(extrator_url)

valor = extrator_url.get_valor_parametro("moedaDestino")
print("\nO valor do meu parâmetro na URL: {} " .format(valor))