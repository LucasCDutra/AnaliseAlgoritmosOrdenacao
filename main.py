import random

from sortFunctions.bubbleSort import bubbleSort, getInfoBubbleSort
import sortTools as tools
from sortFunctions.insertionSort import insertionSort, getInfoInsertionSort
from sortFunctions.mergeSort import getInfoMergeSort
from sortFunctions.selectionSort import getInfoSelectionSort

#Lista de 1000
tam = 1000

getInfoBubbleSort(tam)
getInfoInsertionSort(tam)
getInfoSelectionSort(tam)
getInfoMergeSort(tam)



#print("=QuickSort     ", sorts.quickSort(listSelected,0,size-1))