from helpers import gerar_palavra_secreta, jogo

if __name__ == '__main__':
        palavra_secreta = gerar_palavra_secreta()
        print(palavra_secreta)

    # For looping que imprima a palavra escondida com ********
print("\n===JOGO DA FORCA===")
print("palavra é: ")
for letra in palavra_secreta:
        print("*", end= "")

    # Calculando o tamanho da palavra
tamanho_palavra = len(palavra_secreta)
print(f"\n A palavra tem {tamanho_palavra} letras.")

