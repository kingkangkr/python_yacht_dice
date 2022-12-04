def score_sort(a):
    def sort(unsorted_list):
        if len(unsorted_list) <= 1:
            return
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        score_sort(left)
        score_sort(right)
        merge(left, right)

    def merge(left, right):
        i = 0
        j = 0
        k = 0
        while (i < len(left)) and (j < len(right)):
            if left[i] > right[j]:
                a[k] = left[i]
                i += 1
                k += 1
            else:
                a[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    sort(a)
    return a