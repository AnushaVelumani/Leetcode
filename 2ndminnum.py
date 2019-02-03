#find the 2nd min number from a list of numbers


def min_num(x):
    
    temp = x[0]
    for i in range(len(x)):
        if x[i]<= temp:
            temp=x[i]
    print (temp)


n =min_num([3,2,4,5])




