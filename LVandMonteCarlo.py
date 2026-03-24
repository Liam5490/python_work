import numpy as np
import random 


arraysize = 10000



ones = arraysize//2  #ensures that half the elements are ones
zeros = arraysize - ones #ensures that half the elements are zeroes

arr = np.zeros(arraysize, dtype=int) #sets up the array, sets it to an integer
arr[:ones]=1 #array slices at where the one is found

np.random.shuffle(arr) #randomizer for array


def LasVegas(a: np.ndarray):
    
    n = a.size
    
    SearchOrder = np.random.permutation(n)
    
    for tries, index in enumerate(SearchOrder, start=1):
        if a[index] == 1:
            return index, tries
    
    raise RuntimeError("no one found")
    
index, tries = LasVegas(arr)
print("---las vegas---") 
print(f"size of array: {arraysize}")
print(f"First 1 element location: {index}")
print(f"number of attempts {tries}")



def MonteCarlo(a: np.ndarray, k: int = 10, randoseed: int | None = None): #a is the array, k is the integer set to 10 for the max number of tries
    #randoseed just works like a seed, helps determine the first number

    rng = np.random.default_rng(randoseed)
    n = a.size #tells how many numbers are in the array
    for t in range(1, k + 1):
        index = rng.integers(0, n)  # random index in [0, n)
        if a[index] == 1:
            return True, index, t
    return False, None, k


k = 10 #the fixed number of tries we are working with in monte karlo
found, index, tries = MonteCarlo(arr, k=k)  #calls the monte carlo algorithm

print("----Monte Carlo---")
print(f"Array size: {arraysize} (zeros={zeros}, ones={ones})")
if found:
    print(f"First 1 found at index (0-based): {index}")
    print(f"Number of tries before finding it: {tries}")
else:
    print(f"No 1 found after {tries} attempts (k = {k}).")
