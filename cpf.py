from arquivo import *

class Cpf:

    def __init__(self, cpf, registro:Arquivo) -> None:
        """Construtor do objeto"""
        self.__cpf = cpf # recebe cpf que passou por validações iniciais
        self.__reg = registro # recebe objeto da classe Arquivo

    @staticmethod
    def recebe_cpf(cpf:str):
        """ Validações inciais da entrada de dado (nr de dígitos numéricos, 
            presença de caracteres não numéricos direfentes de ponto e hifen,  
            entrada com 11 dígitos iguais.
            Retorna chamada da classmathod gera_objeto """
        recebido = cpf.replace('.', '').replace('-', '')  
        reg = Arquivo.gera_registro(recebido)   # instancia objeto Arquivo com entrada já "limpa"
        if not recebido.isnumeric():
            msg = 'Caracter(es) INVÁLIDOS. Entre apenas números, "." e "-" .'            
            reg.registra_erro(msg)   # chama gravação de log de erro    
            raise CpfException(msg)  # lança exceção
        if len(recebido) != 11:
            msg = f'Número de dígitos INVÁLIDO: {len(recebido)} (NECESSÁRIO 11).'
            reg.registra_erro(msg)
            raise CpfException(msg)        
        if len(set(list(recebido))) == 1:  # verificação se todos os dígitos são iguais
            msg = 'Entrada INVALIDA (DÍGITOS IGUAIS).'
            reg.registra_erro(msg)
            raise CpfException(msg)    
        return Cpf.gera_obj(recebido, reg)

    @classmethod
    def gera_obj(cls, cpf, registro):
        """Classmethod de instanciação do objeto Cpf"""        
        return cls(cpf, registro)

    def valida_cpf(self):
        """Testa cpf (dígitos verificadores 1 e 2)"""
        cpf_list = list(self.__cpf) # torna cpf em lista de strings


        """Validação do primeiro algarismo do dígito verificador"""
        soma = 0   
        mult = 10
        for i in range(9):
            soma += int(cpf_list[i]) * mult
            mult -= 1
        digito_1 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_1 != int(cpf_list[9]):
            msg = 'Primeiro Digito Verificador INVÁLIDO.'
            self.__reg.registra_erro(msg)  # chama função de gravação de log de erro
            raise CpfException(msg)        # levanta exceção

        """Validação do segundo algarismo do dígito verificador"""
        soma = 0  
        mult = 11
        for i in range(10):
            soma += int(cpf_list[i]) * mult
            mult -= 1
        digito_2 = 0 if (soma % 11) < 2 else 11 - (soma % 11)
        if digito_2 != int(cpf_list[10]):
            msg = 'Segundo Digito Verificador INVÁLIDO.'
            self.__reg.registra_erro(msg)
            raise CpfException(msg)

        self.__reg.registra_sucesso()  # chama função de registro de cpf válido.
        return 'OK => CPF VÁLIDO.'  


    def __str__(self) -> str:
        """Método mágico de geração de string do objeto formatada"""
        return f'CPF {self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}' 

    def __del__(self) -> str:
        """Método mágico de destruição do objeto cpf"""
        print(self.__str__() + " deletado com sucesso.")


class CpfException(Exception):
    """Classe para levantamento de exceções da classe Cpf"""
    pass
