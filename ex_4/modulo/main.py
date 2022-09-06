import Professor as ModuloProfessor

professor = ModuloProfessor.Professor('Cleidson', '35', 2000.00)

print(professor.retorna_dados())
print(professor.acessa_salario('123456789','987654321', 200))

#Output:
# ('Cleidson', '35', 2000.0)
# Você tem permissão para acessar esse método!
# O novo salário de Cleidson é de 2200.0 reais
# None