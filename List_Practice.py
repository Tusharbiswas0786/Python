#WAP to inpt 3 favourite movie names ans store them as a list

# Movie1 = input("Enter Movie 1 name : ")
# Movie2 = input("Enter Movie 2 name : ")
# Movie3 = input("Enter Movie 3 name : ")

# list = [Movie1 , Movie2 , Movie3]

# print(list)
# print(type(list))

#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,2,1]
list2 = list.copy()

list2.reverse()

if (list == list2):
    print("List is palindrome")
else:
    print("List is not palindrome")
