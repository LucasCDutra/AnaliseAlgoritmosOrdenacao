import sortTools as tools


# ===== improved bubble sort function =====

def improvedBubbleSort(arr):
    for i in range(len(arr)):

        swapped = False

        for j in range(0, len(arr) - i - 1):

            tools.comparacoes += 1
            if arr[j] > arr[j + 1]:

                temp = arr[j]
                tools.trocas += 1
                arr[j] = arr[j + 1]
                tools.trocas += 1
                arr[j + 1] = temp
                tools.trocas += 1

                swapped = True


        if not swapped:
            break

def getInfoImprovedBubbleSort(tam):
  # ImprovedBubble sort
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

  print("======  ImprovedBubbleSort  =====")
  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedOrdenado)  # array
  improvedBubbleSort(listSelectedOrdenado)
  tools.MarcarTermino()

  print(listSelectedOrdenado)  # array
  print("=ImprovedBubbleSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
  print("=ImprovedBubbleSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
  print("=ImprovedBubbleSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
  print("==================")

  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedInverso)  # array
  improvedBubbleSort(listSelectedInverso)
  tools.MarcarTermino()
  print(listSelectedInverso)  # array
  print("=ImprovedBubble_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
  print("=ImprovedBubble_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
  print("=ImprovedBubble_Invertido - PIOR CASO = Trocas = ", tools.trocas)
  print("==================")

  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedAleatorio)  # array
  improvedBubbleSort(listSelectedAleatorio)
  tools.MarcarTermino()
  print(listSelectedAleatorio)  # array
  print("=ImprovedBubble_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
  print("=ImprovedBubble_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
  print("=ImprovedBubble_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
  print("==================")
