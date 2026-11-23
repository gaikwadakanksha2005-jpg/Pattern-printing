n=5
for i in range(1,n+1):  #For print rows
    for j in range(1,n-i+1): #give space before stars
        print(" ",end=" ")   #for space
    for k in range(1,i+1):  #For how many time stars are print 
        print("*",end=" ")   # print stars in same line
    print()         

        