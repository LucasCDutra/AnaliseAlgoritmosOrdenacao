import random
import sys
sys.setrecursionlimit(100000)


from sortFunctions.bubbleSort import getInfoBubbleSort
from sortFunctions.improvedBubbleSort import getInfoImprovedBubbleSort
from sortFunctions.insertionSort import getInfoInsertionSort
from sortFunctions.mergeSort import getInfoMergeSort
from sortFunctions.quickSort import getInfoQuickSort
from sortFunctions.selectionSort import getInfoSelectionSort

#from sortFunctions.bubbleSort import bubbleSort, getInfoBubbleSort
import sortTools as tools
#from sortFunctions.insertionSort import insertionSort, getInfoInsertionSort
#from sortFunctions.mergeSort import getInfoMergeSort
#from sortFunctions.selectionSort import getInfoSelectionSort

#Lista de 1000
tam = 10000

#getInfoBubbleSort(tam)
#getInfoInsertionSort(tam)
#getInfoSelectionSort(tam)
#getInfoMergeSort(tam)
getInfoQuickSort(tam)
#getInfoImprovedBubbleSort(tam)


#print("=QuickSort     ", sorts.quickSort(listSelected,0,size-1))