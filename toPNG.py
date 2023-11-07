import sys
import os
from PIL import Image


def clear():
    return os.system('cls')


sys.argv = ['toPNG.py', 'imagens', 'output']

CAMINHO_IMAGENS = sys.argv[1]
OUTPUT_IMAGENS = sys.argv[2]
OPCAO1 = 's'
OPCAO2 = 'n'

print('Bem vindo ao conversor de imagens para png')

apagar = input('Deseja apagar a imagem após a conversão? S/N: ').lower()
clear()

while apagar == '':
    print("Selecao não inserida")
    apagar = input('Deseja apagar a imagem após a conversão? S/N: ').lower()
    clear()


while apagar not in (OPCAO1, OPCAO2):
    apagar = input(
        'Deseja apagar a imagem após a conversão? S/N: ').lower()
    clear()


if not os.path.exists(CAMINHO_IMAGENS):
    print('Parece que não existe a pasta das fotos, deixa que eu crio')
    print('Pasta sem imagens, por favor abra o programa novamente :/')
    print('Pressione enter para finalizar')
    input()
    clear()
    os.makedirs(CAMINHO_IMAGENS)
    sys.exit()

if not os.path.exists(OUTPUT_IMAGENS):
    print('Parece que não existe a pasta de conversão e, deixa que eu crio')
    print('Pressione enter para continuar')
    input()
    clear()
    os.makedirs(OUTPUT_IMAGENS)

while os.listdir(CAMINHO_IMAGENS) != []:

    while apagar != 's':
        for i in os.listdir(CAMINHO_IMAGENS):
            img = Image.open(f'./{CAMINHO_IMAGENS}/{i}')
            tirarExtensao = os.path.splitext(i)[0]
            img.save(f'./{OUTPUT_IMAGENS}/{tirarExtensao}.png', 'png')
        break
    if apagar == 's':
        for i in os.listdir(CAMINHO_IMAGENS):
            img = Image.open(f'./{CAMINHO_IMAGENS}/{i}')
            tirarExtensao = os.path.splitext(i)[0]
            img.save(f'./{OUTPUT_IMAGENS}/{tirarExtensao}.png', 'png')
            os.remove(f'./{CAMINHO_IMAGENS}/{i}')

    print('Prontinho chefe ^^')
    print('Pressione enter para finalizar')
    input()
    clear()
    break
else:
    print('Parece que não existe a itens na pasta, por favor abra o programa novamente :/')
    print('Pressione enter para finalizar')
    input()
    clear()
    sys.exit()
