import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" not in dados:
            return {
                "rua": dados["logradouro"],
                "bairro":dados["bairro"],
                "cidade":dados["localidade"],
                "estado":dados["uf"],
                "cep":dados["cep"]
            }
    return None
