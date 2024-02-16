def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    matrix = []
    for i in range(n):
        matrix.append([None] * n)
    return matrix

def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count = 0
    for item in arr:
        if item is not None:
            count += 1
        else:
            break
    return count


def get_maximum(arr: list[int]) -> int:
    """
    A function that takes an array as an argument, and WITHOUT using the built-in functions, returns the maximum value of the array.
    """
    max_val = float('-inf')
    for item in arr:
        if item is not None and item > max_val:
            max_val = item
    return max_val


def insertion_sort(arr: list[int]) -> None:
    """
    A void function that takes a single-dimensional array arr as an argument and applies insertion sort on the valid data items in the array, i.e., the non-None values. This is an in-place function, meaning the original array that was passed as a reference will be updated with the sorted values.
     
    The function should not return anything.
    """
    def Insert(lst,index,value, end):
        for i in range(end, index, -1):
            lst[i] = lst[i-1]
        lst[index] = value

    n = length(arr)
    for i in range(1, n):
        current = arr[i]
        for j in range(i):
            if current < arr[j]:
                # print(current, list[j])
                Insert(arr, j, current, i) 
                break
    return None


def partition_and_prevail(arr: list[int]) -> None:
    """
    A void function that takes the array to be sorted as an argument
    and applies the “Partition and Prevail” algorithm to sort the valid
    data items in the array, as explained in the assignment.

    The function should not return anything.
    """
    n= length(arr)
    maxima = get_maximum(arr)
    if n!=0:
      group_size = ((maxima+1) // n ) + 1
      overall_matrix = initialize_matrix(n)
      for item in arr:
          if item != None:
              row = item // group_size
              for j in range(n):
                  if overall_matrix[row][j] == None:
                      overall_matrix[row][j] = item
                      break
      for k in overall_matrix:
          insertion_sort(k)
      i=0 
      while i < n:
          for j in range(0,n):
              for k in range(0,n):
                  if overall_matrix[j][k] != None:
                      arr[i] = overall_matrix[j][k]
                      i=i+1
                  else:
                      break


def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply partition_and_prevail sorting algorithm to get the sorted arrays and returns the output as a one dimensional array.
    """
    with open (filename) as f :
        lines = f.readlines()
    values = lines[0][1:-1].split(',')
    parsed_list = []
    for i in range(0,len(values)):
        if values[i].strip() == "None":
          values[i] = None
        else:
          values[i] = int(values[i].strip())
    partition_and_prevail(values)
    return (values)

# print(main("Inputs/sorting01.txt"))