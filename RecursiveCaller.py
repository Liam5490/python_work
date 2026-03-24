swap = 0
recursion = 0 #both will be used as globals

def lomuto(A, left, right):
    global swap
    p = A[right]
    i = left
    for j in range(left, right):
        if A[j] > p:
            A[i], A[j] = A[j], A[i]
            swap += 1
            i += 1
    A[i], A[right] = A[right], A[i]
    swap +=1
    return i

def quicksort(A, left, right):
    global recursion
    if (left < right):
        recursion += 1
        mid = lomuto(A, left, right)
        quicksort(A, left, mid-1)
        quicksort(A, mid+1, right)
        
def main():
    global swap, recursion
    arrays = { 'A': [38, 21, 39, 60, -1, 10, 81, 23],
        'B': [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21],
        'C': [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]}

    for label, array in arrays.items():
        swap = 0
        recursion = 0
        print(f"array {label}: {array}")
        quicksort(array, 0, len(array)-1)
        print(f"descending Sorted array {label}: {array}")
        print(f"number of swaps: {swap}")
        print(f"number of Recursive calls: {recursion}")

main()
