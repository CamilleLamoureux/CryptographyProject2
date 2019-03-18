from functions import algorithm2
print("Welcome ! ! \n"
      "You want to (1 or 2): \n"
      "\t 1- Cipher your own message\n"
      "\t 2- Decipher (you will not choose the message or the key)\n")

choice = int(input("Your choice : "))

# If we want to decipher
if choice == 2:
    cipher = True
    text = list("PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH")
    keyLeft = list("ALZBHGUWIEFJCDYNMQRVKPTOXS")
    keyRight = list("TWXLPRDZMNUGSAQKJHEBCIFYVO")
    offset = 8
    n = 7
    display = int("Do you want to display the table ? (1 or 2)"
                  "\n 1- Yes"
                  "\n 2- No")
    if display == 1:
        display == True
    elif display == 2:
        display == False
    else:
        print("Please try again and make sure your input is 1 or 2.")

    result = algorithm2(text,n,offset,cipher,display)

# If we want to cipher
elif choice == 1:
    cipher = False
    text = list(input("Your message : "))
    n = int(input("Number of lines of your table (n) : "))
    offset = int(input("Your offset : "))
    display = int("Do you want to display the table ? (1 or 2)"
                  "\n 1- Yes"
                  "\n 2- No")
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