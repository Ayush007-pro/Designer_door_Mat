while True:
    my_input = int(input('Enter the number of desired length of design \n'))
    secondINT = my_input*3
    my_input1 = str(my_input)
    my_input2 = str(secondINT)
    var1  = my_input1 + ' ' + my_input2

    N, M = map(int,var1.split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
    for i in range(1,N,2): 
        print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
    print(((M-7)//2)*'-'+'WELCOME'+((M-7)//2)*'-')
    for i in range(N-2,-1,-2): 
        print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')

'''
while True:
    N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
    for i in range(1,N,2): 
        print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
    print(((M-7)//2)*'-'+'WELCOME'+((M-7)//2)*'-')
    for i in range(N-2,-1,-2): 
        print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
'''