import time
import timeit
import random
import numpy as np
# ===== Variaveis =====

tempoDecorrido = 0
trocas = 0
comparacoes = 0
horaInicio = 0
horaTermino = 0


def PreencherInverso(arr):
    for i in range(len(arr)):
        arr[i] = len(arr) - (i+1)
    return arr

def PreencherAleatorio(arr):
    ar = sorted(arr, key=lambda k: random.random())
    return ar

def ZerarMarcadores():
    global trocas,comparacoes
    trocas = 0
    comparacoes = 0

def MarcarInicio():
    global horaInicio
    horaInicio = timeit.default_timer()

def MarcarTermino():
    global horaTermino, tempoDecorrido, horaInicio
    horaTermino = timeit.default_timer()
    tempoDecorrido = (horaTermino - horaInicio)






