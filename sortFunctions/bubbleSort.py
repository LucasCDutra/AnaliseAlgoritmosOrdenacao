import sortTools as tools

# ===== bubble sort function =====
def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            tools.comparacoes +=1
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                tools.trocas +=1

                arr[j] = arr[j + 1]
                tools.trocas +=1

                arr[j + 1] = temp
                tools.trocas +=1
    return arr


def getInfoBubbleSort(tam):
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
    print("======  BubbleSort  =====")
    tools.ZerarMarcadores()
    tools.MarcarInicio()
    print(listSelectedOrdenado)  # array
    bubbleSort(listSelectedOrdenado)
    tools.MarcarTermino()
    print(listSelectedOrdenado)  # array
    print("=BubbleSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
    print("=BubbleSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
    print("=BubbleSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
    print("==================")


    tools.ZerarMarcadores()
    tools.MarcarInicio()
    print(listSelectedInverso)  # array
    bubbleSort(listSelectedInverso)
    tools.MarcarTermino()
    print(listSelectedInverso)  # array
    print("=BubbleSort_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=BubbleSort_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
    print("=BubbleSort_Invertido - PIOR CASO = Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    print(listSelectedAleatorio)  # array
    bubbleSort(listSelectedAleatorio)
    tools.MarcarTermino()
    print(listSelectedAleatorio)  # array
    print("=BubbleSort_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=BubbleSort_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
    print("=BubbleSort_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
    print("==================")
