#################################
#                               #
#       Python Demo             #
#                               #
#################################

# Standard output
print("Our Demo Program Is Running!")

# Define variables
myString = "The bird is green"
myInt = 57 # int
myFloat = 10.8 #float

char = "A" 

# Strings
name1 = "Hajji"
age1 = "28"
name2 = "Mark"  # <-----
age2 = "43"

# User Data
userName = name1
userAge = age1


# if true:
outputStr = "User: %s Age: %s" % (userName, userAge) # output

print(outputStr) 

# Output
# print("String:", myString)
# print("String: %s" % myString)
# print("Integer: %d" % myInt)
# print("Float: %f" % myFloat)

#############################################################
# Create a List
#############################################################
myList = []
myList.append(myString)
myList.append(myInt)
myList.append(myFloat)

# Output List
# print(myList)

# Add together any numbers in the List
total = 0 # total of all the numbers
for index in myList:
    # Check for integer
    if isinstance(index, int):
        total = total + index
    # Check for Float
    if isinstance(index, float):
        total = total + index

# Output the total
# print(total)
################################################################



#################################################################
# LOGIC
#################################################################
x = 2
# print(x == 2) # prints out True
# print(x == 3) # prints out False
# print(x < 3)  # prints out True

# FUNCTIONS
def add_two_numbers(val1, val2):
    result = val1 + val2
    # print("The answer is: %f" % result)

add_two_numbers(23, 2)  # call the function and pass 2 arguments

##################################################################





####### Tkinter #######
# import tkinter as tk
# print(tk)
# window = tk.Tk()
# label = tk.Label(
#     text="Python Demo\n2nd line",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )
# label.pack()
# window.mainloop()


#################################################################
#       Recursive Function                                      #
#################################################################


def GCF(num1, num2, factor = 0):
    if factor == 0:
        factor = num1 if num1 < num2 else num2

    # Try factor on both numbers
    if num1 % factor == 0 and num2 % factor == 0: # if the factor works for both numbers
        return factor
    else:
        factor -= 1 # if the factor does not work decrement
        return GCF(num1, num2, factor)
    

gcfAnswer = GCF(31, 10)
# print("The greatest common factor is: %d" % gcfAnswer)



