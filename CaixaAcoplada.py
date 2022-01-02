#!/usr/bin/python3
# conding: utf-8
""" Classe CaiaAcoplada """ 

from AlavancaAcionamento import AlavancaAcionamento
from ValvulaAlimentacao import ValvulaAlimentacao
from ComportaVedacao import ComportaVedacao

class CaixaAcoplada(object):
    
    def __init__(self):
        
        print("Construtor da caixa do vaso sanitário")
        self.alavanca = AlavancaAcionamento()
        self.valvula = ValvulaAlimentacao()
        self.comporta = ComportaVedacao()
        self.nivel_maximo = 6.0
        self.nivel_agua = 0
        self.encher_caixa()
        
    def __del__(self):
        print("Removendo caixa acoplada: endereço {}".format(id(self)))
        
    def encher_caixa(self):
        print("Encher a caixa de água")
        while self.nivel_agua < self.nivel_maximo:
            self.nivel_agua = self.nivel_agua + self.valvula.get_vazao()
            if self.nivel_agua > self.nivel_maximo:
                self.nivel_agua = self.nivel_maximo
            print("Nível de água: " + str(round(self.nivel_agua,2)))
            
    def acionar(self, opcao=None):
        print("Acionado o vaso sanitário.")
        
        if type(opcao) == int:
            if opcao == 1:
                print("Número 1. Gastar pouca água.")
                self.alavanca.acionar(opcao)
                self.comporta.abrir()
                self.nivel_agua = self.nivel_maximo / 2
                self.comporta.fechar()
                self.valvula.encher_agua()
                self.encher_caixa()
            elif opcao == 2:
                print("Número 2. ")
                self.alavanca.acionar(opcao)
                self.comporta.abrir()
                self.nivel_agua = 0
                self.comporta.fechar()
                self.valvula.encher_agua()
                self.encher_caixa
            else:
                print("Opção desconhecida.")
        else:
            print("Não é um vaso inteligente...")
            self.alavanca.acionar()
            self.comporta.abrir()
            self.nivel_agua = 0
            self.comporta.fechar()
            self.valvula.encher_agua()
            self.encher_caixa
                      
    def relatorio(self):
        self.alavanca.relatorio()