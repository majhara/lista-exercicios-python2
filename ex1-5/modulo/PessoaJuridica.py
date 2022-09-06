import Pessoa as ModuloPessoa

class PessoaJuridica:

    def __init__(self, razao_social, cnpj):
        self.razao_social = razao_social
        self.cnpj = cnpj 
    
    def retorna_dados(self):
        return self.razao_social, self.cnpj