# Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it

def make_shirt(size,text):
    print("The shirt's size is " + size + " and the message to be printed on it is: " + text)

#Call the function once using positional arguments to make a shirt. Call the 
#function a second time using keyword arguments.
make_shirt("XL","mBWA!")
make_shirt(size="XL",text="Back in Blood!!!")

