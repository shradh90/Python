"""
   @Author - Shradha Desai
   @Date - 04-NOV-2021
   @Time - 11:50
   * Title - Flip Coin and print percentage of Heads and Tails
"""
import random

number = input("Please Enter the number:")
number = int(number)
if number <= 0:
    print("Please Enter Positive Integer")
head = 0
tail = 0
for i in range(number):
    coin = random.randint(0, 1)  # we can also use randrange
    if coin <= 0.5:
      
        tail += 1
       
    else:
      
        head += 1
        

        print("Heads percent")
        headPercent = (head / number) * 100
        print(headPercent)
        print("Tails percent")
        tailPercent = (tail / number) * 100
        print(tailPercent)