# util/valiudacao.py
# Responsabilidade única:?validar dados de entrada do usuário
# Nenhuma logica de janela, banco ou calculo entra aqui. 

def validar_nome(nome:str) -> str:
    """
    Valida se o nome não está vazio:
    Retorma o nome sem espaços extras
    Levanta uma exceção se a validação estiver inválida
    """

    nome = nome.strip() #elimina espaços extras
    if not nome:
        raise ValueError("O campo nome não pode estar vazio")
    return nome

def validar_nota(valor_str:str,campo: str = "Nota") -> float:
    """
    Valida se uma string representa uma nota entre 0 e 10
    Retornar em decimal
    Levanta uma exceção se não estiver no intervalo
    """

    try: 
        nota = float(valor_str)
    except ValueError:  
        raise ValueError(f"{campo}:'{valor_str}', não é um número válido (Ex. 7.5)")
    if not 0 <= nota <= 10: 
        raise ValueError(f"'{campo}': o valor '{valor_str}', está fora do intervalo (0 a 10)")
    return nota

def validar_cep(cep:str) -> str:
    """
    Validar o formato basico de CEP(8 caracteres)
    Retorna o cep sem o traço
    Levanta uma exceção se o formato for inválido
    """

    cep = cep.strip().replace("-","")
    if not cep.isdigit() or len(cep) != 8:
        raise ValueError(f"CEP {cep} inválido. Use o formato: 12345-678")
    return cep
