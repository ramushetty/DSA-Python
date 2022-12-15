'''
       *
      **
     ***
    ****
'''
def pattern(n):

    k = n - 1
    for i in range(1,n+1):

        for j in range(0,k):
            print(end=" ")
        
        k = k -1

        for i in range(0,i):
            print("*", end="")
        print()

'''
    ****
    ***
    **
    *
'''
def rpattern(n):

    k = n - 1
    for i in range(n,-1,-1):

        for i in range(0,i):
            print("*", end="")

        # for j in range(0,k):
        #     print(end=" ")
        
        # k = k -1

        
        print()


'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
def T_pattern(n):

    k = n - 1
    for i in range(1,n+1):

        for j in range(0,k):
            print(end=" ")
        
        k = k -1

        for i in range(0,i):
            print("*", end=" ")
        print()
# T_pattern(4)
# pattern(4)
rpattern(4)