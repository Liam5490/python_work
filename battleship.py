import random 

# the size of the 2 d array
grid_size = 10
# this is the array declaration
twoDarry = [ ['']*grid_size for i in range(grid_size) ]

# display the grid (2d array)
def displayArray(thearray):
    for i in range(grid_size):
        print("",i,end= " ")
    print()
    for i in range(grid_size):
        #print(i) #will print the integers for the row
        for j in range(grid_size):
            print('['+thearray[i][j]+']', end = "")
        print(i)

# initilize the 2 d array (the grid)
def setupArray(thearray):
    i = j = 0

    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            thearray[i][j] = "." # + " ", will allow the . to print
            j += 1
        j = 0
        i += 1 

def rando_ship(thearray, num_ships):
    ships_placed = 0
    while ships_placed < num_ships:
       
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        
        
        if thearray[row][column] != 'S':

            thearray[row][column] = 'S'
            ships_placed += 1

def hit_check(thearray, r, c):
    if thearray[r][c] == 'S':
        thearray[r][c] = "X"
        #check if game over 
    elif thearray[r][c] == '.':
        thearray[r][c] = 'O'

    displayArray(thearray)


def check_gameover(array):
    for i in range (len(array)):
        for k in range (len(array[i])):
        #    print(array[i][k])
            if array[i][k] == 'S':
                return True #if this ever returns true, it will not run line 56
    return False #from 51-55 this will continously run

def final_product(thearray):
    # first set up the array
    setupArray(thearray)

    rando_ship(thearray, 5)

    print("Game grid:")
    displayArray(thearray)
    print(check_gameover(thearray))
    while (check_gameover(thearray)): #change true to a function that checks if the game is over
        row_i = eval(input("select a row: "))
        col_i = eval(input("select a column: "))
        hit_check(thearray,row_i,col_i)
    print("game over")


      
# don't forget to call the main function
# lastly do NOT forget to pass the array we declared
final_product(twoDarry)

