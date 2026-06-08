from time import perf_counter


def insert_sort(vetor):
    dados = list(vetor)
    trocas = 0

    inicio = perf_counter()

    for i in range(1, len(dados)):
        elemento_atual = dados[i]
        j = i - 1

        while j >= 0 and dados[j] > elemento_atual:
            dados[j + 1] = dados[j]
            trocas += 1
            j -= 1

        dados[j + 1] = elemento_atual

    tempo_execucao = perf_counter() - inicio
    return tempo_execucao, trocas
