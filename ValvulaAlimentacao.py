#!/usr/bin/python3
# conding: utf-8
"""Valvula de Alimentação """

class ValvulaAlimentacao():
    
    def __init__(self):
        print("Construtor da valvula de alimentação")
        self.capacidade_vazao = 1.1
        
    def __del__(self):
        print("Removendo vávula de alimetação: endereço {}".format(id(self)))
        
    def encher_agua(self):
        print("Vazão : " + str(self.capacidade_vazao) + " litros/seg")
        
    def get_vazao(self):
        return self.capacidade_vazao