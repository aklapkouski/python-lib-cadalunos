from util.validacao import validar_nome, validar_nota, validar_cep
from util.cep import buscar_endereco
from util.calculos import media, aprovado
from util.banco import inserir_registro

def cadastrar_aluno_cli():
    """
    Conduz o cadastro de um aluno pelo terminal.
    Valida cada campo antes de prosseguir.
    """

    print("\n === CADASTRO DE ALUNO === \n")

    while True:
        try:
            nome = validar_nome(input("Digite o nome do aluno: "))
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        try:
            n1 = validar_nota(input("Digite a nota 1: "), campo="Nota 1")
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        try:
            n2 = validar_nota(input("Digite a nota 2: "), campo="Nota 2")
            break
        except ValueError as e:
            print(f"{e}")

    # leitura e validação do cep
    while True:
        try:
            cep = validar_cep(input("Digite o CEP do aluno: "))
        except ValueError as e:
            print(f"{e}")
            continue

        endereco = buscar_endereco(cep)
        if endereco:
            print(f"{endereco['rua']} - {endereco['cidade']}/{endereco['estado']}")
            break
        else:
            print(" 🤦‍♂️CEP não encontrado, tente novamente!")

        numero = input("Digite o número do endereço (Enter para S/N)").strip()

# Regra de negócio
    #print(n1)
    #print(n2)
    m = media(n1,n2)
    status = aprovado(m) 

# Persistir os dados no banco
#inserir_registro(nome,n1,n2)

def listar_alunos_cli() -> None:
    """ Exibe todos os alunos cadastrados"""
    #ToDo

def iniciar() -> None:
    #criar_tabela()
    cadastrar_aluno_cli()
    #listar_alunos_cli()

