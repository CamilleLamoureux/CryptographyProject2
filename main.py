from functions import algorithm2, keyOK
print("Welcome ! ! \n"
      "You want to (1 or 2): \n"
      "\t 1- Cipher your own message\n"
      "\t 2- Decipher a message\n")

choice = int(input("Your choice : "))

# If we want to decipher
if choice == 2:
    cipher = False
    text = list(input('Your cipher text : '))
    offset = int(input('The offset : '))
    n = int(input('The number of lines : '))
    display = int(input("Do you want to display the table ? (1 or 2)"
                  "\n 1- Yes"
                  "\n 2- No \n"))
    if display == 1:
        display == True
    elif display == 2:
        display == False
    else:
        print("Please try again and make sure your input is 1 or 2.")

    result = algorithm2(text,n,offset,cipher,display)

# If we want to cipher
elif choice == 1:
    cipher = True
    text = list(input("Your message : "))

    n = int(input("Number of lines of your table (n) : "))
    offset = int(input("Your offset : "))
    while not keyOK(n, offset):
        print('Please enter a correct key. See ReadMe for more details.')
        n = int(input("Number of lines of your table (n) : "))
        offset = int(input("Your offset : "))

    display = int(input("Do you want to display the table ? (1 or 2)"
                  "\n 1- Yes"
                  "\n 2- No \n"))
    if display == 1:
        display == True
    elif display == 2:
        display == False
    else :
        print("Please try again and make sure your input is 1 or 2.")

    result = algorithm2(text,n,offset,cipher,display)

else :
      print("Please try again and make sure your input is 1 or 2.")

print(result)