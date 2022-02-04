
user_num= int(input("enter a number: "))

# Implementing the steps for Collatz conjecture using loop
while user_num != 1: #runs until the vaue "1" is returned.
  if user_num % 2 == 0:
   user_num= user_num // 2
   print (user_num)

  else:
   user_num = user_num * 3 + 1
   print (user_num)

print("you have reached the lowest value")
