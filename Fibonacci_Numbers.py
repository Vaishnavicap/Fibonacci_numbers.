n = int(input("Enter the no. of elements : "))
a = 0
b = 1
print("List of ",n, " Fibonacci numbers : ")
print("0 1",end=" ") 
for i in range (2,n):
    sum = a + b
    print(sum , end=" ")
    a = b
    b = sum
