import random
import sys
sys.setrecursionlimit(10000000)


from sortFunctions.bubbleSort import getInfoBubbleSort
from sortFunctions.improvedBubbleSort import getInfoImprovedBubbleSort
from sortFunctions.insertionSort import getInfoInsertionSort
from sortFunctions.mergeSort import getInfoMergeSort
from sortFunctions.quickSort import getInfoQuickSort
from sortFunctions.selectionSort import getInfoSelectionSort

import sortTools as tools


#Elementos da Lista
tam = 1000

getInfoBubbleSort(tam)
getInfoInsertionSort(tam)
getInfoSelectionSort(tam)
getInfoMergeSort(tam)
getInfoQuickSort(tam)
getInfoImprovedBubbleSort(tam)
