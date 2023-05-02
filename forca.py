import os
from time import sleep


def limpar():
    os.system("cls")


dicasPedidas = 0
dicas = []
digitadas = []
erradas = []
chances = 5

desafiante = input(" Desafiante seu nome: ")
limpar()
jogador = input(" Jogador seu nome: ")
limpar()


print("PROCESSANDO...")
sleep(2)
limpar()

chave = input(f'{desafiante}, qual é a palavra chave? ')
espacos = "_" * len(chave)
dica1 = input(f'{desafiante}, dica número 1? ')
dica2 = input(f'{desafiante}, dica número 2? ')
dica3 = input(f'{desafiante}, dica número 3? ')


print("PROCESSANDO...")
sleep(2)
limpar()

print(f'{jogador}, palavra chave contém {len(chave)} letras. ')
print(espacos)

while True:
    opcao = input(
        f'{jogador}, digite (0) para jogar, (1) para solicitar dica ou digite (2) para sair:')

    if opcao == "1":
        if dicasPedidas == 0:
            print('Aqui vai sua primeira dica: ', dica1)
            dicas.append(dica1)
            print(" Restam apenas 2 dicas")
            dicasPedidas = 1

        elif dicasPedidas == 1:
            print('Aqui vai sua segunda dica: ', dica2)
            dicas.append(dica2)
            print(" Restam apenas 1 dica")
            dicasPedidas = 2

        elif dicasPedidas == 2:
            print('Sua terceira e última dica é: ', dica3)
            dicas.append(dica3)
            print(" Restam 0 dicas")
            dicasPedidas = 3

        else:
            print("Você já usou todas as dicas!")

    elif opcao == "0":
        letra = input('Qual letra você gostaria de arriscar? ')
        if len(letra) > 1:
            print("Você só pode digitar uma letra por vez!")
            limpar()
            continue
        if letra in chave:
            print("Você acertou uma letra!")
            limpar()
            digitadas.append(letra)
            espacos = ""
            for letra_chave in chave:
                if letra_chave in digitadas:
                    espacos += letra_chave
                else:
                    espacos += "_"
            print(espacos)
            if espacos == chave:
                print(f"Parabéns, {jogador}! Você venceu!")
                break
        else:
            print("Você errou!")
            limpar()
            erradas.append(letra)
            chances -= 1
            print(f"Você tem {chances} chances")
            if chances == 0:
                print(f"Você perdeu, {jogador}!")
                break
    elif opcao == "2":
        print(f"Valeu, {jogador}!")
        break
    else:
        print("Opção inválida!")
        limpar()
        continue
