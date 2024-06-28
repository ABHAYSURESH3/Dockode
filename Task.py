rowc = int(input("Enter row count: "))
colc = int(input("Enter column count: "))

for row in range(rowc * 4 + 1):
    for col in range(5 + (colc-1) * 4):
        if row % 2 == 0 and col % 4 != 0:
            if (row // 2) % 2 == 0 and (col // 4) % 2==0:
                print("-", end="")
            elif (row // 2) %2 != 0 and (col // 4) %2!=0:
                print("-", end="")
            else: print(" ", end="") 
        elif row % 2 != 0 and col % 4 == 0:
            if (row // 2) % 2 == 0:
                if (col // 4) % 2 == 0:
                    print("/", end="")
                else: print("\\", end="")
            elif (row // 2) % 2 != 0:
                if (col // 4) % 2 != 0:
                    print("/", end="")
                else: print("\\", end="")
        else: print(" ", end="")
    print("")
