lottery = {'userlotno':[],'word':['first','second','third','fourth'],'default': [6]}
rem = "yes"
for i in range(0,4): 
    number = int(input(f"Enter your Lottery No between 0 to 9 for {lottery['word'][i]} try :" ))
    if number>=0 and number<=9: 
        print("")
    elif rem == input("If you enter wrong no you will kick from ' LOTTERY GAME'\n Enter 'yes' if you want to continue: ").lower():
        print("Enter number no between 0 to 9")
        number = int(input(f"Enter your {lottery['word'][i]} Lottery No : " ))
    else:    
        print("You have kicked from 'LOTTERY GAME'")        
        break        
    lottery['userlotno'].append(number)
    if lottery['default'][0] == lottery['userlotno'][i]:
        print("Congralation your are winner")
        break
    elif i<2:
        print("you loose")
        print("You have ",2-i," more chance")
    else :
        
        print("you loose")
        print(" your last chance")              
print("user lottery no: ", lottery['userlotno'],sep=" ")

