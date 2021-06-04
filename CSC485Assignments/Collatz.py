#!/usr/bin/env python3
# Naol Legesse
# I used a pool from multiporcessing to make this program concurrent
from multiprocessing import Pool
"""A program to classify integers according to their Collatz sizes.
(The Collatz size of n is the number of odd integers in the Collatz sequence
that starts from n.)"""

LIMIT = 3000 # Modify it. Use a positive integer.
RUNS = 3

def clear(fileName):
    """Empty the file. Create it if it does not exist."""
    with open(fileName, "w"):
        pass

def append(number, fileName):
    """Append number to textfile fileName."""
    with open(fileName, "a") as file:
        file.write(str(number)+"\n")

def isIn(number, fileName):
    """Return True if number is in the textfile; ohterwise return False."""
    with open(fileName) as file:
        isThere = str(number)+"\n" in file
    return isThere
            
def parity(n):
    """Return 0 if even; return 1 if odd."""
    return n%2

def successor(n):
    """Collatz successor."""
    return n//2 if parity(n)==0 else 3*n+1

def classifyEven(n):
    """Pre-condition: n is even.
       Append n to either oddSizeEvens or evenSizeEvens."""
    s = successor(n) # s=n//2
    # s < n
    # size(n) == size(s).
    if parity(s) == 0: # s is even
        if isIn(s, "c_oddSizeEvens.txt"): # size(s) is odd
            append(n, "c_oddSizeEvens.txt")
        else: # size(s) is even
            append(n, "c_evenSizeEvens.txt")
    else: # s is odd
        if isIn(s, "c_oddSizeOdds.txt"): # size(s) is odd
            append(n, "c_oddSizeEvens.txt")
        else: # size(s) is even
            append(n, "c_evenSizeEvens.txt")

def classifyOdd(n):
    """Pre-condition: n is odd and n>1.
       Append n to either oddSizeOdds or evenSizeOdds."""
    # Calculate terms of Collatz sequence form n until you find a term k < n,
    # and count odd terms as you go (using oddsCounter):
    k = n
    oddsCounter = 0
    # size(n) == size(k) + oddsCounter
    while k >= n: 
        if parity(k) == 1:
            oddsCounter += 1
        k = successor(k)
        # size(n) == size(k) + oddsCounter
    # After the loop:
    # k < n
    # size(n) == size(k) + oddsCounter 
    if parity(k) == 0: # k is even
        if isIn(k, "c_oddSizeEvens.txt"): # size(k) is odd
            if parity(oddsCounter) == 0: # oddsCounter is even
                append(n, "c_oddSizeOdds.txt")
            else: # oddsCounter is odd
                append(n, "c_evenSizeOdds.txt")
        else: # size(k) is even
            if parity(oddsCounter) == 0: # oddsCounter is even
                append(n, "c_evenSizeOdds.txt")
            else: # oddsCounter is odd
                append(n, "c_oddSizeOdds.txt")
    else: # k is odd
        if isIn(k, "c_oddSizeOdds.txt"): # size(k) is odd
            if parity(oddsCounter) == 0: # oddsCounter is even
                append(n, "c_oddSizeOdds.txt")
            else: # oddsCounter is odd
                append(n, "c_evenSizeOdds.txt")
        else: # size(k) is even
            if parity(oddsCounter) == 0: # oddsCounter is even
                append(n, "c_evenSizeOdds.txt")
            else: # oddsCounter is odd
                append(n, "c_oddSizeOdds.txt")

def classify(n):
    """Precondition: n>1.
       Append n to one of the four files."""
    if parity(n) == 0: # n is even
        classifyEven(n)
    else: # n is odd
        classifyOdd(n)
            
def main():
    clear("c_evenSizeEvens.txt")
    clear("c_evenSizeOdds.txt")
    clear("c_oddSizeEvens.txt")
    clear("c_oddSizeOdds.txt")
    append(1, "c_oddSizeOdds.txt") # 1 is a special case.
    #inputs = [] INPUT LIST CHANGED TO LIST COMP
    #for n in range(2, LIMIT+1):# create input list
        #classify(n)
        #inputs.append(n)
        # instead of doing it like above, ose pool from multiporocessing
        # to make an inout list and map the inputs.
    with Pool(50) as p:
        p.map(classify, [x for x in range(2, LIMIT+1)])
    print("Completed!")

if __name__ == "__main__":
    import time
    totalTime = 0
    for _ in range(RUNS):
            start = time.perf_counter()
            main()
            elapsed = time.perf_counter() - start
            print(f"Classifying {LIMIT} integers took {elapsed:0.4f} seconds.\n")
            totalTime += elapsed
    print(f"Average time: {totalTime/RUNS:0.4f} seconds.\n")
        
# A test of correctness:
# LIMIT=16
# evenSizeEvens 10, 14
# evenSizeOdds  5, 7, 15
# oddSizeEvens  2, 4, 6, 8, 12, 16
# oddSizeOdds   1, 3, 9, 11, 13
