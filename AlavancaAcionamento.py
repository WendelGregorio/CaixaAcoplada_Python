#!/usr/bin/python3
# conding: utf-8
""" Classe alavana de acionamento. Aquele botão da caixa d'agua """

class AlavancaAcionamento(object):
    """ alavanca de acionamento """
    
    def __init__(self):
        """Construtor"""
        print("Construtor da alavanca de acionamento")
        self.contador1 = 0
        self.contador2 = 0
        
    def __del__(self):
        """Destrutor"""
        print("Removendo alavanca: endereco {}".format(id(self)))
        
    def acionar(self, opcao=None):
        """ Acionamento a alavanca de acionamento. Pressionaram o botão."""
        print("alavanca de acionamento ativada.")
        if type(opcao) == int:
            if opcao == 1:
                self.contador1 += 1
            else:
                self.contador2 += 1
        else: 
            self.contador2 += 1
            
    def relatorio(self):
        """Relatorio de uso de agua"""
        print("Relatório de uso de água")
        print("")
        print("Número de descargas Opção 1: " + str(self.contador1))
        print("Número de descargas Opção 2: " + str(self.contador2))
    