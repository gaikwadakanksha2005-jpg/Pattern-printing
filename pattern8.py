n=5
for i in range(n,0,-1): # for rows
    for j in range(1,n-i+1): #for reverse star pattern
        print(" ",end=" ") #print space
    for k in range(1,i*2): #Increse star by 2 in each line
        print("*",end=" ")
    print()         
