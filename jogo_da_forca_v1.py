from random import choice
from desenho import desenho


class JogoDaVelha:
    def __init__(self):
        with open('palavras.txt') as arquivo:
            self.lista_palavras = [palavra.strip() for palavra in arquivo]
        self.lista_desenho = desenho
        self.jogo_usuario = []
        self.erros_usuario = []
        self.acertos_usuario = []

    def iniciar(self):
        self.escolher_palavra()
        self.perguntar_usuario()

    def escolher_palavra(self):
        self.palavra = choice(self.lista_palavras)
        print('\033[1;31m-\033[m'*30)
        print(f'\033[1;32ma palavra tem {len(self.palavra)} letras\033[m')
        print('\033[1;31m-\033[m'*30)
        for self.i in self.palavra:
            self.jogo_usuario.append('_')
        self.mostrar_letras()

    def mostrar_letras(self):
        for self.letras in self.jogo_usuario:
            print(f'\033[1;32m{self.letras}\033[m', end=' ')
        print()

    def perguntar_usuario(self):
        self.letra = input(f'\033[1;33mEscolha uma letra: \033[m').lower().strip()
        print('-'*30)
        self.analise()

    def analise(self):
        if self.letra == '' or self.letra == ' ':
            print('\033[0;34mVocê não digitou nada.\033[m')
            self.situacao_jogo()

        elif self.letra in self.erros_usuario and len(self.erros_usuario) != 0:
            print('\033[0;31mVocê ja errou essa letra\033[m')
            print('-'*30)
            self.situacao_jogo()

        elif self.letra in self.acertos_usuario and len(self.acertos_usuario) != 0:
            print(f'\033[0;31mVocê ja acertou essa letra\033[m')
            print('-'*30)
            self.situacao_jogo()

        elif self.letra not in self.palavra:
            self.desenho_forca()

        else:
            for self.k, self.v in enumerate(self.palavra):
                if self.letra == self.v:
                    self.jogo_usuario.pop(self.k)
                    self.jogo_usuario.insert(self.k, self.v)
                    self.acertos_usuario.append(self.v)

            print(f'\033[1;35mVocê acertou a letra: {self.letra}\033[m')
            print()
            self.situacao_jogo()

    def situacao_jogo(self):
        if self.palavra == ''.join(self.jogo_usuario):
            print(
                f'Você ganhou, a palavra é: \033[1;32m{ "".join(self.jogo_usuario).upper()}\033[m')
        else:
            self.mostrar_letras()
            self.perguntar_usuario()

    def desenho_forca(self):
        if len(self.lista_desenho) > 1:
            print(f'\033[1;31m{self.lista_desenho[0]}\033[m')
            self.lista_desenho.pop(0)
            print(
                f'\033[0;31mVocê errou, a letra ({self.letra}) não pertence a palavra.\033[m')
            self.erros_usuario.append(self.letra)
            self.situacao_jogo()
        else:
            print(f'{self.lista_desenho[0]}')
            print('-'*30)
            print('\033[0;41mVOCE PERDEU!!!\033[m')


jogo = JogoDaVelha()
jogo.iniciar()
