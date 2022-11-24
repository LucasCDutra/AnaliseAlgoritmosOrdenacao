import sortTools as tools

# ===== insertion sort function =====
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]#troca
        tools.trocas +=1
        j = i - 1
        tools.comparacoes += 1
        while j >= 0 and key < arr[j]:#comprara
            tools.comparacoes += 1

            arr[j + 1] = arr[j]#troca
            tools.trocas += 1
            j -= 1

        arr[j + 1] = key#troca
        tools.trocas += 1
    return arr




def getInfoInsertionSort(tam):

    # Insertion sort
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

    print("======  InsertionSort  =====")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedOrdenado)  # array
    insertionSort(listSelectedOrdenado)
    tools.MarcarTermino()
    #print(listSelectedOrdenado)  # array
    print("=InsertionSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
    print("=InsertionSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
    print("=InsertionSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedInverso)  # array
    insertionSort(listSelectedInverso)
    tools.MarcarTermino()
    #print(listSelectedInverso)  # array
    print("=Insertion_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=Insertion_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
    print("=Insertion_Invertido - PIOR CASO = Trocas = ", tools.trocas)
    print("==================")

    tools.ZerarMarcadores()
    tools.MarcarInicio()
    #print(listSelectedAleatorio)  # array
    insertionSort(listSelectedAleatorio)
    tools.MarcarTermino()
    #print(listSelectedAleatorio)  # array
    print("=Insertion_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
    print("=Insertion_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
    print("=Insertion_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
    print("==================")
