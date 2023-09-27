import math
from PySimpleGUI import *

class TelaPython:
    
    def __init__(self) -> None:

        layout = [
            [Text('Insira suas notas!')],
            [Text('Nota 1', size=(5,0)),In(size=(5,0),key='nota1')],        
            [Text('Nota 2', size=(5,0)),In(size=(5,0),key='nota2')],          
            [Text('Nota 3', size=(5,0)),In(size=(5,0),key='nota3')],
            [Text('Nota 4', size=(5,0)),In(size=(5,0),key='nota4')],
            [Button('Enviar'),Cancel('Sair')]
        ]

        janela = Window('Dados do Usúario').layout(layout) #Janela
        self.button, self.values = janela.Read()        #extrair os dados da tela

    def Iniciar(self):

        global nota1, nota2, nota3, nota4
        nota1 = int(self.values['nota1'])
        nota2 = int(self.values['nota2'])
        nota3 = int(self.values['nota3'])
        nota4 = int(self.values['nota4'])
       
tela = TelaPython()
tela.Iniciar()

def media():

    variaveis = [nota1, nota2, nota3, nota4]
    soma = sum(variaveis)   
    media = math.ceil(soma/4)
    return media

class TelaResultado(TelaPython):   

    def __init__(self) -> None:
        
        layout = [    
            [Text('Sua nota foi:')],   
            [Text(media())],
            [Cancel('Sair')]
        ]

        janela = Window('Dados do Usúario').layout(layout)#janela
        self.button, self.values = janela.Read() #extrair os dados da tela

tela1 = TelaResultado()


