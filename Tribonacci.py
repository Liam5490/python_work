def tribonocci(n):
    if n < 0:
        print("invalid input") #immediately checks if the input isn't valid
        return None
    elif n == 0: 
        return 0
    elif n == 1 or n == 2:
        return 1
    
    dynamicprogramming = [0] * (n + 1) # a list that is initialized at 0 to index from 0 to n (n+1 to have the final value)
    dynamicprogramming[0] = 0 #each line sets the values to follow tribonaci
    dynamicprogramming[1] = 1
    dynamicprogramming[2] = 1
    #follows a bottom up approach
    
    for i in range(3, n + 1):
        dynamicprogramming[i] = (dynamicprogramming[i - 1] + 
                                 dynamicprogramming[i - 2] +
                                 dynamicprogramming[i - 3]) #adds the values to perform tribonaci
        
    return dynamicprogramming[n]

while True:
    n = int(input("type an integer: "))
    if n >= 0:
        break
    print("type a correct number") #checks for a valid input
    
print(f"Tribonacci({n}) = {tribonocci(n)}")
