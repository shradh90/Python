"""
   @Author - Shradha Desai
   @Date - 04-NOV-2021
   @Time - 11:50
   * Title - Nth Harmonic Value
"""

def harmonic(num):
    i = 1
    sum = 0

    while i <= num:
        sum += 1 / i
        i += 1
        print(sum)


num = int(input("Enter a Number "))
if num <= 0:
    print("Please enter the no greater than zero.")
else:
    harmonic(num)