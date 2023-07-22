num1 = 0
numb2 = 0 
with open('done.txt','r') as file1:
    # read line
    line = file1.readlines()
    # changing string line to integer 
    first_line = int(line[0])
    second_line = int(line[1])
    third_line = int(line[2]) 
    # multiplication 
    numb1 = first_line * second_line 
    numb2 = numb1 - third_line

with open('done.txt','w') as file1:
    file1.write(line[0] )
    file1.write(line[1] )
    file1.write(line[2] )  
    file1.write(str(numb2))  

