from util import media, aprovado, mensagem
from util import criar_tabela, inserir_registro, listar_registros

criar_tabela()

nome = input("Digite o nome do aluno:")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))

media = media(n1,n2)
status = aprovado(media)

inserir_registro(nome,n1,n2)

for aluno in listar_registros():
    print(aluno)


