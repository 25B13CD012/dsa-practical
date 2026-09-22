def linear(a, key):
    for i, x in enumerate(a):
        if x == key:
            return i
    return -1


def binary(a, key):
    lo, hi = 0, len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid

        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def bubble(a):
    for n in range(len(a), 1, -1):
        swapped = False

        for i in range(1, n):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True

        if not swapped:
            break


def insertion(a):
    for i in range(1, len(a)):
        x, j = a[i], i

        while j and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1

        a[j] = x


# Input
a = [34, 7, 23, 32, 5, 62]

# Bubble Sort
b = a.copy()
bubble(b)

print("Bubble:", *b)

# Binary Search
print("Index of 23:", binary(b, 23))

# Insertion Sort
c = a.copy()
insertion(c)

print("Insertion correct:", b == c)

# Linear Search
print("Missing 99:", linear(b, 99))