import json #bibliotecas padrão
import sys

import requests #bibliotecas pip

#arquivos locais

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200 :
            return resposta.text
    except:
        print('erro ao fazer requisição', url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer parsing')

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_popupacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
        else:
            print('pais não encontrado')

def mostrar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('moedas do ', pais['name'],':')
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
        else:
            print('pais não encontrado')

#paises = json.loads(resposta.text) #parsing json para python

#print('código http: {}'.format(resposta.status_code)) # retorna o código http

#print(resposta.text)
#print(paises[0])

#print('Quantidade de países: {}'.format(len(paises)))
#for pais in paises:
#    print(pais['name'])

if __name__ == '__main__':
    if len(sys.argv) == 1: #se não tiver nenhum argumento além do nome do arquivo
        print('Bem vindo ao sistema de países!')
        print('Uso: python main.py <ação> <país(moeda, populacao)> ')
        print('Ações disponíveis:\n contagem\n moeda \n população')
    else:
        argumento1 = sys.argv[1]
        if argumento1 == 'contagem':
            print(contagem_de_paises())
            #exit(0) #saiu sem nenhum erro / 1 saiu com erro
        elif argumento1 == 'moeda':
            try:
                argumento2 = sys.argv[2]
                mostrar_moedas(argumento2)
            except:
                print('É preciso passar no nome do país')
        elif argumento1 == 'populacao':
            try:
                argumento2 = sys.argv[2]
                mostrar_popupacao(argumento2)
            except:
                print('É preciso passar no nome do país')
        else:
            print('Argumento inválido')





# texto_da_resposta = requisicao(URL_ALL)
# if texto_da_resposta:
#    texto_depois_do_parsing = parsing(texto_da_resposta)
# if texto_depois_do_parsing:
#    print('contagem de países {}'.format(contagem_de_paises(texto_depois_do_parsing)))
#    print(listar_paises(texto_depois_do_parsing))
# mostrar_popupacao('brazil')
# mostrar_moedas('brazil')
