
def insertionSort(lst):
    '''
    1. Assume the first element to be sorted and the rest to be unsorted.
    2. Compare the first element with the second element:
      2a. If the if the neighboring element is less than the current element, insert the element in the correct position of the sorted portion.
      2b. Otherwise, the neighboring element is in the correct position.
    3. Repeat 1 and 2 until all elements within the list are sorted.

    * Time complexity: Worst case run-time is O(n^2).
    * Space complexity: Worst case is O(1) because I modify the array in place.
    '''
    n = len(lst) - 1
    i = 0

    while i < n:
        if lst[i+1] < lst[i]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        for j in range(i):
            if lst[i] < lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
        i += 1
        print('\ti={}, lst={}'.format(i, lst))


lst = [10, 2, 3, 8, 4, 1, 7]
print('unsorted list: \n\t{}'.format(lst))
print('using insertion sort...')
insertionSort(lst)
print('sorted list: \n\t{}'.format(lst))
