import random
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

from bubble_sort import bubble_sort
from insert_sort import insert_sort
from merge_sort import merge_sort


def gerar_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1, 100))
    return vetor

def agregar_media(resultados):
    algoritmos = sorted({r["algoritmo"] for r in resultados})
    tamanhos = sorted({r["tamanho"] for r in resultados})

    dados_agregados = {alg: [] for alg in algoritmos}
    for alg in algoritmos:
        for t in tamanhos:
            tempos = [r["tempo"] for r in resultados if r["algoritmo"] == alg and r["tamanho"] == t and r["tempo"] is not None]
            if tempos:
                dados_agregados[alg].append(mean(tempos))
            else:
                dados_agregados[alg].append(None)

    return tamanhos, dados_agregados

def plotar(resultados, salvar_png=True):
    tamanhos, dados_agregados = agregar_media(resultados)

    plt.figure(figsize=(9, 6))
    for alg, medias in dados_agregados.items():
        ys = np.array([m if m is not None else np.nan for m in medias], dtype=float)
        plt.plot(tamanhos, ys, marker="o", label=alg)

    plt.xscale("log")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo médio (s)")
    plt.title("Desempenho por algoritmo")
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()

    if salvar_png:
        plt.savefig("benchmark.png", dpi=200)
        print("Grafico salvo em benchmark.png")

    plt.show()


vetor1 = gerar_vetor(1000)
vetor2 = gerar_vetor(10000)
vetor3 = gerar_vetor(100000)
dados = []

for i in range(3):
    tempo, trocas = bubble_sort(vetor1)
    dados.append({
        "algoritmo": "Bubble Sort",
        "tentativa": i,
        "tamanho": 1000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = bubble_sort(vetor2)
    dados.append({
        "algoritmo": "Bubble Sort",
        "tentativa": i,
        "tamanho": 10000,
        "tempo": tempo,
        "trocas": trocas,
    })

# Nao acaba em menos de 5 min
for i in range(3):
    tempo, trocas = None, None
    dados.append({
        "algoritmo": "Bubble Sort",
        "tentativa": i,
        "tamanho": 100000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = insert_sort(vetor1)
    dados.append({
        "algoritmo": "Insert Sort",
        "tentativa": i,
        "tamanho": 1000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = insert_sort(vetor2)
    dados.append({
        "algoritmo": "Insert Sort",
        "tentativa": i,
        "tamanho": 10000,
        "tempo": tempo,
        "trocas": trocas,
    })

# Nao acaba em menos de 5 min
for i in range(3):
    tempo, trocas = None, None
    dados.append({
        "algoritmo": "Insert Sort",
        "tentativa": i,
        "tamanho": 100000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = merge_sort(vetor1)
    dados.append({
        "algoritmo": "Merge Sort",
        "tentativa": i,
        "tamanho": 1000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = merge_sort(vetor2)
    dados.append({
        "algoritmo": "Merge Sort",
        "tentativa": i,
        "tamanho": 10000,
        "tempo": tempo,
        "trocas": trocas,
    })

for i in range(3):
    tempo, trocas = merge_sort(vetor3)
    dados.append({
        "algoritmo": "Merge Sort",
        "tentativa": i,
        "tamanho": 100000,
        "tempo": tempo,
        "trocas": trocas,
    })

print(dados)
plotar(dados)