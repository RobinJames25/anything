size=int(input("Enter the size of the array:"))
 
arr=[]

i=0

while i<=size:
    arr.append(i)
    i+=1

new_container=arr[::-1]

print(arr)
print(new_container)

for item in new_container:
    print(item, end=' ')