def removeElement(num, val):
    for i in num[:]:
        if i == val:
            del num[i]
            
           
    return (len(num))

z = removeElement([0,1,2,2,3,0,4,2], 2)

print(z)
