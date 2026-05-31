c = {
    "limpa": "\033[m",
    "erro": "\033[1;31m", #vermelho
    "sucesso": "\033[1;32m", #verde
    "alerta": "\033[1;33m", #amarelo
    "info": "\033[1;34m", #lilas
    "roxo": "\033[1;35m" #roxo mais pra rosa =/
}
def media(np1, np2, pim=0):
    try:
        resultado = ((np1 + np2)/2) * 0.8 + pim * 0.2
        if 6.68 <= resultado and resultado <= 7:
            resultado =  7
        return resultado
    except (ValueError, TypeError):
        print(f"{c['erro']} ERRO ao fazer o calculo {c['limpa']}")
    except KeyboardInterrupt:
        print(f"{c['erro']} ERRO acao cancelada pelo usuario {c['limpa']}")

def especular(np1, np2):
    try:
        calculo = ((np1 + np2)/2) * 0.8
        diferenca = 7 - calculo
        if diferenca <= 0:
            return f"{c['sucesso']}Voce ja passou, media {media(np1,np2)} (sem precisar do PIM) {c['limpa']}"
        else:
            valor_pim = round(diferenca / 0.2, 2)
            if 6.68 <= valor_pim and valor_pim < 7:
                valor_pim = 7
            else:
                if valor_pim > 10:
                    return "Precisa de mais de 10 no PIM mano =/"
                else:
                    return valor_pim
    except:
        return f"{c['erro']}ERRO ao especular {c['limpa']}"
def exame(media=0, exame=0):
    try:
        return (media + exame)/2
    except:
        return f"{c['erro']}ERRO ao calcular exame {c['limpa']}"