def transpose (A):
    AT = []  #The transposed of A, [] creates a list for the matrices to be stored in
    for j in range (len(A[0])):
        AT.append([]) #the j (Column) row of AT
        for i in range (len(A)):
            AT[-1].append(A[i][j])
        return AT
    
B = [[11, 14], [7, 18], [0, 22]]
print(B)
print(transpose(B))

C = [[8],[6]]
print(C)
print(transpose(C))

