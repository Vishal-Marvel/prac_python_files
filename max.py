a=[]

n=int(input("Enter number of elements:"))
for i in range(n):
    b=int(input("Enter element:"))
    a.append(b)
 
print(a) 
a.sort() 
print(a)
print("Smallest element is:",a[0]) 
print("Largest element is:",a[n-1])
print ("Done by Vishal")
