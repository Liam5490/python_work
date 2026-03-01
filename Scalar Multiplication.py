

def scale (A, s):
    As = []
    for i in range (len(A)):
        As.append([])
        for j in range(len(A[0])):
            As[-1].append(A[i][j] * s)
    return As

A = [[11, 14], [7,18], [0,22]]
print(scale(A, 10))
B = [[8],[6]]
print(scale(B, 0.5))
