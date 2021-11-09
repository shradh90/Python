"""
    @Author - Shradha Desai
    @Date - 04-NOV-2021
    @Time - 11:50
   * Title - Factors of Numbers
"""

fact = 0
num = int(input("Enter the number: "))

for i in range(2, num + 1):
    if num % i == 0:
        for j in range(2, int(i / 2)):
            if i % j == 0:
                fact = 1
                break
        if fact == 0:
            print(i)