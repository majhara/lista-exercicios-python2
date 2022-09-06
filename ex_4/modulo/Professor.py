class Professor:
    
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    def retorna_dados(self):
        return self.nome, self.idade, self.salario
    
    def __modifica_salario(self, valor):
        self.valor = valor
        self.salario += valor
        print(f"O novo salário de {self.nome} é de {self.salario} reais")
    
    def acessa_salario(self, id_usuario, senha, valor):
        if id_usuario == '123456789' and senha == '987654321':
            print("Você tem permissão para acessar esse método!")
            self.__modifica_salario(valor)
        else:
            print("Acesso negado!")
            
        