def staircase(n):
    for i in range(n):
        for j in range(n):
            if i+j >= 3:
                print("#", end="")
            else:
                print(" ", end="")
        print()

staircase(4)