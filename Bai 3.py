# tong so trong xau
import re

str = input("Enter string: ")

list = re.findall(r'-?\d+', str)

sum = sum(int(i) for i in list )
print("Sum of list: ", sum)
