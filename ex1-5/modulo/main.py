import Pessoa as ModuloPessoa
import PessoaJuridica as ModuloPessoaJuridica
import PessoaFisica as ModuloPessoaFisica

# Feito isso, crie uma instância 
pessoa = ModuloPessoa.Pessoa('Mayara', '123456789', '27', 'N')

# e retorne esses valores
print(pessoa.retorna_dados())
print(pessoa.verifica_tipo())

# Criando instância de Pessoa Juridica
empresa = ModuloPessoaJuridica.PessoaJuridica('Dorminhoca Pijamas', '123456789/0001-01')

# retornando os dados
print(empresa.retorna_dados())

# invocando o metodo 'abrir empresa'
pessoa2 = ModuloPessoaFisica.PessoaFisica('Jefferson', '1245678545', '27')
print(pessoa2.abrir_empresa('Empresa de Jefferson', '741852963/001-33', 'manutencao de PC'))

