import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS

def gerar_palavra_secreta():
    """Gera uma palavra secreta para a forca, vem do arquivo texto"""

    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavras = f_obj.read().splitlines()
        print(palavras)

    return random.choice(palavras)

def verificar_letra_informada(palavra_secreta, suas_tentativas, tentativas):
    """Verifica se a letra dada está correta
    param: palavra secreta Gerada com base no arquivo texto das palavas secretas
    param: suas_tentativas Lista com todas as tentativas
    param: tentativas letra inserida nesta jogada
    return: retorna um status
    """
    status = '' # O status precisa ser zerado toda vez que a função é chamada
    acertos = 0 # Também precisa ser zerado para essa jogada/tentativa

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
        else:
            status += '*'

        if letra.lower() == tentativas.lower():
            acertos += 1

    print(f"\n Acertou {acertos} letra(s), '{tentativas}'")

    return status

def total_tentativas(palavra_secreta):
    """
    Define a quantidade de tentativas de acordo com a palavra secreta
    :param palavra_secreta: Gerada aleatoriamente
    :return: Retorna a quantidade de tentativas
    """
    chances = len(palavra_secreta)
    return chances + TENTATIVAS_ADICIONAIS

def jogo(palavra_secreta):

    """
    Função principal do jogo
    param: palavra gerada a partir do arquivo texto
    return:
    """
    chute = 0
    advinhado = False
    suas_tentativas = []
    chances = total_tentativas(palavra)
    total_chances = chances

    print(f"-Total de chances {chances}")
    while chute < total_chances:
        letra_tentativa = input("\nEntre sua letra: ")
        # Diminuindo as chances de 1 a 1
        chances -= 1

        # Se a letra já foi informada ou advinhada
        if letra_tentativa in suas_tentativas:
          print("****ATENÇÃO**** Você já tentou essa letra")
        elif len(letra_tentativa) == 1:
         # Adicionando a letra no local correto da palavra
         suas_tentativas.append(letra_tentativa)
         resultado = verificar_letra_informada(palavra, suas_tentativas, letra_tentativa)
        if resultado == palavra:
            advinhado = True
            print(f'\nParabéns, você venceu! Palavra é {palavra_secreta}')
            break
        else:
            print(f"\n - {' '.join(resultado)}")
    else:
        print(f"Entrada incorreta, informe somente 1 letra")

        # Mostra quantas tentativas estão restantes
        print(f"\n *** Tentativas restantes {chances}")
        chute += 1
    if chute == total_chances:
        print(f"\n *** Suas tentativas acabaram.A palavra secreta é {palavra_secreta} ***")

