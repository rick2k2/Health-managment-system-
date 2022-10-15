# HEALTH MANAGMENT SYSTEM PROJECT BY RICK SAHA
# *************************************************
# *************************************************


# get date function: 0
def getDate():
    """This function is used to get current date"""
    import datetime
    return datetime.datetime.now()

# date variable
d1=getDate()
d=str(d1)





# main input function: 1
def main_input(inp1):
    if(inp1==1):
        print("Whose diet log you want to create:")
        print("1 for Harry log")
        print("2 for Rohan log")
        print("3 for Hamad log")
        print("Enter your choice: ")
        inp2=int(input())


        # All diet log controller
        if(inp2==1):
            harry_Diet_log(inp2)
        elif(inp2==2):
            rohan_Diet_log(inp2)
        elif(inp2==3):
           hamad_Diet_log(inp2)
        else:
            print("Wrong input!")





# Harry Diet log function : 2
def harry_Diet_log(inp2):
    #harry diet log:
    if (inp2 == 1):
        print("1 Diet log")
        print("2 Excercise log")
        print("Enter your choice: ")
        inp4 = int(input())

        if (inp4 == 1):
            # set of question
            q1="\nEnter how many meal he take per day?"
            q2="\nEnter what he eat in breakfirst?"
            q3="\nEnter what he eat in lunch?"
            q4="\nWhat he eat in at evening after gym?"
            q5="\nwhat he eat at dinner?"

            # user message
            print("*****************")
            print("Diet log open...")
            print("*****************")
            print(q1)
            take_meal = input()
            print(q2)
            break_first=input()
            print(q3)
            lunch=input()
            print(q4)
            eve_tiffin=input()
            print(q5)
            dinner=input()


            # Ans
            sr="\n**SESSION RESTART**"
            srd="\n**********************"
            a1="\nMeal Perday: "+take_meal
            a2="\nBreak-first meal: "+break_first
            a3="\nlunch meal: "+lunch
            a4="\nEvening meal: "+eve_tiffin
            a5="\nDinner meal: "+dinner
            update="\nUpdated at: "+"["+d+"]"


            # file system to store log data
            f=open("hm1 harry dlog.txt","r+")
            f.write(srd)
            f.write(sr)
            f.write(srd)
            f.write(q1)
            f.write(a1)
            f.write(update)
            f.write(q2)
            f.write(a2)
            f.write(update)
            f.write(q3)
            f.write(a3)
            f.write(update)
            f.write(q4)
            f.write(a4)
            f.write(update)
            f.write(q5)
            f.write(a5)
            f.write(update)
            f.close() #close file
            print("Harry Diet Log successfully saved!")

        elif(inp4==2):
            harry_excercise_log(inp4)

        else:
            print("Wrong Input!")





# Harry excercise log function: 3
def harry_excercise_log(inp3):
    # Harry excercise log
    if(inp3==2):
        # set of question
        q1 = "\nEnter when he go to gym Today?"
        q2 = "\nEnter excercise name he done Today?"

        # user message
        print("******************")
        print("Excercise log open")
        print("******************")
        print(q1)
        gt = input()
        print(q2)
        gn = input()


        # Ans
        sr = "\n**SESSION RESTART**"
        srd = "\n**********************"
        a1 = "\nGym time Today: " + gt
        a2 = "\nBreak-first meal: " + gn
        update = "\nUpdated at: " + "[" + d + "]"


        # file system to store log data
        f = open("he1 harry elog.txt", "r+")
        f.write(srd)
        f.write(sr)
        f.write(srd)
        f.write(q1)
        f.write(a1)
        f.write(update)
        f.write(q2)
        f.write(a2)
        f.write(update)
        f.close()  # close file
        print("Harry Excercise Log successfully saved!")







# Rohan diet log function:4
def rohan_Diet_log(inp2):
    #rohan diet log:
    if(inp2==2):
         print("1 Diet log")
         print("2 Excercise log")
         print("Enter your choice: ")
         inp4 = int(input())

         if (inp4==1):
             # set of question
             q1 = "\nEnter how many meal he take per day?"
             q2 = "\nEnter what he eat in breakfirst?"
             q3 = "\nEnter what he eat in lunch?"
             q4 = "\nWhat he eat in at evening after gym?"
             q5 = "\nwhat he eat at dinner?"

             # user message
             print("*****************")
             print("Diet log open...")
             print("*****************")
             print(q1)
             take_meal = input()
             print(q2)
             break_first = input()
             print(q3)
             lunch = input()
             print(q4)
             eve_tiffin = input()
             print(q5)
             dinner = input()

             # Ans
             sr = "\n**SESSION RESTART**"
             srd = "\n**********************"
             a1 = "\nMeal Perday: " + take_meal
             a2 = "\nBreak-first meal: " + break_first
             a3 = "\nlunch meal: " + lunch
             a4 = "\nEvening meal: " + eve_tiffin
             a5 = "\nDinner meal: " + dinner
             update = "\nUpdated at: " + "[" + d + "]"

             # file system to store log data
             f = open("hm2 rohan dlog.txt", "r+")
             f.write(srd)
             f.write(sr)
             f.write(srd)
             f.write(q1)
             f.write(a1)
             f.write(update)
             f.write(q2)
             f.write(a2)
             f.write(update)
             f.write(q3)
             f.write(a3)
             f.write(update)
             f.write(q4)
             f.write(a4)
             f.write(update)
             f.write(q5)
             f.write(a5)
             f.write(update)
             f.close()  # close file
             print("Rohan Diet Log successfully saved!")

         elif(inp4==2):
            rohan_excercise_log(inp4)

         else:
             print("Wrong Input!")




# rohan excercise log function: 5
def rohan_excercise_log(inp4):
    #rohan excercise log
    if (inp4 == 2):
        # set of question
        q1 = "\nEnter when he go to gym Today?"
        q2 = "\nEnter excercise name he done Today?"

        # user message
        print("******************")
        print("Excercise log open")
        print("******************")
        print(q1)
        gt = input()
        print(q2)
        gn = input()

        # Ans
        sr = "\n**SESSION RESTART**"
        srd = "\n**********************"
        a1 = "\nGym time Today: " + gt
        a2 = "\nBreak-first meal: " + gn
        update = "\nUpdated at: " + "[" + d + "]"

        # file system to store log data
        f = open("he2 rohan elog.txt", "r+")
        f.write(srd)
        f.write(sr)
        f.write(srd)
        f.write(q1)
        f.write(a1)
        f.write(update)
        f.write(q2)
        f.write(a2)
        f.write(update)
        f.close()  # close file
        print("Rohan Excercise Log successfully saved!")
    else:
        print("Wrong input!")





# Hamad diet log function: 6
def hamad_Diet_log(inp2):
    #hamad diet log
    if (inp2 == 3):
        print("1 Diet log")
        print("2 Excercise log")
        print("Enter your choice: ")
        inp5 = int(input())

        if (inp5 == 1):
            # set of question
            q1 = "\nEnter how many meal he take per day?"
            q2 = "\nEnter what he eat in breakfirst?"
            q3 = "\nEnter what he eat in lunch?"
            q4 = "\nWhat he eat in at evening after gym?"
            q5 = "\nwhat he eat at dinner?"

            # user message
            print("*****************")
            print("Diet log open...")
            print("*****************")
            print(q1)
            take_meal = input()
            print(q2)
            break_first = input()
            print(q3)
            lunch = input()
            print(q4)
            eve_tiffin = input()
            print(q5)
            dinner = input()

            # Ans
            sr = "\n**SESSION RESTART**"
            srd = "\n**********************"
            a1 = "\nMeal Perday: " + take_meal
            a2 = "\nBreak-first meal: " + break_first
            a3 = "\nlunch meal: " + lunch
            a4 = "\nEvening meal: " + eve_tiffin
            a5 = "\nDinner meal: " + dinner
            update = "\nUpdated at: " + "[" + d + "]"

            # file system to store log data
            f = open("hm3 hamad dlog.txt", "r+")
            f.write(srd)
            f.write(sr)
            f.write(srd)
            f.write(q1)
            f.write(a1)
            f.write(update)
            f.write(q2)
            f.write(a2)
            f.write(update)
            f.write(q3)
            f.write(a3)
            f.write(update)
            f.write(q4)
            f.write(a4)
            f.write(update)
            f.write(q5)
            f.write(a5)
            f.write(update)
            f.close()  # close file
            print("Hamad Diet Log successfully saved!")

        elif(inp5==2):
            hamad_excercise_log(inp5)
        else:
            print("Wrong Input!")







# Hamad excercise log function: 7
def hamad_excercise_log(inp5):
    # rohan excercise log
    if (inp5 == 2):
        # set of question
        q1 = "\nEnter when he go to gym Today?"
        q2 = "\nEnter excercise name he done Today?"

        # user message
        print("******************")
        print("Excercise log open")
        print("******************")
        print(q1)
        gt = input()
        print(q2)
        gn = input()

        # Ans
        sr = "\n**SESSION RESTART**"
        srd = "\n**********************"
        a1 = "\nGym time Today: " + gt
        a2 = "\nBreak-first meal: " + gn
        update = "\nUpdated at: " + "[" + d + "]"

        # file system to store log data
        f = open("he3 hamad elog.txt", "r+")
        f.write(srd)
        f.write(sr)
        f.write(srd)
        f.write(q1)
        f.write(a1)
        f.write(update)
        f.write(q2)
        f.write(a2)
        f.write(update)
        f.close()  # close file
        print("Hamad Excercise Log successfully saved!")




# Retrive controller here
def retrive_log_controller(inp1):
    retrive_log(inp1)


# # Retrive log start here
def retrive_log(inp1):
    if(inp1==2):
        print("What log you want to retrive\n1.Diet log Retrive\n2.Excercise log Retrive")
        print("Enter your choice: ")
        inp6=int(input())
        if(inp6==1):
            diet_retrive_menu(inp6)
        elif(inp6==2):
            excercise_retrive_menu(inp6)
        else:
            print("Wrong input!")



def diet_retrive_menu(inp6):
    if (inp6 == 1):
        print("Whose Diet log you want to retrive?\n1.Harry Diet Log\n2.Rohan Diet Log\n3.Hamad Diet log")
        print("Enter your choice: ")
        inp7 = int(input())
        if(inp7==1):
            harry_diet_retrive(inp7)
        elif(inp7==2):
            rohan_diet_retrive(inp7)
        elif(inp7==3):
            hamad_diet_retrive(inp7)
        else:
            print("wrong input!")



def harry_diet_retrive(inp7):
    # harry diet log data
    if (inp7 == 1):
        print("********************************")
        print("Retrive Data from Harry Diet log")
        print("********************************")
        f = open("hm1 harry dlog.txt", "r")
        data = f.read()
        print(data)
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")



def rohan_diet_retrive(inp7):
    # rohan diet log data
    if (inp7 == 2):
        print("********************************")
        print("Retrive Data from Rohan Diet log")
        print("********************************")
        f = open("hm2 rohan dlog.txt", "r")
        data = f.read()
        print(data)
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")



def hamad_diet_retrive(inp7):
    # hamad diet log data
    if (inp7 == 3):
        print("********************************")
        print("Retrive Data from Hamad Diet log")
        print("********************************")
        f = open("hm3 hamad dlog.txt", "r")
        data = f.read()
        print(data)
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")



def excercise_retrive_menu(inp6):
        if(inp6==2):
            print("Whose Excercise log you want to retrive?\n1.Harry Excercise Log\n2.Rohan Excercise Log\n3.Hamad Excercise log")
            print("Enter your choice: ")
            inp8 = int(input())
            if(inp8==1):
                harry_excercise_retrive(inp8)
            elif(inp8==2):
                rohan_excercise_retrive(inp8)
            elif(inp8==3):
                hamad_excercise_retrive(inp8)
            else:
                print("wrong input!")



def harry_excercise_retrive(inp8):
    if (inp8 == 1):
        print("\n\n**************************************")
        print("Retrive Data from Harry Excercise log")
        print("**************************************")
        f = open("he1 harry elog.txt", "r")
        data = f.read()
        print(data)
        f.close()#close file
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")




def rohan_excercise_retrive(inp8):
    if (inp8 == 2):
        print("\n\n**************************************")
        print("Retrive Data from Rohan Excercise log")
        print("**************************************")
        f = open("he2 rohan elog.txt", "r")
        data = f.read()
        print(data)
        f.close()#close file
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")




def hamad_excercise_retrive(inp8):
    if (inp8 == 3):
        print("\n\n**************************************")
        print("Retrive Data from Hamad Excercise log")
        print("**************************************")
        f = open("he3 hamad elog.txt", "r")
        data = f.read()
        print(data)
        f.close()#close file
        print("\n\n*************************************")
        print("Data retrive status: Successfully done!")
        print("***************************************")




# Program start from here
print("************************************")
print("WELCOME TO 'HEALTH MANAGMENT SYSTEM'")
print("BY: RICK SAHA")
print("Language used: 'PYTHON'")
print("************************************")
print("\nWhat you want to do?\n1.Diet log\n2.Retrive log")
print("Enter your choice: ")
inp0=int(input())
inp1=inp0
if(inp1==1):
    main_input(inp1)
elif(inp1==2):
    retrive_log_controller(inp1)
else:
    print("wrong input!")





# ***************
# DESCRIPTION:  *
# ****************************************************************************************************
# 'Health managment system' project workflow describe here
# I used here 7 function for data save in file and also data retrive from file

# All function name here:
#1. def main_input()
#2. def harry_Diet_log():
#3. def harry_excercise_log():
#4. def rohan_Diet_log():
#5. def rohan_excercise_log():
#6. def hamad_Diet_log():
#7. def hamad_excercise_log():
#8. def harry_diet_retrive()
#9. def rohan_diet_retrive()
#10. def hamad_diet_retrive()
#11.def harry_excercise_retrive()
#12.def rohan_excercise_retrive()
#13.def hamad_excercise_retrive()


# I used all this function to partion my code and highly taken care about clean code so any other
# programmer eaisly understand my code

#project developed By Rick saha
