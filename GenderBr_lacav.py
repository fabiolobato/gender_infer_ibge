#Importando as bibliotecas
import urllib.request
import urllib.parse
import requests

#Declarando as variáveis Globais
url = 'http://servicodados.ibge.gov.br/api/v1/censos/nomes/basica'

def get_gender(nome):
    name = nome
    args_f = {'nome':name, 'sexo':'f'} 
    r_f = requests.get(url, args_f )

    args_m = {'nome':name, 'sexo':'m'} 
    r_m = requests.get(url, args_m )
    
    if(r_m.text == '[]' and r_f.text =='[]'):
        sexo = 'indefinido'
    else:
        f = r_f.json()[0]['rank']
        m = r_m.json()[0]['rank']

        sexo = ''
        if(f< m):
            sexo = 'mulher'
        else:
            sexo = 'homem'
    return sexo