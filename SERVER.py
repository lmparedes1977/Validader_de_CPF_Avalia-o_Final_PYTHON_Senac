from cpf import *
from arquivo import *
import time


"""Bloco de execução do programa SERVIDOR"""
while True:
    try:        
        entrada = Arquivo.le_json(Arquivo.JSON_ENTRADA)   # Chama função de leitura de arquivo JSON de entrada do usuário via GUI
        if entrada['cpf']:
            cpf = Cpf.recebe_cpf(entrada['cpf'])   # Instanciação do objeto cpf
            retorno =  cpf.valida_cpf()      # Retorno de valiação dos dídigos verificadores
            print(f'{entrada["cpf"]} => {retorno}')   # Impressão de validação em console                
            Arquivo.escreve_json(Arquivo.JSON_RETORNO, {'msg': retorno })   # Chama função gravação de retorno em arquivo JSON
            Arquivo.escreve_json(Arquivo.JSON_ENTRADA, {'cpf': ''})  # Chama função de "limpeza" de entrada para nova consulta (caso sucesso)
    except CpfException as e:  
        Arquivo.escreve_json(Arquivo.JSON_RETORNO, {'msg': str(e) })   # Chama função para gravação de erro em arquivo JSON
        print(f'{entrada["cpf"]} => {e}')  # Impressão de excessão em console
        Arquivo.escreve_json(Arquivo.JSON_ENTRADA, {'cpf': ''})   # Chama função de "limpeza" de entrada para nova consulta (caso erro)
     
    time.sleep(0.2)

