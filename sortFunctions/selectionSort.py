import sortTools as tools
# ===== selection sort function =====
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            tools.comparacoes +=1
            if arr[min_idx] > arr[j]: #comparacao
                min_idx = j#troca
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #troca
        tools.trocas +=1
    return arr



def getInfoSelectionSort(tam):
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

    # Bubble sort
    #print("======  selectionSort  =====")
    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedOrdenado)#array
    selectionSort(listSelectedOrdenado)
    tools.MarcarTermino()

    print(listSelectedOrdenado)#array
    print("=selectionSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
    print("=selectionSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
    print("=selectionSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
    print("==================")
    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedInverso)#array
    selectionSort(listSelectedInverso)
    tools.MarcarTermino()
    #print(listSelectedInverso)#array
    print("=selectionSort_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=selectionSort_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
    print("=selectionSort_Invertido - PIOR CASO = Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedAleatorio)#array
    selectionSort(listSelectedAleatorio)
    tools.MarcarTermino()
    #print(listSelectedAleatorio)#array
    print("=selectionSort_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=selectionSort_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
    print("=selectionSort_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
    print("==================")
