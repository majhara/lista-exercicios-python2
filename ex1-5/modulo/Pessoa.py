# Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.

class Pessoa:
    def __init__(self, nome, documento, idade, tipo_pessoa):
        self.nome = nome
        self.documento = documento
        self.idade = idade
        self.tipo_pessoa = tipo_pessoa
        
    def retorna_dados(self):
        return self.nome, self.documento, self.idade
        
    def verifica_tipo(self):
        if self.tipo_pessoa == 'F':
            return f"{self.nome} é fumante"
        if self.tipo_pessoa == 'N':
            return f"{self.nome} não é fumante"
        else:
            return f"Não tenho essa informação sobre {self.nome}"
    
  
    
