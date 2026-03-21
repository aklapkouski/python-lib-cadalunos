def mensagem(nome, media, status):
    if status:
        return f"{nome} foi aprovado com a média: {media:.2f}"
    else:
        return f"{nome} foi reprovado com a média: {media:.2f}"