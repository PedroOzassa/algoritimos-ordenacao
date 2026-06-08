from time import perf_counter


def juntar(esquerda, direita, trocas):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        trocas += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
        trocas += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1
        trocas += 1

    return resultado


def ordenar(lista, trocas):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = ordenar(lista[:meio], trocas)
    direita = ordenar(lista[meio:], trocas)
    return juntar(esquerda, direita, trocas)


def merge_sort(vetor):
    dados = list(vetor)
    trocas = 0

    inicio = perf_counter()
    dados = ordenar(dados, trocas)
    tempo_execucao = perf_counter() - inicio
    return tempo_execucao, trocas
