string = input("Enter a string: ")
reverse = string[::-1]  # This will reverse the string
# print(reverse)

if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
