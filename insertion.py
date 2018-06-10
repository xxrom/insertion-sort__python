def InsertionSort(array):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j - 1] > array[j]:
       swap(array, j - 1, j)
       j -= 1

  return array

def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

if __name__ == '__main__':
  unsortedArray = [-22, 300, 20, 3, 0, -2, 3, -203]
  sortedArray = InsertionSort(unsortedArray)
  print(sortedArray)

