
for i in range(5):
    for j in range(0,5-i,1):
        print(end=" ")
    for j in range(0,i*2+1, 1):
        print(end="*")
    print("")
