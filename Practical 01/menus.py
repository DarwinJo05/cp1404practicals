user_name = input("Enter name: ")
print ("(H)ello \n(G)oodbye \n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print (f"Hello {user_name}")
    elif choice == "G":
        print (f"Goodbye {user_name}")
    else:
        print ("Invalid choice")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = input(">>> ").upper()

print ("Finished message")