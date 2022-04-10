# use recursion to print out the numbers from 9 to 0
def countDown(x):
    if(x == 0):
        print("Done!")
    else:
        print(x)
        countDown(x-1)


countDown(9)
