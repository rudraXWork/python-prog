def mean(string):
    a=len(string)
    b=sum(string)
    mean=b/a
    print(mean)


def median(string):
    no=len(string)
    string.sort()
    if no %2==0:
        median1= string[no//2]
        median2= string[no//2 -1]
        median=(median1+median2)/2
    else:
        median=string[no//2]   
    print(median)    

string=[7,9,9,9,13,21,17,21,22,25,25,29,30,30,30,60,70,70] 
mean(string)
median(string)

# / is used for floating-point division, which means it returns a floating-point number as the result of the division. For example, 5 / 2 would evaluate to 2.5.

# //, on the other hand, is used for integer division, which means it returns the largest whole number that is less than or equal to the result of the division. For example, 5 // 2 would evaluate to 2.
