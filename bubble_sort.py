from time import perf_counter


def bubble_sort(vetor):
    dados = list(vetor)
    trocas = 0

    inicio = perf_counter()
    tamanho = len(dados)

    for i in range(tamanho):
        trocou = False
        for j in range(0, tamanho - i - 1):
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
                trocas += 1
                trocou = True
        if not trocou:
            break

    tempo_execucao = perf_counter() - inicio
    return tempo_execucao, trocas
