def insertion_sort(alist):
    counter = 0
    for i in range(1, len(alist)):

        value_to_sort = alist[i]
        while alist[i - 1] > value_to_sort and i > 0:
            alist[i], alist[i - 1] = alist[i - 1], alist[i]
            i -= 1
            counter += 2
    return alist, counter


def selection_sort(alist):
    counter = 0
    for i in range(0, len(alist) - 1):
        min_value = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_value]:
                min_value = j
                counter += 2
        if min_value != i:
            alist[min_value], alist[i] = alist[i], alist[min_value]
    return counter


def merge_sort(alist):
    count = 0
    if len(alist) > 1:
        middle_index = len(alist) // 2
        left_half = alist[:middle_index]
        right_half = alist[middle_index:]


        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        # merge
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index

        while i < len(left_half) and j < len(right_half):
            count += 2
            if left_half[i] < right_half[j]:  # left array less than right array at current index
                count += 1
                alist[k] = left_half[i]  # saves the value of left array inside merge array
                i += 1  # increase i to next index as it is saved in the merge array now
            elif left_half[i] > right_half[j]:
                count += 1
                alist[k] = right_half[j]    # saves the value of right array inside merge array
                j += 1  # increase j index as it is saved inside merge array
            k += 1  # increase k index as new value is in merge array
        count += 1

        # left over element in left array and right array is fully added into merged array
        while i < len(left_half):
            count += 1
            alist[k] = left_half[i]  # saves the last value in the left array into the merge array
            i += 1
            k += 1
        count += 1

        # left over element in right array and left array is fully added into merge array
        while j < len(right_half):
            count += 1
            alist[k] = right_half[j]  # saves the value of right array inside merge array
            j += 1
            k += 1
        count += 1

    return count


#print(selection_sort([23, 10, 49, 12]))
#print(insertion_sort([10, 23, 31, 49]))


