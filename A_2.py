    #my method
# height=int(input("Enter the height of the pyramid: "))
# b=str(input("Which character for the top you want to use? "))
# c=height
# for i in range(1,1*2,2):
#     print(" "*(c-1)+b*1)
#     c-=1
# for i in range(3,height+1):
#     print(" "*(height-i), "/", end="")
#     print(" "*(2*(i-1) - 3),"\\",sep="")
# print("/"+"_"*(2*height-3)+"\\") 


    # teacher's method
height = int(input('Enter the height of the pyramid: '))
peak = input('Which character for the top you want to use? ')

print(' '* (height - 1) + peak)

cnt = 1
for i in range(height - 2, 0, -1):
  print(' ' * i + '/' + ' ' * cnt + '\\')
  cnt += 2

print('/'+ '_'*cnt + '\\')

     

          

    