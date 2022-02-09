GST = 0.15
item = float(input("Enter item price:"))
total = item * GST
totalcost = item + total
print(f"total cost is: ${totalcost}")

timesby=1024
num = int(input("Number of Gigabytes:"))
print(f"Number of Gigabytes: {num*timesby}")

a = 323
b = 895
c = 13

a= b % a
b= a//c
c= a % b
d= a//b//c

print(a, b, c)
