n=5
for i in range(n):  #Uesd for rows
    for j in range(n): #used For columns
        if i==0 or i==n-1 or j==0 or j==n-1: #if any condition is true print it
            print("*",end=" ") #print stars
        else:
            print(" ",end=" ")
    print()        