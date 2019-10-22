class Palavra:


class jogo:
    __init__(self):
        self.vidas = 13
        self.chutes = 0
        self.palavra_escondida = Palavra()
        self.historico_chutes = []

    def chutar(self, letra):
        self.chutes += 1
        letra = letra.upper()
        if self.eh_valido(letra):
            if self.adiciona_historio(letra):
                if self.palavra_escondida.tem_letra(letra):

    def adiciona_historico(self, letra):
        if letra in self.historico_chutes:
            return False
        else:
            self.historico_chutes.append(letra)
            return True            

    def eh_valido(self, letra):
        if len(letra) == 1 and letra.isalpha():
            return True
        else:
            return False



if __name__=="__main__":
    while (jogo.ganhou() and jogo.perdeu()):
        print("----------------------")
        print(f"vidas; {jogo.vidas}")
        print(jogo.palavra_escondida)
        print(f"chutes: {jogo.historico_chutes}")
        print("----------------------")
        letra=input(" Digite uma letra:")
        jogo.chutar(letra)
        if jogo.ganhou():
            print(" voce ficou vivo dessa vez ")
        elif jogo.perdeu():
            print(" chegou a sua hora ")
    

     