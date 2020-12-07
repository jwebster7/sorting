
def partition(lst, low, high):
    '''
    Helper function for quick sort. 
    '''
    pivot = lst[low]
    left = low + 1
    right = high
    parititioned = False

    while not parititioned:
        while left <= right and lst[left] <= pivot:
            left = left + 1
        while lst[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            parititioned = True
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp

    temp = lst[low]
    lst[low] = lst[right]
    lst[right] = temp

    return right

def quickSort(lst, low, high):
    '''
    1. Assign a pivot (len(array) / 2)
    2. Assign a left pointer (0) and right pointer (length of array - 1).
    3. Compare the element at the left pointer and the element at the right pointer with the pivot.
    4. Check if left element is less than the pivot and if the right element is greater than the pivot:
      4a. If true, increment the left pointer and decrement the right pointer
      4b. Otherwise, swap the left element and right element.
    5. When left >= right, swap the pivot with either the left or right pointer.
    6. Repeat steps 1 - 5 on the left half and the right half of the list till the entire list is sorted.

    * Time complexity: Worst case is O(n^2), but the average case is Θ(nlog(n))
    * Space complexity: O(log(n))
    '''
    if low < high:
        pivot = partition(lst, low, high)
        quickSort(lst, low, pivot-1)
        quickSort(lst, pivot+1, high)


lst = [22, 10, 2, 3, 8, 4, 1, 7, 23]
print('unsorted list: \n\t{}'.format(lst))
print('using quick sort...')
quickSort(lst, 0, len(lst) - 1)
print('sorted list: \n\t{}'.format(lst))
