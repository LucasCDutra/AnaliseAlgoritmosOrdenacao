import sortTools as tools

# ===== merge sort function =====
def mergeSort(arr):
    tools.comparacoes +=1
    if len(arr) > 1:
        r = len(arr)//2
        L = arr[:r]
        M = arr[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        tools.comparacoes += 1
        while i < len(L) and j < len(M):
            tools.comparacoes += 1
            if L[i] < M[j]:
                tools.trocas +=1
                arr[k] = L[i]
                i += 1
            else:
                tools.trocas +=1
                arr[k] = M[j]
                j += 1
            k += 1

        tools.comparacoes += 1
        while i < len(L):
            tools.trocas +=1
            arr[k] = L[i]
            i += 1
            k += 1

        tools.comparacoes += 1
        while j < len(M):
            tools.trocas +=1
            arr[k] = M[j]
            j += 1
            k += 1
    return arr

def getInfoMergeSort(tam):
    arrayO = []
    for i in range(tam):
        arrayO.append(i)
    arrayI = []
    for i in range(tam):
        arrayI.append(i)
    arrayA = []
    for i in range(tam):
        arrayA.append(i)

    # Criando variações de array
    listSelectedOrdenado = arrayO  # array ordenado (Melhor Caso)
    listSelectedInverso = tools.PreencherInverso(arrayI)  # array invertido (Pior Caso)
    listSelectedAleatorio = tools.PreencherAleatorio(arrayA)  # array Aleatorio (Caso Padrão)

    # Merge sort
    print("======  MergeSort  =====")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedOrdenado)#array
    mergeSort(listSelectedOrdenado)
    tools.MarcarTermino()
    #print(listSelectedOrdenado)#array
    print("=mergeSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
    print("=mergeSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
    print("=mergeSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedInverso)#array
    mergeSort(listSelectedInverso)
    tools.MarcarTermino()
    #print(listSelectedInverso)#array
    print("=mergeSort_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=mergeSort_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
    print("=mergeSort_Invertido - PIOR CASO = Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedAleatorio)#array
    mergeSort(listSelectedAleatorio)
    tools.MarcarTermino()
    #print(listSelectedAleatorio)#array
    print("=mergeSort_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=mergeSort_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
    print("=mergeSort_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
    print("==================")
