#!/usr/bin/python3
# conding: utf-8
""" Classe comporta de vedação """


class ComportaVedacao(object):
    """comporta de vedação"""
    
    def __init__(self):
        print("Construtor da comporta de vedação")
        self.status = "FECHADO"
        
    def __del__(self):
        print("Removendo comporta de vedação: endereço {}".format(id(self)))
    
    def abrir(self, vazao=None):
        if vazao == None:
            print("Comporta de vedação aberta. Saindo toda água.")
        else:
            print("Comporta de vedação aberta. Saindo " + str(vazao) + "de água.")
            
        self.status = "ABERTO"
    
    def fechar(self):
        print("Comporta de vedação fechada.")
        self.status = "FECHADO"
        
    def get_status(self):
        return self.status