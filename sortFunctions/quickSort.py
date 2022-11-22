import sortTools as tools


# ===== quick sort function =====

def partition(arr, low, high):

  pivot = arr[high]

  i = low - 1


  for j in range(low, high):
    tools.comparacoes += 1
    if arr[j] <= pivot:

      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
      tools.trocas += 2

  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  tools.trocas += 2

  return i + 1


def quickSort(arr, low, high):

  if low < high:

    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)


def getInfoQuickSort(tam):
  # Quick sort
  arrayO = []
  for i in range(tam):
    arrayO.append(i)
  arrayI = []
  for i in range(tam):
    arrayI.append(i)
  arrayA = []
  for i in range(tam):
    arrayA.append(i)

  #Criando variações de array
  listSelectedOrdenado = arrayO  # array ordenado (Melhor Caso)
  listSelectedInverso = tools.PreencherInverso(arrayI)  # array invertido (Pior Caso)
  listSelectedAleatorio = tools.PreencherAleatorio(arrayA)  # array Aleatorio (Caso Padrão)

  print("======  QuickSort  =====")
  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedOrdenado)  # array
  quickSort(listSelectedOrdenado, 0, len(listSelectedOrdenado)-1)
  tools.MarcarTermino()

  print(listSelectedOrdenado)  # array
  print("=QuickSort_Ordenado - MELHOR CASO= Tempo Decorrido (em segundos) = ", tools.tempoDecorrido)
  print("=QuickSort_Ordenado - MELHOR CASO= Tempo Comparações = ", tools.comparacoes)
  print("=QuickSort_Ordenado - MELHOR CASO= Trocas = ", tools.trocas)
  print("==================")

  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedInverso)  # array
  quickSort(listSelectedInverso, 0, len(listSelectedInverso)-1)
  tools.MarcarTermino()
  print(listSelectedInverso)  # array
  print("=Quick_Invertido - PIOR CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
  print("=Quick_Invertido - PIOR CASO = Tempo Comparações = ", tools.comparacoes)
  print("=Quick_Invertido - PIOR CASO = Trocas = ", tools.trocas)
  print("==================")

  tools.ZerarMarcadores()
  tools.MarcarInicio()
  print(listSelectedAleatorio)  # array
  quickSort(listSelectedAleatorio, 0, len(listSelectedAleatorio)-1)
  tools.MarcarTermino()
  print(listSelectedAleatorio)  # array
  print("=Quick_Aleatorio - NORMAL CASO = Tempo Decorrido (em segundos)= ", tools.tempoDecorrido)
  print("=Quick_Aleatorio - NORMAL CASO = Tempo Comparações = ", tools.comparacoes)
  print("=Quick_Aleatorio - NORMAL CASO = Trocas = ", tools.trocas)
  print("==================")