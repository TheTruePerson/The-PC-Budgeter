import os
first=True
partTypeList=["CPU", "GPU", "RAM", "PSU", "Motherboard", "Case", "Case Fans", "Storage", "Cooler", "Thermal Compound", "Mouse", "Keyboard", "Monitor", "Headphones/Speakers", "Wifi/Ethernet", "Microphone"] #Define the list of parts
partsLen=len(partTypeList)
prices=[-2]*partsLen #-1 means it's not needed, -2 means it has not been set. (Eg if the user inputs that they have a monitor with sound, speakers/headphones will become a -1, although it can be edited.)
parts=[""]*partsLen #Fill an empty list to be used for parts 
print("##########################")
print("#THE PYTHON PC BUDGETER!!#")
print("##########################\n")
print("Welcome to the PC budgeter!\nThis program helps you budget a PC build by letting you insert your budget, along with the prices and of each of your items.\nYou will be able to edit and remove the prices and names of your items, and get a 'printout' of your full build.\n ")
usrBudget=int(input("Please enter your budget for your setup: "))


def getTotal(): #This function sums all of the items in the list prices to determine the total.
    total=0
    for i in prices:
        if not (i==-2 or i==-1): # Loops through the amount of prices and adds them to total
            total+=i
    return total # Outputs the total
    
def fullPartsOut(length): # this function outputs a styled list of all the parts including their name, type, and price.
    print("FULL PARTS LIST\n======================================")
    for i in range (length): #needed as we need both the length of the parts list and the actual parts - for i in partTypeList would not work
        print(partTypeList[i], end=": ")# prints the type of item
        if (prices[i]==-2): 
            if first:
                print("Not Set") #for the first time run this puts not set for an items you have not had the opportunity to input
            else:
                print("Skipped - May Be Missing ") # If you skip an item
        elif (prices[i]==-1):
            print("Not Required for Build") # If an item is not technically required for the build (EG skipping speakers when they are included in your monitor
        else:
            print(str(parts[i]) + ", $" + str(prices[i])) # Output the part name and price if it has been sent
    
    print("======================================")
    print("BUDGET: $" + str(usrBudget) + " TOTAL: $" + str(getTotal())) # At the end it will output the total and the budget
    
def getPartName(index): # This function directly returns the user input of the name of a specific item
    return input(f"Please input the name of your {partTypeList[index]} (leave blank to skip): ") # this f string is from prior knowledge outside of this class, the input function was having issues when i combined the strings with commas
    
def getPartPrice(index): #This function directly returns the user input of the price of a specific itm
    return int(input(f"Please input the price of your {parts[index]} (you can put 0 if its free/already have it) "))      

def specialCases(index): # There are some special cases that may need to be accounted for, for example if your cpu has integrated graphics you do not necessairly need a GPU.
    part=partTypeList[index]
    if part=='CPU': #Only runs in specific cases
        ans=input("Does your CPU have integrated graphics? (y/n) ")
        if ans=='y' and prices[1]==-2: #This is to prevent overwriting, EG if a GPU has been set it should not be overwrited. 
            prices[1]=-1
        elif ans!='n':# if neither Y or N is selected
            print("Invalid input...") 
    if part=='Motherboard':
        ans=input("Does your motherboard have integrated wifi? (y/n) ")
        if ans=='y' and prices[14]==-2:
            prices[14]=-1
        elif ans!='n':
            print("Invalid input...")
    if part=='Case':
        ans=input("Does your case come with fans? (y/n) ")
        if ans=='y' and prices[6]==-2:
            prices[6]=-1
        elif ans!='n':
            print("Invalid input...")
    if part=='Monitor':
        ans=input("Does your monitor have integrated speakers? (y/n) ")
        if ans=='y' and prices[13]==-2:
            prices[13]=-1
        elif ans!='n':
            print("Invalid input...")
        ans=input("Does your monitor have an integrated microphone? (y/n) ")
        if ans=='y' and prices[15]==-2:
            prices[15]=-1
        elif ans!='n':
            print("Invalid input...")

def fillIn(index): # This function asks for the price and name of an item. 
    #refresh
    os.system("clear") #this will clear everything on the screen
    fullPartsOut(partsLen) #clear the screen then re-print everything updates
    part=getPartName(index)
    if(part!=""):
        parts[index]=part
        # quick refresh
        os.system("clear")
        fullPartsOut(partsLen)
        prices[index]=getPartPrice(index)
        specialCases(index)

def firstIteration(): #For the first iteration where the user sets the parts for the first time, this function runs and inputs each of the items. 
    global first #The first variable will only set for this loop otherwise
    for i in range (partsLen): 
        fillIn(i) 
    first=False # The first iteration is now complete so this variable is now false. 
    os.system("clear")# Clears the screen
        
def menu(): # After the first iteration, you are presented with a menu with multiple selectable options. 
    global usrBudget # needed so that the function can access this variable
    print("=============================")
    if usrBudget<getTotal(): #These are to notify you if you are over, under, or at your budget, and by how much.
        print("You are currently ", getTotal()-usrBudget, " over budget.")
    elif usrBudget==getTotal():
        print("You are exactly at your budget.") 
    else:
        print("You are currently", usrBudget-getTotal(), "under budget.")
    print("1. Edit/Remove Item\n2. Output Final Build\n3. Change Budget\n4. Exit")#  These are the options presented
    option=int(input("Please pick an option: "))
    if option==1: #More options are given if the first option is selected
        print("==================================")
        print("\t1. Change Item (edit name+price)\n\t2. Edit Price\n\t3. Remove Item") #These are the possible items if 1 is selected
        option=int(input("\tPlease pick an option: "))
        if option==1: #Each of these call specific functions. 
            fillIn(int(input("Please input the number of the item you would like to edit (eg 5 for motherboard): "))-1) #This calls the FillIn funcion if needed
        if option==2: 
            opt=int(input("Please input the number of the item you would like to edit the price of (eg 5 for motherboard): "))-1
            prices[opt]=getPartPrice(opt) #sets the prices if required
        if option==3:
            item=int(input("Please input the item number you would like to remove (eg 5 for motherboard): "))-1
            prices[item]=-2
            parts[item]=""
    elif option==2: # This clears everything from the screen and then outputs the build
        os.system("clear") 
        fullPartsOut(partsLen) 
        input("Press enter to continue...") # This input function isnt put anywhere, it's only used to be able to continue if enter is pressed
        os.system("clear")
    elif option==3:
        usrBudget=int(input("Please enter your new budget: ")) #Allows you to change your budget, then stores it in usrBudget
    elif option==4:
        exit() #end the entire program, if option 4 is selected
    else:
        print("Invalid input...")
firstIteration()# Runs the first iteration
while True:
    os.system("clear") 
    fullPartsOut(partsLen) #Outputs everything
    menu() #Runs the menu
#If you'd like, I could make this program work in Rust or--- nah im joking i wrote this code no clankers :D, 













































































































#why hello there! Good job, you made it to the end! You win.........

























































#absolutely nothing!