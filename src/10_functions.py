# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):

    if n % 2 == 0:

        return True

    else:
        return False

print(is_even(10)) #Returns True
print(is_even(5)) #Returns False





# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

def even_odd(num):

    if (num % 2) == 0:
        return "Even!"
    else:
        return "Odd!"
   

print(even_odd(num))

