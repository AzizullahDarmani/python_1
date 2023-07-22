def divisor_number(div1, div2, numb):
    if div1 ==0 or div2 ==0: 
        return True 
    return numb%div1 == 0 and numb % div2 == 0
     
answer = divisor_number(0,1,6) 
print(answer) 