import Pessoa as ModuloPessoa

class PessoaFisica:
    def __init__(self, nome, documento, idade):     
        self.nome = nome
        self.documento = documento
        self.idade = idade
        
    def abrir_empresa(self, razao_social, cnpj, tipo):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.tipo = tipo
        return f"{self.nome} é dono(a) da empresa {self.razao_social}, cujo CNPJ é {self.cnpj} e sua principal atividade é {self.tipo}"
    
    