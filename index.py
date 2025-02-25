# Print the first 10 terms of the Fibonacci series using a  for loop.

# num = int(input("enter number of fibonacci series"))
# a = 0
# b=1
# for i in range(num):
#     print(a)
#     a, b = b, a + b
    
# Check if a given number is a prime number using a  for loop
# num2 = int(input("enter any number"))
# count = 0
# for i in range(2,num2):
#     if num2%2==0:
#         count+=1
# # print(count)
# if count==0:
#     print(num2,"is prime")
# else:
#     print(num2,"is not a prime")



# Write a program to calculate the factorial of a number using a  while  loop.

# num1 = int(input("enter any number"))
# factorial = 1
# i = num1
# while num1>0:
#     factorial*=num1
#     num1-=1
# print(factorial)



# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop. 
# for i in range (1,101):
#     if (i%3==0) and (i%5==0):
#         print(i)


# Implement a basic login system where the user has three 
# attempts to enter the correct password using a loop

# user = int(input("enter any user id"))
# password  = input("enter password")
# attempts = 3
# while attempts>0:
#     if user == 1:
#         if password == "Anil@123":
#             print("login Successfully")
#             break
#         else:
#             attempts-=1
#             if attempts>0:
#                 print("Enter correct password Remaining attempts",attempts)
#                 password  = input("enter any number")
#             else:
#                 print("Your attempts ended sorry")




# Implement a menu-driven program where the user can 
# choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit. 



while True:
    print("Select Below one")
    print("Enter 1 for find square of a number")
    print("Enter 2 for find cube of a number")
    print("Enter 3 for Exit..")
    choice = int(input("Enter Anyone Choice From Menu "))
    if (choice<=3) and (choice>0):
        if choice == 1:
            num = int(input("Enter a Number to find it's Square"))
            print("Square of the Numbere is :",num**2)
            break
        elif choice ==2:
            num = int(input("Enter a Number to find it's Cube"))
            print("Square of the Numbere is :",num**3)
            break
            
        elif choice ==3:
            print("Your entered Exit....")
            break
    else:
        print("Invalid Choice...")
        break

# Write a program that keeps asking the user to enter numbers 
# until they enter a negative number. Use a  while  loop. 
# negative = 0
# while negative==0:
#     user = int(input("Please enter negative numbere only"))
#     if user <0:
#         print("You are entered negative number Thank You")
#         break
        
