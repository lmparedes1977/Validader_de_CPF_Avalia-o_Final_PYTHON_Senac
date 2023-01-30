import time
import json

class Arquivo:        

    """Constantes com os nomes dos arquivos utilizados no programa"""    
    TXT_SUCESSO = './resultado.txt'
    LOG_ERRO = './erros.log'
    JSON_ENTRADA = './entrada.json'
    JSON_RETORNO = './retorno.json'

    def __init__(self, dado) -> None:
        """construtor de clase"""  
        self.__dado = dado     
        pass
        
    @classmethod  # 
    def gera_registro(cls, dado):
        """Chama construtor de classe e instancia objeto"""
        return cls(dado)

        
    def registra_sucesso(self):
        '''Grava entradas válidas em arquivo'''
        with open(Arquivo.TXT_SUCESSO, 'a', encoding='utf-8') as valido:
            valido.write(
                f'{self.__str__()} OK - {time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}\n')
                
    
    def registra_erro(self, msg):
        '''Grava log de de erros em arquivo'''
        with open(Arquivo.LOG_ERRO, 'a', encoding='utf-8') as log:
            log.write(
                f'{self.__dado} - {msg} - {time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}\n')
               

    @staticmethod
    def escreve_json(arquivo, dado):
        """Grava um dicionário python em arquivo JSON, ambos especifi na chamada da função"""
        Arquivo.gera_json()
        with open(arquivo, 'w', encoding='utf-8') as arq:
            arq.write(json.dumps(dado, ensure_ascii=False))
        

    @staticmethod    
    def le_json(arquivo):
        """Lê do Arquivo JSON especificado na chamada e retorna dicionário python"""
        Arquivo.gera_json()
        with open(arquivo, 'r', encoding='utf-8') as arq:
            return json.load(arq) 
                

    @staticmethod
    def gera_json():
        """Verifica se os arquivos JSON existem e, em caso negativo, os cria"""
        try:
            open(Arquivo.JSON_ENTRADA, 'r').close()
            open(Arquivo.JSON_RETORNO, 'r').close()
        except:
            with open(Arquivo.JSON_ENTRADA, 'w', encoding='utf-8') as arq:
                arq.write(json.dumps({'cpf': ''}, ensure_ascii=False))
            with open(Arquivo.JSON_RETORNO, 'w', encoding='utf-8') as arq:
                arq.write(json.dumps({'msg': ''}, ensure_ascii=False))


    def __str__(self) -> str:
        """Método mágico para formatação de string de objeto Arquivo"""
        return f'CPF {self.__dado[:3]}.{self.__dado[3:6]}.{self.__dado[6:9]}-{self.__dado[9:]}'

    def __del__(self) -> str:
        """Método mágico para impressão de log no console quando objeto é deletado"""
        print(f'Gravação efetuada com sucesso em {time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time() - 10800))}')                    