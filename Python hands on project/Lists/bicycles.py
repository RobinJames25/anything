bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())#Accessing the last item in a list
print(bicycles[-2].title())#Accessing the second last item in a list

message ="My First bicycle was a " + bicycles[0].title()+"."
print (message)