
def bubbleSort(lst):
    '''
    1. One the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on.
    2. Compare each element (lst[i]) with its right side (lst[i + 1]) neighbour.
    3. Swap the smallest element to the left.
    4. Repeating steps 1-3 until the whole list is covered.

    * Time complexity: The orst-case runtime is O(n^2)
    * Space complexity: Space is constant because I perform the swaps in place so O(1)
    '''
    # n - 1 = the last index in the list
    n = len(lst) - 1

    # start at the last index and use 'j' as a runner to continually swap elements.
    while n > 0:
        j = 0
        # j is a runner that swaps neighboring elements if the element to the right of the current is less than the current.
        while j < n:
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        print('\tn={}, lst={}'.format(n, lst))
        n -= 1


lst = [10, 2, 3, 8, 4, 1, 7]
print('unsorted list: \n\t{}'.format(lst))
print('using bubble sort...')
bubbleSort(lst)
print('sorted list: \n\t{}'.format(lst))
