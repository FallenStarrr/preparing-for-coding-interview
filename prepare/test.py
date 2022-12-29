def quick_sort(ar):
    if len(ar) < 2:
        return ar

    piv  = ar[0]
    big = [i for i in ar[1:] if i > piv]
    small = [i for i in ar[1:] if i < piv]


    return quick_sort(small) + [piv] + quick_sort(big)


def merge_sort(ar):
    if len(ar) > 1:
        mid = len(ar) // 2
        left = ar[:mid]
        right = ar[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        m = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ar[m] = left[l]
                l += 1
            else:
                ar[m] = right[r]
                r += 1
            m += 1

        while l < len(left):
            ar[m] = left[l]
            l += 1
            m += 1

        while r < len(right):
            ar[m] = right[r]
            r += 1
            m += 1





def binary_search(ar, item):
    low = 0
    high = len(ar) - 1
    mid = len(ar) // 2
    guess = ar[mid]
    while low <= high:
        if item == guess:
            return mid
        elif item > guess:
            low = mid + 1

        elif item < guess:
            high  = mid - 1

    return None 



def binary_search_rec(ar, item, low, high):
    mid = len(ar) // 2
    guess = ar[mid]

    if guess == item:
        return mid

    elif item > guess:
        binary_search_rec(ar, item, mid + 1, high)

    else:
        binary_search_rec(ar, item, low, mid - 1)

    return None


def bubble_sort(ar):
    for i in len(ar) - 1:
        for j in len(ar) - 1:
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]


        


list = [2, 3, 4, 22, 11, 10, 4]
list2 = [1, 3, 6, 21, 11, 18, 19]

quick_sort(list)
merge_sort(list2)

print(list)
print(list2)

print(binary_search(list, 3))
print(binary_search_rec(list, 3))







