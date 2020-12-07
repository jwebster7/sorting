
def mergeSort(lst):
    '''
    1. Split the unsorted list into groups recursively until there is one element per group
    2. Compare each of the elements and then group them 
    3. Repeat step 2 until the whole list is merged and sorted in the process

    * Time complexity: The worst-case runtime is O(nlog(n))
    * Space complexity: Since we modify the list in place, the space is ~ O(n)
    '''
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        # print('before recursive call...')
        # print('\tleft half={}'.format(left))
        # print('\tright half={}'.format(right))
        mergeSort(left)
        mergeSort(right)
        # print('after recursive call...')

        i = k = j = 0

        # print('\tleft half={}'.format(left))
        # print('\tright half={}'.format(right))
        # print('beginning the merge...')
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            # print('\ti={}, left={}'.format(i, left))
            # print('\tj={}, right={}'.format(j, right))
            # print('\tk={}, lst={}'.format(k, lst))
            k += 1

        # print('accounting for missed elements in the left half...')
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
            # print('\ti={}, left={}'.format(i, left))
            # print('\tk={}, lst={}'.format(k, lst))

        # print('accounting for missed elements in the right half...')
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
            # print('\tj={}, right={}'.format(i, right))
            # print('\tk={}, lst={}'.format(k, lst))


lst = [0, 2, 3, 8, 4, 1, 7]
print('unsorted list: \n\t{}'.format(lst))
print('using merge sort...')
mergeSort(lst)
print('sorted list: \n\t{}'.format(lst))
