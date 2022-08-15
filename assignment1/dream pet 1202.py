DREAM_PET_BANNER = r"""/===============================================================================\
|   _____    ______   ______   ______   __    __       ______  ______  ______   |
|  /\  __ \./\  == \ /\  ___\ /\  __ \ /\ "-./  \     /\  == \/\  ___\/\__  _\  |
|  \ \ \/\ \\ \  __< \ \  __\ \ \  __ \\ \ \-./\ \    \ \  _-/\ \  __\\/_/\ \/  |
|   \ \____ /\ \_\ \_\\ \_____\\ \_\ \_\\ \_\ \ \_\    \ \_\   \ \_____\ \ \_\  |
|    \/____/  \/_/ /_/ \/_____/ \/_/\/_/ \/_/  \/_/     \/_/    \/_____/  \/_/  |
\===============================================================================/"""

LIVING_ROOM_BANNER = r"""
               _     _       _              ______                      
              | |   (_)     (_)             | ___ \                     
              | |    ___   ___ _ __   __ _  | |_/ /___   ___  _ __ ___  
              | |   | \ \ / / | '_ \ / _` | |    // _ \ / _ \| '_ ` _ \ 
              | |___| |\ V /| | | | | (_| | | |\ \ (_) | (_) | | | | | |
              \_____/_| \_/ |_|_| |_|\__, | \_| \_\___/ \___/|_| |_| |_|
                                      __/ |                             
                                     |___/ 
"""

KITCHEN_BANNER = r"""
                     _   __ _  _          _
                    | | / /(_)| |        | |
                    | |/ /  _ | |_   ___ | |__    ___  _ __
                    |    \ | || __| / __|| '_ \  / _ \| '_ \
                    | |\  \| || |_ | (__ | | | ||  __/| | | |
                    \_| \_/|_| \__| \___||_| |_| \___||_| |_|
"""

GARDEN_BANNER = r"""
                     _____                   _              
                    |  __ \                 | |             
                    | |  \/  __ _  _ __   __| |  ___  _ __  
                    | | __  / _` || '__| / _` | / _ \| '_ \ 
                    | |_\ \| (_| || |   | (_| ||  __/| | | |
                     \____/ \__,_||_|    \__,_| \___||_| |_|        
"""


GAME_SETUP_BANNER = "\n===================================GAME SETUP===================================="
GAME_START_BANNER = "\n===================================GAME START===================================="
STATUS_BANNER = "\n=====================================STATUS======================================"
GAME_END_BANNER = "\n====================================GAME END====================================="

# START YOUR PROGRAM BELOW
print(DREAM_PET_BANNER)

#First message Enter a name and say nice to see you
name=input("Welcome to Dream Pet. May I grab your name please. ")
print("Nice to see you "+name+". I hope you enjoy our short interaction.")

#State data entry Distinguish different situations and set problems
print(GAME_SETUP_BANNER)
number_option=input("Now, tell me "+name+", would you like one or two pets? (1/2) ")

#Select an animal and ask the following questions Convert input to lowercase
if number_option =="1": #Select an animal and ask the following questions Convert input to lowercase
    pet1_type=input("What type of animal is your pet? (Cat/Dog)? ").lower()
    pet1_name=input("What is this "+pet1_type+" called? ")
    pet1_room=input("Where is "+pet1_name+" right now? (Living Room/Kitchen/Garden) ").lower() 
    hunger1_value=float(input("What is "+pet1_name+"'s hunger value? "))
    happiness1_value=float(input("What is "+pet1_name+"'s happiness value? "))
    if pet1_type=="cat": # pet cat sound
        pet1_happy_sound="Meow"
        pet1_angry_sound="Hisssss"
    else: # pet dog sound
        pet1_happy_sound="Woof"
        pet1_angry_sound="Grrrrrr"
elif number_option =="2": #Select two animal and ask the following questions Convert input to lowercase
    pet1_type=input("What type of animal is your first pet? (Cat/Dog)? ").lower()
    pet1_name=input("What is this "+pet1_type+" called? ")
    pet1_room=input("Where is "+pet1_name+" right now? (Living Room/Kitchen/Garden) ").lower()
    hunger1_value=float(input("What is "+pet1_name+"'s hunger value? "))
    happiness1_value=float(input("What is "+pet1_name+"'s happiness value? "))
    pet2_type=input("What type of animal is your second pet? (Cat/Dog)? ").lower()
    pet2_name=input("What is this "+pet2_type+" called? ")
    pet2_room=input("Where is "+pet2_name+" right now? (Living Room/Kitchen/Garden) ").lower()
    hunger2_value=float(input("What is "+pet2_name+"'s hunger value? "))
    happiness2_value=float(input("What is "+pet2_name+"'s happiness value? "))
    if pet1_type=="cat": # pet1 cat sound
        pet1_happy_sound="Meow"
        pet1_angry_sound="Hisssss"
    else: #pet1 dog sound
        pet1_happy_sound="Woof"
        pet1_angry_sound="Grrrrrr"
    if pet2_type=="cat": # pet2 cat sound
        pet2_happy_sound="Meow"
        pet2_angry_sound="Hisssss"
    else: # pet2 dog sound
        pet2_happy_sound="Woof"
        pet2_angry_sound="Grrrrrr"

#the number of successful interactions
pet1_time_spent=0
pet2_time_spent=0

#Game Status
print(STATUS_BANNER)
print(name+", here is a summary of the current status of your pets:")

#The status of choosing an animal
if happiness1_value>100: #for one pet limit happiness1_value
    happiness1_value=100.00
elif happiness1_value<0:
    happiness1_value=0.00
if hunger1_value>100: #for one pet limit happiness1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
print("Your little "+pet1_type+", "+pet1_name+", is in the "+pet1_room+" and is "+format(happiness1_value,".2f")+"% happy and "+format(hunger1_value,".2f")+"% hungry.")
if number_option == "2": #The status of choosing two animals
    if happiness2_value>100: #for pet2 limit happiness2_value
        happiness2_value=100.00
    elif happiness2_value<0:
        happiness2_value=0.00
    if hunger2_value>100: #for pet2 limit happiness2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    print("Your little "+pet2_type+", "+pet2_name+", is in the "+pet2_room+" and is "+format(happiness2_value,".2f")+"% happy and "+format(hunger2_value,".2f")+"% hungry.")

#Game Start
print(GAME_START_BANNER)

#In the Living Room
print(LIVING_ROOM_BANNER)
if pet1_room=="living room": #The situation of a pet
    print(pet1_happy_sound+", "+pet1_name+" is in the living room!")
if number_option == "2" and pet2_room=="living room": #The situation of two pets
    print(pet2_happy_sound+", "+pet2_name+" is in the living room!")

action_living=input("We are in the living room, which of the following actions would you like to perform? (Interact/Find/Leave) ").lower() #The player selects an action
pet_food=False # did not find pet food
if action_living == "interact": #Interactions with the pet
    while number_option =="1": #The player owns 1 pet. There are two interactions when pets move from other places to the living room
        if pet1_room == "living room":#Pet in the living room
            pet_play=input(name+", do you want to pet or play with "+pet1_name+"? (Pet/Play) ").lower()
            if pet_play=="pet":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
            elif pet_play=="play":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
            pet1_time_spent=pet1_time_spent+1 #interaction successful
        elif pet1_room != "living room":#Pet not in the living room
            pet_call=input(pet1_name+" is not in the living room, do you want to call it? (Yes/No) ").lower()
            if pet_call =="yes": #call pet
                if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    pet1_room="living room" #Pet moves to living room
                    pet1_time_spent=pet1_time_spent+1
                    continue #Carry out the situation of pet in the living room
                else: #Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
        action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
        break #Proceed to the next action
    while number_option =="2": #The player owns 2 pets
        if pet1_room != "living room" and pet2_room != "living room": #0 pet in the living room
            pet_call=input("No pet is in the living room, who do you want to call? ("+pet1_name+"/"+pet2_name+"/Both) ")
            if pet_call==pet1_name: #Call pet 1
                if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    pet1_room="living room"
                    pet1_time_spent=pet1_time_spent+1 #interaction successful
                else: #Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    action_living=input("None of the pets are here, which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
            elif pet_call==pet2_name: #Call pet 2
                if happiness2_value>=20 and hunger2_value<90: # Call succeeded
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                    pet2_room="living room"
                    pet2_time_spent=pet2_time_spent+1 #interaction successful
                else: #Call failed
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    action_living=input("None of the pets are here, which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
            else: #Call pet 1 and 2
                if happiness1_value>=20 and hunger1_value<90 and happiness2_value>=20 and hunger2_value<90:# 2 pets Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                    pet1_room="living room"
                    pet2_room="living room" 
                    pet1_time_spent=pet1_time_spent+1 #interaction successful
                    pet2_time_spent=pet2_time_spent+1 #interaction successful
                elif (happiness1_value>=20 and hunger1_value<90) or (happiness2_value>=20 and hunger2_value<90):# 1 pet Call succeeded
                    if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                        print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                        print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                        pet1_room="living room"
                        pet1_time_spent=pet1_time_spent+1 #interaction successful
                    else: # pet2 Call succeeded
                        print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                        print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                        pet2_room="living room"
                        pet2_time_spent=pet2_time_spent+1 #interaction successful
                else: # no pets Call succeeded
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    action_living=input("None of the pets are here, which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
        elif not (pet1_room == "living room" and pet2_room == "living room" ) and (pet1_room == "living room" or pet2_room == "living room"):#1 pet in the living room
            if pet1_room == "living room": # pet1 in the living room
                pet1_cpp=input(name+", do you want to call "+pet2_name+", or pet or play with "+pet1_name+"? (Call/Play/Pet) ").lower() #Choose an action with pet1
                if pet1_cpp=="call": #call pet2
                    if happiness2_value>=20 and hunger2_value<90: # pet2 Call succeeded
                        print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                        pet2_room="living room"
                        pet2_time_spent=pet2_time_spent+1 #interaction successful
                    else: # pet2 Call failed
                        print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                elif pet1_cpp=="play": #play with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                    hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                    pet1_time_spent=pet1_time_spent+1 #interaction successful
                    action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
                else: #pet with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                    pet1_time_spent=pet1_time_spent+1 #interaction successful
                    action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
            else: # pet2 in the living room
                pet2_cpp=input(name+", do you want to call "+pet1_name+", or pet or play with "+pet2_name+"? (Call/Play/Pet) ").lower() #Choose an action with pet2
                if pet2_cpp=="call": #call pet1
                    if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                        print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                        pet1_room="living room"
                        pet1_time_spent=pet1_time_spent+1
                    else: # pet1 Call failed
                        print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                elif pet2_cpp=="play": #play with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                    hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                    pet2_time_spent=pet2_time_spent+1
                    action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
                else: #pet with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                    pet2_time_spent=pet2_time_spent+1
                    action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
                    break
        if pet1_room == "living room" and pet2_room == "living room": #2 pets in the living room
            pet_play=input("Both "+pet1_name+" and "+pet2_name+" are in the living room! Do you want to pet or play with them? (Pet/Play) ").lower()
            if pet_play=="pet": #pet with 2 pets
                pet_choice=input(name+", your choice is "+pet_play+", who do you want to interact with? ("+pet1_name+"/"+pet2_name+"/Both) ")
                if pet_choice.lower()=="both":
                    pet_choice=[ pet1_name, pet2_name ]
                if pet1_name in pet_choice: #pet with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                    pet1_time_spent=pet1_time_spent+1
                if pet2_name in pet_choice: #pet with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                    pet2_time_spent=pet2_time_spent+1  
            else: #play with 2 pets
                pet_choice=input(name+", your choice is "+pet_play+", who do you want to interact with? ("+pet1_name+"/"+pet2_name+"/Both) ")
                if pet_choice.lower()=="both":
                    pet_choice=[ pet1_name, pet2_name ]
                if pet1_name in pet_choice: #play with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                    hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                    pet1_time_spent=pet1_time_spent+1
                if pet2_name in pet_choice: #play with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                    hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                    pet2_time_spent=pet2_time_spent+1
            action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
            break
        elif pet1_room == "living room":
            pet1_play=input(name+", do you want to pet or play with "+pet1_name+"? (Pet/Play) ").lower()
            if pet1_play=="pet":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
            elif pet1_play=="play":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
            pet1_time_spent=pet1_time_spent+1 #interaction successful
        elif pet2_room == "living room":
            pet2_play=input(name+", do you want to pet or play with "+pet2_name+"? (Pet/Play) ").lower()
            if pet2_play=="pet":
                if pet2_type=="dog":
                    print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                else:
                    print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
            elif pet2_play=="play":
                if pet2_type=="dog":
                    print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                else:
                    print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
            pet2_time_spent=pet2_time_spent+1 #interaction successful
        action_living=input(name+", which one of the following actions would you like to perform next? (Find/Leave) ").lower()
        break
if action_living=="find": #The player finds pet food
    pet_food=input("Which type of pet food do you want to look for? (Simple/Lavish) ").lower()
    if pet_food=="simple":
        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
    else: #lavish food
        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
    print("Great, now we have some pet food, lets go to the kitchen!")
if action_living=="leave": #The player leaves the living room
    print("Alright, lets move on to the kitchen immediately!")

#Game Status
print(STATUS_BANNER)
print(name+", here is a summary of the current status of your pets:")
if happiness1_value>100: #for one pet limit happiness1_value
    happiness1_value=100.00
elif happiness1_value<0:
    happiness1_value=0.00
if hunger1_value>100: #for one pet limit happiness1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
print("Your little "+pet1_type+", "+pet1_name+", is in the "+pet1_room+" and is "+format(happiness1_value,".2f")+"% happy and "+format(hunger1_value,".2f")+"% hungry.")
if number_option == "2": #The status of choosing two animals
    if happiness2_value>100: #for pet2 limit happiness2_value
        happiness2_value=100.00
    elif happiness2_value<0:
        happiness2_value=0.00
    if hunger2_value>100: #for pet2 limit happiness2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    print("Your little "+pet2_type+", "+pet2_name+", is in the "+pet2_room+" and is "+format(happiness2_value,".2f")+"% happy and "+format(hunger2_value,".2f")+"% hungry.")

# In the Kitchen
print(KITCHEN_BANNER)
if pet1_room=="kitchen":
    print(pet1_happy_sound+", "+pet1_name+" is already in the kitchen waiting for you!")
if number_option == "2" and pet2_room=="kitchen": #The situation of two pets
    print(pet2_happy_sound+", "+pet2_name+" is already in the kitchen waiting for you!")

action_kitchen=input("Now that we are in the kitchen, what would you like to do? (Interact/Prepare/Leave) ").lower() #The player selects an action in kitchen
pet_feed=0 #did not feed pet now 
if action_kitchen == "interact": #Interactions with the pet in kitchen
    while number_option =="1": #The player owns 1 pet
        if pet1_room == "kitchen":#Pet in the kitchen
            pet_play=input(name+", do you want to pet or play with "+pet1_name+"? (Pet/Play) ").lower()
            if pet_play=="pet":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
            elif pet_play=="play":
                if pet1_type=="dog":
                    print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                else:
                    print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
            pet1_time_spent=pet1_time_spent+1
            action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
            break #Proceed to the next action
        elif pet1_room != "kitchen":#Pet not in the kitchen
            pet_call=input(pet1_name+" is not in the kitchen, do you want to call it? (Yes/No) ").lower()
            if pet_call =="yes": #call pet
                if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the kitchen now!")
                    pet1_room="kitchen" #Pet moves to kitchen
                    pet1_time_spent=pet1_time_spent+1
                    continue #Carry out the situation of pet in the kitchen
                else: #Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                    break #Proceed to the next action
            else: # do not call pet
                action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break #Proceed to the next action
    while number_option =="2": #The player owns 2 pets
        if pet1_room != "kitchen" and pet2_room != "kitchen": #0 pet in the kitchen
            pet_call=input("No pet is in the kitchen, who do you want to call? ("+pet1_name+"/"+pet2_name+"/Both) ")
            if pet_call==pet1_name: #Call pet 1
                if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the kitchen now!")
                    pet1_room="kitchen"
                    pet1_time_spent=pet1_time_spent+1
                    pet1_play=input("Do you want to pet or play with "+pet1_name+"? (Play/Pet) ").lower()
                    if pet1_play=="pet":
                        if pet1_type=="dog":
                            print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                        else:
                            print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                        happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                    elif pet1_play=="play":
                        if pet1_type=="dog":
                            print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                        else:
                            print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                        happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                        hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                    pet1_time_spent=pet1_time_spent+1
                    action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                else: #pet 1 Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    action_kitchen=input("None of the pets are here, which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break
            elif pet_call==pet2_name: #Call pet 2
                if happiness2_value>=20 and hunger2_value<90: # Call succeeded
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the kitchen now!")
                    pet2_room="kitchen"
                    pet2_time_spent=pet2_time_spent+1
                    pet2_play=input("Do you want to pet or play with "+pet2_name+"? (Play/Pet) ").lower()
                    if pet2_play=="pet":
                        if pet2_type=="dog":
                            print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                        else:
                            print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                        happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                    elif pet2_play=="play":
                        if pet2_type=="dog":
                            print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                        else:
                            print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                        happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                        hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                    pet2_time_spent=pet2_time_spent+1
                    action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                else: #pet 2 Call failed
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    action_kitchen=input("None of the pets are here, which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break
            else: #Call pet 1 and 2
                if happiness1_value>=20 and hunger1_value<90 and happiness2_value>=20 and hunger2_value<90:# 2 pets Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the kitchen now!")
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the kitchen now!")
                    pet1_room="kitchen"
                    pet2_room="kitchen" 
                    pet1_time_spent=pet1_time_spent+1
                    pet2_time_spent=pet2_time_spent+1
                    continue #Carry out the situation of 2 pets in the kitchen
                elif (happiness1_value>=20 and hunger1_value<90) or (happiness2_value>=20 and hunger2_value<90):# 1 pet Call succeeded
                    if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                        print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the kitchen now!")
                        print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                        pet1_room="kitchen"
                        pet1_time_spent=pet1_time_spent+1
                        pet1_play=input("Do you want to pet or play with "+pet1_name+"? (Play/Pet) ").lower()
                        if pet1_play=="pet":
                            if pet1_type=="dog":
                                print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                            else:
                                print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                            happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                        elif pet1_play=="play":
                            if pet1_type=="dog":
                                print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                            else:
                                print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                            happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                            hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                        pet1_time_spent=pet1_time_spent+1
                    else: # pet2 Call succeeded
                        print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                        print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the kitchen now!")
                        pet2_room="kitchen"
                        pet2_time_spent=pet2_time_spent+1
                        pet2_play=input("Do you want to pet or play with "+pet2_name+"? (Play/Pet) ").lower()
                        if pet2_play=="pet":
                            if pet2_type=="dog":
                                print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                            else:
                                print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                            happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                        elif pet2_play=="play":
                            if pet2_type=="dog":
                                print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                            else:
                                print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                            happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                            hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                        pet2_time_spent=pet2_time_spent+1
                    action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                else: # no pet Call succeeded
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    action_kitchen=input("None of the pets are here, which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break
        elif pet1_room == "kitchen" and pet2_room == "kitchen": #2 pets in the kitchen
            pet_play=input("Both "+pet1_name+" and "+pet2_name+" are in the kitchen! Do you want to pet or play with them? (Pet/Play) ").lower()
            if pet_play=="pet": #pet with 2 pets
                pet_choice=input(name+", your choice is "+pet_play+", who do you want to interact with? ("+pet1_name+"/"+pet2_name+"/Both) ")
                if pet_choice == pet1_name or pet_choice.lower()=="both": #pet with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                    pet1_time_spent=pet1_time_spent+1
                if pet_choice == pet2_name or pet_choice.lower()=="both": #pet with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                    pet2_time_spent=pet2_time_spent+1
            else: #play with 2 pets
                pet_choice=input(name+", your choice is "+pet_play+", who do you want to interact with? ("+pet1_name+"/"+pet2_name+"/Both) ")
                if pet_choice == pet1_name or pet_choice.lower()=="both": #play with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                    hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                    pet1_time_spent=pet1_time_spent+1
                if pet_choice == pet2_name or pet_choice.lower()=="both": #play with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                    hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                    pet2_time_spent=pet2_time_spent+1
            action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
            break
        else: #1 pet in the kitchen
            if pet1_room == "kitchen": # pet1 in the kitchen
                pet1_cpp=input(name+", do you want to call "+pet2_name+", or pet or play with "+pet1_name+"? (Call/Play/Pet) ").lower() #Choose an action with pet1
                if pet1_cpp=="call": #call pet2
                    if happiness2_value>=20 and hunger2_value<90: # pet2 Call succeeded
                        print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the kitchen now!")
                        pet2_room="kitchen"
                        pet2_time_spent=pet2_time_spent+1
                        continue #Carry out the situation of 2 pets in the kitchen
                    else: # pet2 Call failed
                        print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                        pet1_play=input("Do you want to pet or play with "+pet1_name+"? (Play/Pet) ").lower()
                        if pet1_play=="pet":
                            if pet1_type=="dog":
                                print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                            else:
                                print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                            happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                        elif pet1_play=="play":
                            if pet1_type=="dog":
                                print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                            else:
                                print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                            happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                            hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                        pet1_time_spent=pet1_time_spent+1
                elif pet1_cpp=="play": #play with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness1_value=happiness1_value+13.21 #Increase the pet's happiness
                    hunger1_value=hunger1_value+10.90 #Increase the pet's hunger
                    pet1_time_spent=pet1_time_spent+1
                else: #pet with pet1
                    if pet1_type=="dog":
                        print(pet1_happy_sound+", "+pet1_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet1_happy_sound+", "+pet1_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness1_value=happiness1_value+9.26 #Increase the pet's happiness
                    pet1_time_spent=pet1_time_spent+1
                action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break
            else: # pet2 in the kitchen
                pet2_cpp=input(name+", do you want to call "+pet1_name+", or pet or play with "+pet2_name+"? (Call/Play/Pet) ").lower() #Choose an action with pet2
                if pet2_cpp=="call": #call pet1
                    if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                        print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the kitchen now!")
                        pet1_room="kitchen"
                        pet1_time_spent=pet1_time_spent+1
                        continue #Carry out the situation of 2 pets in the kitchen
                    else: # pet1 Call failed
                        print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                        pet2_play=input("Do you want to pet or play with "+pet2_name+"? (Play/Pet) ").lower()
                        if pet2_play=="pet":
                            if pet2_type=="dog":
                                print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                            else:
                                print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                            happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                        elif pet2_play=="play":
                            if pet2_type=="dog":
                                print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                            else:
                                print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                            happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                            hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                elif pet2_cpp=="play": #play with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is chasing after that ball! It's so excited it almost knocked over the table!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves pouncing at that cat wand! Such a predator!")
                    happiness2_value=happiness2_value+13.21 #Increase the pet's happiness
                    hunger2_value=hunger2_value+10.90 #Increase the pet's hunger
                else: #pet with pet2
                    if pet2_type=="dog":
                        print(pet2_happy_sound+", "+pet2_name+" is really enjoying that rub in the tummy!!")
                    else:
                        print(pet2_happy_sound+", "+pet2_name+" loves that good scratch under the chin, it is purring so loud! Such a purr machine!!")
                    happiness2_value=happiness2_value+9.26 #Increase the pet's happiness
                pet2_time_spent=pet2_time_spent+1
                action_kitchen=input(name+", which one of the following actions would you like to perform next? (Prepare/Leave) ").lower()
                break
if action_kitchen=="prepare": #The player prepares the pet food
    if pet_food==False: #player did not find the pet food in the previous room
        print("You forgot to find where the pet food is, so there appears to be nothing you can prepare. Let's leave.")
    else: #player find the pet food in the previous room
        pet_food_prepare=input("With the pet food in front of you, how would you like to prepare it? (Methodical/Chaotic) ").lower()
        if pet_food_prepare=="methodical": #methodical preparation
            if pet_food=="lavish": #lavish food
                pet_food_water=float(input("Enter the amount of water: "))
                pet_food_dry=float(input("Enter the amount of dry food: "))
                x=0 #number of cups
                y=0 #number of spoons
                while x*15<pet_food_water: #Added water to the bowl
                    x=x+1
                    print("Added "+str(x)+" cups to the bowl")
                while y*7<pet_food_dry: #Added dry food to the bowl
                    y=y+1
                    print("Added "+str(y)+" spoons to the bowl")
                absolute_difference=round(abs(pet_food_water-pet_food_dry))
                print("You carefully spend 1 hour making the perfect meal. The end result looks like something edible for humans.")
            else: #simple food
                print("You carefully spend 1 hour making the perfect meal. The end result looks like something edible for humans.")
        else: #chaotic preparation
            if pet_food=="lavish": #lavish food
                print("The complex design of the original receipe meant that in such a haphazard preparation ruined the taste and texture.")
            else: #simple food
                print("The blender blends the simple pet food into a paste that looks a bit better than what you started with.")
        if number_option =="1": #The player owns 1 pet
            if pet1_room!="kitchen":
                pet1_room="kitchen"
                print(pet1_happy_sound+", "+pet1_name+" heard you preparing the food, it dashed into the kitchen!")
            pet_choice=input("You look at the prepared food in your hands. What do you feel like doing now? (Feed/Leave) ").lower()
            if pet_choice=="feed": #choose feed pet
                if hunger1_value==0: 
                    print(pet1_name+" is already full, you don't need to feed it.")
                else: 
                    pet_feed=1 #feed pet
                    pet1_time_spent=pet1_time_spent+1
                    if pet_food=="lavish" and pet_food_prepare=="methodical": # Methodically preparing lavish pet food
                        if absolute_difference==0: # the difference is 0
                            happiness1_value=happiness1_value+20
                            hunger1_value=hunger1_value-20
                        elif absolute_difference>0 and absolute_difference<15: # absolute difference is not 0 but is less than 15
                            if pet_food_water>pet_food_dry: # there is more water than dry food
                                happiness1_value=happiness1_value+20
                                hunger1_value=hunger1_value-10
                            else: # there is more dry food than water
                                happiness1_value=happiness1_value+10
                                hunger1_value=hunger1_value-20
                        else: #absolute difference is more than or equal 15
                            if absolute_difference%2==1: # the absolute difference is an odd number
                                happiness1_value=happiness1_value-20
                                hunger1_value=hunger1_value+20
                            else: # the absolute difference is even
                                happiness1_value=happiness1_value-15
                                hunger1_value=hunger1_value-10
                    else: #lavish pet food prepared chaotically and simple food
                        feed_amount=20 # initial amount grams of food
                        hunger1_value=hunger1_value-10 # initial hunger1_value
                        while feed_amount<100 and hunger1_value>0: 
                            print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                            feed_amount=feed_amount+20
                            hunger1_value=hunger1_value-10
                        if hunger1_value<=0: #print the last statement as hunger1_value<=0
                            hunger1_value=0
                            print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                            print(pet1_happy_sound+", "+pet1_name+" is satiated from the feast!")
                            if feed_amount==100:
                                print("There's no more prepared food left!")
                        elif feed_amount==100: #print the last statement as feed_amount==100
                            print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                            print("There's no more prepared food left!")
                        if pet_food=="lavish" and pet_food_prepare=="chaotic": #lavish pet food prepared chaotically
                            happiness1_value=happiness1_value-10
                if pet_feed>0 : #feed pet successful
                    print("The "+pet1_type+" finished the feast, and you leave the kitchen.")
                else: # do not feed pet
                    print("Okay, no feeding is needed, you go to the living room.")
            else: # Leave kitchen
                print("Forget about the prepared pet food, let's leave the kitchen.")
        else : #The player owns 2 pets
            if pet1_room!="kitchen":
                pet1_room="kitchen"
                print(pet1_happy_sound+", "+pet1_name+" heard you preparing the food, it dashed into the kitchen!")
            if pet2_room!="kitchen":
                pet2_room="kitchen"
                print(pet2_happy_sound+", "+pet2_name+" heard you preparing the food, it dashed into the kitchen!")
            pet_choice=input("You look at the prepared food in your hands. What do you feel like doing now? (Feed/Leave) ").lower()
            pet_feed_order_final=0
            if pet_choice=="feed": #feed pet
                pet_feed_order=input("Which pet do you want to feed? ("+pet1_name+"/"+pet2_name+") ")
                if pet_feed_order==pet1_name: #feed pet1
                    if hunger1_value==0: # pet1 is already full
                        print(pet1_name+" is already full, you don't need to feed it.")
                        feed_another_pet=input("Would you like to feed "+pet2_name+" instead? (Yes/No) ").lower()
                        if feed_another_pet=="yes": 
                            if hunger2_value==0: # pet2 is already full
                                print(pet2_name+" is already full, you don't need to feed it.")
                                print("Okay, no feeding is needed, you go to the living room.")
                            else: #feed pet2
                                pet_feed=2 #feed pet2
                                pet2_time_spent=pet2_time_spent+1
                                pet_feed_order_final=pet2_name
                        else : #do not want to feed another pet
                            print("Okay, no feeding is needed, you go to the living room.")
                    else: 
                        pet_feed=1 # feed pet1
                        pet1_time_spent=pet1_time_spent+1
                        pet_feed_order_final=pet1_name
                else: #feed pet2
                    if hunger2_value==0: # pet2 is already full
                        print(pet2_name+" is already full, you don't need to feed it.")
                        feed_another_pet=input("Would you like to feed "+pet1_name+" instead? (Yes/No) ").lower()
                        if feed_another_pet=="yes": 
                            if hunger1_value==0: # pet1 is already full
                                print(pet1_name+" is already full, you don't need to feed it.")
                                print("Okay, no feeding is needed, you go to the living room.")
                            else: 
                                pet_feed=1 #feed pet1
                                pet1_time_spent=pet1_time_spent+1
                                pet_feed_order_final=pet1_name
                        else : #do not want to feed another pet. choose No
                            print("Okay, no feeding is needed, you go to the living room.")
                    else: # feed pet2
                        pet_feed=2
                        pet2_time_spent=pet2_time_spent+1
                        pet_feed_order_final=pet2_name
            else: # Leave kitchen
                print("Forget about the prepared pet food, let's leave the kitchen.")
            if pet_feed_order_final==pet1_name:
                if pet_food=="lavish" and pet_food_prepare=="methodical": # Methodically preparing lavish pet food
                    if absolute_difference==0: # the difference is 0
                        happiness1_value=happiness1_value+20
                        hunger1_value=hunger1_value-20
                    elif absolute_difference>0 and absolute_difference<15: # absolute difference is not 0 but is less than 15
                        if pet_food_water>pet_food_dry: # there is more water than dry food
                            happiness1_value=happiness1_value+20
                            hunger1_value=hunger1_value-10
                        else: # there is more dry food than water
                            happiness1_value=happiness1_value+10
                            hunger1_value=hunger1_value-20
                    else: #absolute difference is more than or equal 15
                        if absolute_difference%2==1: # the absolute difference is an odd number
                            happiness1_value=happiness1_value-20
                            hunger1_value=hunger1_value+20
                        else: # the absolute difference is even
                            happiness1_value=happiness1_value-15
                            hunger1_value=hunger1_value-10
                else: #lavish pet food prepared chaotically and simple food
                    feed_amount=20 # initial amount grams of food
                    hunger1_value=hunger1_value-10 # initial hunger1_value
                    while feed_amount<100 and hunger1_value>0: 
                        print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                        feed_amount=feed_amount+20
                        hunger1_value=hunger1_value-10
                    if hunger1_value<=0: #print the last statement as hunger1_value<=0
                        hunger1_value=0
                        print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                        print(pet1_happy_sound+", "+pet1_name+" is satiated from the feast!")
                        if feed_amount==100:
                            print("There's no more prepared food left!")
                    elif feed_amount==100: #print the last statement as feed_amount==100
                        print("You fed "+pet1_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger1_value,".2f")+"% hungry.")
                        print("There's no more prepared food left!")
                    if pet_food=="lavish" and pet_food_prepare=="chaotic": #lavish pet food prepared chaotically
                        happiness1_value=happiness1_value-10
                print("The "+pet1_type+" finished the feast, and you leave the kitchen.")
            elif pet_feed_order_final==pet2_name:
                if pet_food=="lavish" and pet_food_prepare=="methodical": # Methodically preparing lavish pet food
                    if absolute_difference==0: # the difference is 0
                        happiness2_value=happiness2_value+20
                        hunger2_value=hunger2_value-20
                    elif absolute_difference>0 and absolute_difference<15: # absolute difference is not 0 but is less than 15
                        if pet_food_water>pet_food_dry: # there is more water than dry food
                            happiness2_value=happiness2_value+20
                            hunger2_value=hunger2_value-10
                        else: # there is more dry food than water
                            happiness2_value=happiness2_value+10
                            hunger2_value=hunger2_value-20
                    else: #absolute difference is more than or equal 15
                        if absolute_difference%2==1: # the absolute difference is an odd number
                            happiness2_value=happiness2_value-20
                            hunger2_value=hunger2_value+20
                        else: # the absolute difference is even
                            happiness2_value=happiness2_value-15
                            hunger2_value=hunger2_value-10
                else: #lavish pet food prepared chaotically and simple food
                    feed_amount=20 # initial amount grams of food
                    hunger2_value=hunger2_value-10 # initial hunger2_value
                    while feed_amount<100 and hunger2_value>0: 
                        print("You fed "+pet2_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger2_value,".2f")+"% hungry.")
                        feed_amount=feed_amount+20
                        hunger2_value=hunger2_value-10
                    if hunger2_value<=0: #print the last statement as hunger2_value<=0
                        hunger2_value=0
                        print("You fed "+pet2_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger2_value,".2f")+"% hungry.")
                        print(pet2_happy_sound+", "+pet2_name+" is satiated from the feast!")
                        if feed_amount==100:
                            print("There's no more prepared food left!")
                    elif feed_amount==100: #print the last statement as feed_amount==100
                        print("You fed "+pet2_name+" "+str(feed_amount)+" grams of food, it is now "+format(hunger2_value,".2f")+"% hungry.")
                        print("There's no more prepared food left!")
                    if pet_food=="lavish" and pet_food_prepare=="chaotic": #lavish pet food prepared chaotically
                        happiness2_value=happiness2_value-10
                print("The "+pet2_type+" finished the feast, and you leave the kitchen.")
if action_kitchen=="leave": #The player leaves the kitchen
    print("Alright, lets go back to the living room immediately!")

#Game Status
print(STATUS_BANNER)
print(name+", here is a summary of the current status of your pets:")
if happiness1_value>100: #for one pet limit happiness1_value
    happiness1_value=100.00
elif happiness1_value<0:
    happiness1_value=0.00
if hunger1_value>100: #for one pet limit happiness1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
print("Your little "+pet1_type+", "+pet1_name+", is in the "+pet1_room+" and is "+format(happiness1_value,".2f")+"% happy and "+format(hunger1_value,".2f")+"% hungry.")
if number_option == "2": #The status of choosing two animals
    if happiness2_value>100: #for pet2 limit happiness2_value
        happiness2_value=100.00
    elif happiness2_value<0:
        happiness2_value=0.00
    if hunger2_value>100: #for pet2 limit happiness2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    print("Your little "+pet2_type+", "+pet2_name+", is in the "+pet2_room+" and is "+format(happiness2_value,".2f")+"% happy and "+format(hunger2_value,".2f")+"% hungry.")

# In the Living Room (again)
print(LIVING_ROOM_BANNER)
if pet_feed==1 and happiness1_value>60 and hunger1_value<50: #have fed pet
    pet1_room="living room"
if pet1_room=="living room":
    print(pet1_happy_sound+", "+pet1_name+" is in the living room!")
if number_option == "2": #The situation of two pets
    if pet_feed==2 and happiness2_value>60 and hunger2_value<50: #have fed pet
        pet2_room="living room"
    if pet2_room=="living room":
        print(pet2_happy_sound+", "+pet2_name+" is in the living room!")
# actions in living room
while number_option == "1": #The situation of a pet. There are two interactions when pets move from other places to the living room
    if pet1_room == "living room":#Pet in the living room
        action_living_again=input("What would you like to do now? (Goodbye/Cage/Leave) ").lower()
        if action_living_again=="goodbye": # Say goodbye to the pet
            print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
            happiness1_value=happiness1_value+10 #Increase the pet's happiness
            pet1_time_spent=pet1_time_spent+1
        elif action_living_again=="cage": # place the pet in a cage.
            print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
            happiness1_value=happiness1_value-20 #decrease the pet's happiness
        print("Okie, lets finish this game!")
        break #Proceed to the next action
    elif pet1_room != "living room":#Pet not in the living room
        pet_call=input(pet1_name+" is not in the living room, do you want to call it? (Yes/No) ").lower()
        if pet_call =="yes": #call pet
            if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                pet1_room="living room" #Pet moves to living room
                pet1_time_spent=pet1_time_spent+1
                continue #Carry out the situation of pet in the living room
            else: #Call failed
                print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                print("Well, I guess you can leave then.")
                break #Proceed to the next action
        else: # do not call pet
            print("Well, I guess you can leave then.")
            break #Proceed to the next action
while number_option == "2": #The situation of two pets
    if pet1_room != "living room" and pet2_room != "living room": #0 pet in the living room
        pet_choice=input("No pets are in the living room :(. Would you like to Call or Leave? (Call/Leave) ").lower()
        if pet_choice=="call": 
            pet_call=input("Who are we calling? ("+pet1_name+"/"+pet2_name+"/Both) ") 
            if pet_call==pet1_name: #Call pet 1
                if happiness1_value>=20 and hunger1_value<90: # Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    pet1_room="living room"
                    pet1_time_spent=pet1_time_spent+1
                    action_living_again=input("Do you want to say goodbye to "+pet1_name+" or put it in the cage? (Goodbye/Cage/Leave) ").lower()
                    if action_living_again=="goodbye": # Say goodbye to the pet
                        print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
                        happiness1_value=happiness1_value+10 #Increase the pet's happiness
                        pet1_time_spent=pet1_time_spent+1
                    elif action_living_again=="cage": # place the pet in a cage.
                        print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
                        happiness1_value=happiness1_value-20 #decrease the pet's happiness
                    print("Okie, lets finish this game!")
                else: #Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    print("None of the pets are here, lets finish this game!")
            elif pet_call==pet2_name: #Call pet 2    
                if happiness2_value>=20 and hunger2_value<90: # Call succeeded
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                    pet2_room="living room" 
                    pet2_time_spent=pet2_time_spent+1
                    action_living_again=input("Do you want to say goodbye to "+pet2_name+" or put it in the cage? (Goodbye/Cage/Leave) ").lower()
                    if action_living_again=="goodbye": # Say goodbye to the pet
                        print("You gently pat "+pet2_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet2_name+' replies: "'+pet2_happy_sound+'"!')
                        happiness2_value=happiness2_value+10 #Increase the pet's happiness
                        pet2_time_spent=pet2_time_spent+1
                    elif action_living_again=="cage": # place the pet in a cage.
                        print("You put "+pet2_name+' in its cage, who "'+pet2_angry_sound+'" in protest.')
                        happiness2_value=happiness2_value-20 #decrease the pet's happiness
                    print("Okie, lets finish this game!")
                else: #Call failed
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    print("None of the pets are here, lets finish this game!")
            else: #Call pet 1 and 2
                if happiness1_value>=20 and hunger1_value<90 and happiness2_value>=20 and hunger2_value<90:# 2 pets Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                    pet1_room="living room"
                    pet2_room="living room" 
                    pet1_time_spent=pet1_time_spent+1
                    pet2_time_spent=pet2_time_spent+1
                    continue #Carry out the situation of 2 pets in the living room
                elif (happiness1_value>=20 and hunger1_value<90) or (happiness2_value>=20 and hunger2_value<90):# 1 pet Call succeeded
                    if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                        print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                        print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                        pet1_room="living room"
                        pet1_time_spent=pet1_time_spent+1
                        action_living_again=input("Do you want to say goodbye to "+pet1_name+" or put it in the cage? (Goodbye/Cage/Leave) ").lower()
                        if action_living_again=="goodbye": # Say goodbye to the pet
                            print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
                            happiness1_value=happiness1_value+10 #Increase the pet's happiness
                            pet1_time_spent=pet1_time_spent+1
                        elif action_living_again=="cage": # place the pet in a cage.
                            print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
                            happiness1_value=happiness1_value-20 #decrease the pet's happiness
                        print("Okie, lets finish this game!") #all of them print this statement
                    else: # pet2 Call succeeded
                        print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                        print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                        pet2_room="living room"
                        pet2_time_spent=pet2_time_spent+1
                        action_living_again=input("Do you want to say goodbye to "+pet2_name+" or put it in the cage? (Goodbye/Cage/Leave) ").lower()
                        if action_living_again=="goodbye": # Say goodbye to the pet
                            print("You gently pat "+pet2_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet2_name+' replies: "'+pet2_happy_sound+'"!')
                            happiness2_value=happiness2_value+10 #Increase the pet's happiness
                            pet2_time_spent=pet2_time_spent+1
                        elif action_living_again=="cage": # place the pet in a cage.
                            print("You put "+pet2_name+' in its cage, who "'+pet2_angry_sound+'" in protest.')
                            happiness2_value=happiness2_value-20 #decrease the pet's happiness
                        print("Okie, lets finish this game!") #all of them print this statement
                else: # no pets Call succeeded
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    print("None of the pets are here, lets finish this game!")
        else: #leave the living room
            print("None of the pets are here, lets finish this game!")
        break #Proceed to the next action   
    elif pet1_room == "living room" and pet2_room == "living room": #2 pets in the living room
        pet1_cpp=input("Both "+pet1_name+" and "+pet2_name+" are in the living room! Do you want to say goodbye, put them in the cage, or leave? (Goodbye/Cage/Leave) ").lower() #Choose an action with two pets
        if pet1_cpp=="goodbye": #Say goodbye to the two pets
            print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
            print("You gently pat "+pet2_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet2_name+' replies: "'+pet2_happy_sound+'"!')
            happiness1_value=happiness1_value+10 #Increase the pet's happiness
            happiness2_value=happiness2_value+10 #Increase the pet's happiness
            pet1_time_spent=pet1_time_spent+1
            pet2_time_spent=pet2_time_spent+1
            print("Okie, lets finish this game!") 
        elif pet1_cpp=="cage": # place the two pets in  cage.
            print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
            print("You put "+pet2_name+' in its cage, who "'+pet2_angry_sound+'" in protest.')
            happiness1_value=happiness1_value-20 #decrease the pet's happiness
            happiness2_value=happiness2_value-20 #decrease the pet's happiness
            print("Okie, lets finish this game!")
        else: # Leave
            print("Okie, lets finish this game!")
        break #Proceed to the next action 
    else :#1 pet in the living room
        if pet1_room == "living room": # pet1 in the living room
            pet1_cpp=input("What would you like to do now? (Call/Goodbye/Cage/Leave) ").lower() #Choose an action with pet1
            if pet1_cpp=="call": #call pet2
                if happiness2_value>=20 and hunger2_value<90: # pet2 Call succeeded
                    print(pet2_happy_sound+", "+pet2_name+" came from the "+pet2_room+", it is with you in the living room now!")
                    pet2_room="living room"
                    pet2_time_spent=pet2_time_spent+1
                    continue #Carry out the situation of 2 pets in the living room
                else: # pet2 Call failed
                    print(pet2_angry_sound+"! Oh no, "+pet2_name+" is a bit angry, it doesn't want to come!")
                    action_living_again=input("Do you want to say goodbye to "+pet1_name+", put it in the cage, or leave? (Goodbye/Cage/Leave) ").lower()
                    if action_living_again=="goodbye": # Say goodbye to the pet
                        print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
                        happiness1_value=happiness1_value+10 #Increase the pet's happiness
                        pet1_time_spent=pet1_time_spent+1
                    elif action_living_again=="cage": # place the pet in a cage.
                        print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
                        happiness1_value=happiness1_value-20 #decrease the pet's happiness
            elif pet1_cpp=="goodbye": # Say goodbye to the pet.
                print("You gently pat "+pet1_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet1_name+' replies: "'+pet1_happy_sound+'"!')
                happiness1_value=happiness1_value+10 #Increase the pet's happiness
                pet1_time_spent=pet1_time_spent+1
            elif pet1_cpp=="cage": # place the pet in a cage. 
                print("You put "+pet1_name+' in its cage, who "'+pet1_angry_sound+'" in protest.')
                happiness1_value=happiness1_value-20 #decrease the pet's happiness
            print("Okie, lets finish this game!") #all of them print this statement
            break #Proceed to the next action
        else: # pet2 in the living room
            pet1_cpp=input("What would you like to do now? (Call/Goodbye/Cage/Leave) ").lower() #Choose an action with pet2
            if pet1_cpp=="call": #call pet1
                if happiness1_value>=20 and hunger1_value<90: # pet1 Call succeeded
                    print(pet1_happy_sound+", "+pet1_name+" came from the "+pet1_room+", it is with you in the living room now!")
                    pet1_room="living room"
                    pet1_time_spent=pet1_time_spent+1
                    continue #Carry out the situation of 2 pets in the living room
                else: # pet1 Call failed
                    print(pet1_angry_sound+"! Oh no, "+pet1_name+" is a bit angry, it doesn't want to come!")
                    action_living_again=input("Do you want to say goodbye to "+pet2_name+", put it in the cage, or leave? (Goodbye/Cage/Leave) ").lower()
                    if action_living_again=="goodbye": # Say goodbye to the pet
                        print("You gently pat "+pet2_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet2_name+' replies: "'+pet2_happy_sound+'"!')
                        happiness2_value=happiness2_value+10 #Increase the pet's happiness
                        pet2_time_spent=pet2_time_spent+1
                    elif action_living_again=="cage": # place the pet in a cage.
                        print("You put "+pet2_name+' in its cage, who "'+pet2_angry_sound+'" in protest.')
                        happiness2_value=happiness2_value-20 #decrease the pet's happiness
            elif pet1_cpp=="goodbye": # Say goodbye to the pet.
                print("You gently pat "+pet2_name+"'s head and whispers 'see you soon, little one' in its ear, "+pet2_name+' replies: "'+pet2_happy_sound+'"!')
                happiness2_value=happiness2_value+10 #Increase the pet's happiness
                pet2_time_spent=pet2_time_spent+1
            elif pet1_cpp=="cage": # place the pet in a cage. 
                print("You put "+pet2_name+' in its cage, who "'+pet2_angry_sound+'" in protest.')
                happiness2_value=happiness2_value-20 #decrease the pet's happiness
            print("Okie, lets finish this game!") #all of them print this statement
            break #Proceed to the next action           

#Game Status
print(STATUS_BANNER)
print(name+", here is a summary of the current status of your pets:")
if happiness1_value>100: #for one pet limit happiness1_value
    happiness1_value=100.00
elif happiness1_value<0:
    happiness1_value=0.00
if hunger1_value>100: #for one pet limit happiness1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
print("Your little "+pet1_type+", "+pet1_name+", is in the "+pet1_room+" and is "+format(happiness1_value,".2f")+"% happy and "+format(hunger1_value,".2f")+"% hungry.")
if number_option == "2": #The status of choosing two animals
    if happiness2_value>100: #for pet2 limit happiness2_value
        happiness2_value=100.00
    elif happiness2_value<0:
        happiness2_value=0.00
    if hunger2_value>100: #for pet2 limit happiness2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    print("Your little "+pet2_type+", "+pet2_name+", is in the "+pet2_room+" and is "+format(happiness2_value,".2f")+"% happy and "+format(hunger2_value,".2f")+"% hungry.")

# Calculate the final game state
print(GARDEN_BANNER)
print("Good job "+name+", now we are in the garden, let's see how you are performing.")
if happiness1_value>100: #for one pet limit happiness1_value
    happiness1_value=100.00
elif happiness1_value<0:
    happiness1_value=0.00
if hunger1_value>100: #for one pet limit happiness1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
f_pet=happiness1_value+pet1_time_spent*1.2 # f(happiness level, time spent with pet)
if hunger1_value-50<0:
    g_pet=-1
elif hunger1_value-50>0:
    g_pet=1
else:
    g_pet=0
pet1_final_happiness_level=f_pet-g_pet*hunger1_value/10
if pet1_final_happiness_level>100:
    pet1_final_happiness_level=100
elif pet1_final_happiness_level<0:
    pet1_final_happiness_level=0
if number_option == "2": #The situation of two pets
    if happiness2_value>100: #for pet2 limit happiness2_value
        happiness2_value=100.00
    elif happiness2_value<0:
        happiness2_value=0.00
    if hunger2_value>100: #for pet2 limit happiness2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    f_pet2=happiness2_value+pet2_time_spent*1.2 # f(happiness level, time spent with pet)
    if hunger2_value-50<0:
        g_pet2=-1
    elif hunger2_value-50>0:
        g_pet2=1
    else:
        g_pet2=0
    pet2_final_happiness_level=f_pet2-g_pet2*hunger2_value/10
    if pet2_final_happiness_level>100:
        pet2_final_happiness_level=100
    elif pet2_final_happiness_level<0:
        pet2_final_happiness_level=0
#Game Status
print(STATUS_BANNER)
print(name+", here is a summary of the current status of your pets:")
if pet1_final_happiness_level>100: #for one pet limit pet1_final_happiness_level
    pet1_final_happiness_level=100.00
elif pet1_final_happiness_level<0:
    pet1_final_happiness_level=0.00
if hunger1_value>100: #for one pet limit hunger1_value
    hunger1_value=100.00
elif hunger1_value<0:
    hunger1_value=0.00
if hunger1_value>=90:
    pet1_room="kitchen"
print("Your little "+pet1_type+", "+pet1_name+", is in the "+pet1_room+" and is "+format(pet1_final_happiness_level,".2f")+"% happy and "+format(hunger1_value,".2f")+"% hungry.")
if number_option == "2": #The status of choosing two animals
    if pet2_final_happiness_level>100: #for pet2 limit pet2_final_happiness_level
        pet2_final_happiness_level=100.00
    elif pet2_final_happiness_level<0:
        pet2_final_happiness_level=0.00
    if hunger2_value>100: #for pet2 limit hunger2_value
        hunger2_value=100.00
    elif hunger2_value<0:
        hunger2_value=0.00
    if hunger2_value>=90:
        pet2_room="kitchen"
    print("Your little "+pet2_type+", "+pet2_name+", is in the "+pet2_room+" and is "+format(pet2_final_happiness_level,".2f")+"% happy and "+format(hunger2_value,".2f")+"% hungry.")

# End of the program
print(GAME_END_BANNER)
if number_option == "1": #The situation of a pet
    if pet1_final_happiness_level>=80 and hunger1_value<=20: #outcome was a success
        print("Congratulations! You did an amazing job looking after your pets! Hope to see you again soon!")
    else: #outcome was not a success
        print("Unfortunately! You didn't do a good job looking after your pets! Hopefully you will do better next time.")
elif number_option == "2": #The status of choosing two animals
    if pet1_final_happiness_level>=80 and hunger1_value<=20 and pet2_final_happiness_level>=80 and hunger2_value<=20: # outcome was a success
        print("Congratulations! You did an amazing job looking after your pets! Hope to see you again soon!")
    else: #outcome was not a success
        print("Unfortunately! You didn't do a good job looking after your pets! Hopefully you will do better next time.")
print("Bye "+name+"!")