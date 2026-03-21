from util import media, aprovado, mensagem

nome = input("Digite o nome do aluno:")
n1 = float(input("Digite a N1: "))
n2 = float(input("Digite a N2: "))


media = media(n1,n2)
status = aprovado(media)
print(mensagem(nome, media, status))


