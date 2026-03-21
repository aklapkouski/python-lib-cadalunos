from util import media, aprovado, mensagem
from util import criar_tabela, inserir_registro, listar_registros
from util import buscar_endereco

criar_tabela()

nome = input("Digite o nome do aluno:")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))
cep = input("Digite seu cep: ")
numero_endereco = input("Digite o número do endereço:")

endereco = buscar_endereco(cep)
print(endereco)

media = media(n1,n2)
status = aprovado(media)

# inserir_registro(nome,n1,n2)

# for aluno in listar_registros():
#     print(aluno)


