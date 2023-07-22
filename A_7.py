dicto_1 = {}
while True:
    user_input = input("what do you want to do: add/delete/exit? \n")
    if user_input == 'add':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        print("here is the dictionary: ")
        dicto_1[key] = value
        for i in dicto_1:
            print("\t-",i," : ", dicto_1[i])
    elif user_input == 'delete':
        key = input("Enter the key: ")
        del dicto_1[key]
        for i in dicto_1:
            print("\t-",i," : ", dicto_1[i])
    elif user_input == 'exit':
        break

