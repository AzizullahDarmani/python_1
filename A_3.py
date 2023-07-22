# my method
# sum_number=0
# done=0
# while True:
#     n = int(input("Enter a number between 1 and 10 (or 0 to exit): "))
#     done+=n
         
#     if n==0:
#         print("The program is finished, the final sum is: ",sum_number) 
#         break
    
#     elif n>=1 and n<=10:
#         n
#         sum_number+=n 
#         print("The sum of all your number is: ",done) 
       
    
#     else:
#         print("Sorry, if the number is not between 0 and 10 it's to hard for me.")
#         done-=n 



# teacher's method
total = 0
i = 1
while i != 0:
  i = int(input('You number: '))

  if i > 0 and i <= 10:
    total += i
    print(total)

  elif i < 0 or i > 10:
    print('too hard !')
  

  print('total is:', total)

        