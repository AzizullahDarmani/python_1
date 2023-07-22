
things = []

# loop until the user enters 'nothing'
while True:
    # print the current list of to-do items
    print("Here is the list:")
    for i in things:
        print(" - " + i)
    
    # ask the user for input
    user_input = input("What do you want to add: ")
    
    # check if the user entered 'nothing', and exit the loop if so
    if user_input == "nothing":
        for i in things: 
            print(" - " + i) 
        print("Goodbye.")
        
        break
    
    # add the user's input to the to-do list
    things.append(user_input)
