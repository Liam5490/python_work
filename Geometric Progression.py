A = int(input("Scale Factor: "))
R = float(input("Common_ratio: "))

def sum (A, R, N):
    print("The sum is: ", A * (R ** N - 1)/ (R - 1))

def sum_infinity (A, R):
    if(1 > R > -1):
        print("The GP converges with infinite elements to: ", A /(1-R))
    else:
        print("the sum is infinite")

def n_th (A, R, N): 
    return A * R ** (N-1)






if abs(R) < (1):
    sum_infinity (A, R)
 

    print(f"The first three terms are {n_th (A, R, 1)}, {n_th (A, R, 2)}, {n_th (A, R, 3)}")
elif abs(R) > (1):
    N = int(input("number of terms: "))
    print("GP does not converge")
    sum (A, R, N)

    print(f"The first three terms are {n_th (A, R, 1)}, {n_th (A, R, 2)}, {n_th (A, R, 3)}")



        
