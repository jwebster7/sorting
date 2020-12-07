
def selectionSort(lst):
    '''
    1. Assume the first element to be sorted and the rest to be unsorted.
    2. Assume the first element to be the smallest element.
    3. Check if the first element is less than each of the other elements:
      3a. If true, do nothing.
      3b. Otherwise choose the smaller element, set it as the new minimum, and repeat step 3.
    4. Once one iteration through the list is completed, swap the minimum element with the first element of the list.
    5. Assume the second element in the list to be the smallest and repeat until all the elements in the list are sorted.
    '''
    n = len(lst)
    i = 0

    while i < n:
        min_index = i
        j = i + 1
        while j < n:
            if lst[j] < lst[min_index]:
                min_index = j
            j += 1
        print('\ti={}, lst={}'.format(i, lst))
        lst[i], lst[min_index] = lst[min_index], lst[i]
        i += 1


lst = [10, 2, -5, 8, 4, 1, 7]
print('unsorted list: \n\t{}'.format(lst))
print('using selection sort...')
selectionSort(lst)
print('sorted list: \n\t{}'.format(lst))
