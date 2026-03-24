import numpy as np



 
NumbofVars = int(input("Enter the number of inputs: ")) #checks number of variables

CoEffofFunction = [float(x) for x in input( "Enter the coefficients of each variable (for example: 3000 2000 2000): ").split()] #.split is put in just to make sure there is spacing between the numbers

SquareConstraints = input("Enter the data for the square matrix stating the constraints via a semi colon and space\n" "(ex: 2 1 8;4 2 0;5 4 3): "
)

A = [] #stores the input from squareconstraints
for row in SquareConstraints.strip().split(";"):  #uses the ; as a divider like in the class example
    A.append([float(x) for x in row.strip().split()])


ConLimits = [float(x) for x in input("Enter the constraint limits; separate each value with a space (example: 300 200 300): "
).split()] #same line of thinking as the earlier input

f = np.array(CoEffofFunction, dtype=float) #every list is converted to an array, allows for floating points
A = np.array(A, dtype=float)
b = np.array(ConLimits, dtype=float)

profits = []
units = []
for j in range (NumbofVars):#takes in the the variables and considers which produces the highest profit 
    col = A[:, j]
    ratios = np.where(col > 0, b / col, np.inf)#checks for the ratio
    maximum= float(np.min(ratios))#gives the maximum value as a float
    profit = maximum * f[j]
    profits.append(profit)
    units.append(maximum)



    print(f"If only variable {j+1} is made, profit is: {profit:.2f}, units produced: {maximum:.2f}")
    
def Profit(k):
    return profits[k]

Bestvariation = max(range(NumbofVars), key=Profit) #key for profit to check which is the highest, giving us the largest profit 
bestProfit = profits[Bestvariation] 

if np.isfinite(bestProfit):
    print(f"the greatest profit is {bestProfit} at variation {Bestvariation}")
else:
    print("Problem with input, please run again")

    

    
try:
    xunit = np.linalg.inv(A).dot(b)
    totalprofit = float(np.dot(f, xunit))
    print("\nSolution:")
    for i, val in enumerate(xunit):
        print(f"Variable {i+1} = {val:.6g}") 
    print(f"Total profit = {totalprofit:.6g}")#both put within point six to show full float

except np.linalg.LinAlgError:
    print("cannot solve")


        

        
