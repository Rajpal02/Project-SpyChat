print "Hello!"
print "Lets Get Started!"

from steganography.steganography import Steganography
from Spy_Details import Spy_Detailss,spy,ChatMessage,Friends,All_Status
from termcolor import colored
from pymsgbox import alert
import os

def send_a_message():
    Friend_choice = select_a_friend()

    original_image = raw_input("What is the name of your original image: ")
    if os.path.isfile(original_image):
        output_image = "output.png"
        text = raw_input("What do you wanna say: ")
        if len(text) == 0:
            print "Text Can't be Empty \n"
        else:
            Steganography.encode(original_image,output_image,text)
            new_chat = ChatMessage(text, True)
            Friends[Friend_choice].chats.append(new_chat)
            print "Your Message Send Successfully \n"
    else:
        print "No such file is present!"

def read_a_message():
    sender = select_a_friend()
    output_image = raw_input("Enter the name of file: ")
#Decoding the hidden text from image
    if os.path.isfile(output_image)==1:
        secret_text = Steganography.decode(output_image)
        print secret_text

#Check for hidden text inside a image
        if len(secret_text) > 0:
            new_chat = ChatMessage(secret_text, False)
            Friends[sender].chats.append(new_chat)
            print new_chat
        else:
            print 'Oops Looks like there is no hidden message encoded'
            exit()
    else:
        print 'No such file present'
        exit()

def read_chat(Spy_name):
    read_for = select_a_friend()
    for chats in Friends[read_for].chats:

        ctime = colored(chats.time.strftime("%d:%B:%Y"), 'blue')
        cspy = colored(Friends[read_for].name, 'red')
        cdfg = colored(Spy_name,'green')
    #According to the message sender the chat message are printed
        if chats.sent_by_me:
                print 'At ['+ctime+']'+ cdfg + ' said: '+chats.message
        else:
                print 'At ['+ctime+']'+ cspy + " said: " + chats.message

    #Check for emergency codes
        if chats.message=="SOS"or "SAVE ME"or "HELP ME":
            alert("I need your help","Emergency")
#End of function


def select_a_friend():
    items = 0
    for friend in Friends:
        print '%d. %s. %s, Age -> %d, Rating -> %.2f ,online -> %s' % (
                                                    items + 1,friend.salutation,friend.name,friend.age,friend.rating,
                                                                friend.online)
        items = items + 1

    friend_choice = raw_input("Choose from your friends: ")
    if len(friend_choice) > 0:
        friend_choice_position = int(friend_choice) - 1
        if friend_choice_position < len(Friends) and friend_choice >= 0:
            print "%s %s is added as a friend." %(Friends[friend_choice_position].salutation,
                                                  Friends[friend_choice_position].name)
        else:
            print"Invalid Input"
            exit()
    else:
        print "Nothing Entered"

    return friend_choice_position

def add_friend(Spy_rating):
    new_name = raw_input("Enter Spy name: ")
    new_salutation = raw_input("Add Salutation (Mr./Mrs.): ")
    new_age = raw_input("Enter age: ")
    new_rating = raw_input("Rating: ")
    new_online = raw_input("Is spy online? (True/False): ")

    if len(new_name) > 0 and len(new_age) > 0 and len(new_rating) > 0:
        if new_name.isalpha() and new_age.isdigit() and not new_rating.isalpha():
            new_age = int(new_age)
            new_rating = float(new_rating)
            new_online = bool(new_online)

            if new_age > 12 and new_rating > Spy_rating:
                dict = Spy_Detailss(new_name,new_salutation,new_age,new_rating,new_online)
                Friends.append(dict)
                print "%s, Age: %d, Rating: %.1f. Friend added" %(new_name, new_age,new_rating)

            else:
                print "We can't add spy as a friend by the details you provided.."
        else:
            print "inappropriate data"
    else:
        print "Some fields are left blank...kindly fill them"

    print "The user has " + str(len(Friends)) + " friends and they are: "
    for i in range(len(Friends)):
        print Friends[i].salutation + ". " + Friends[i].name
    return len(Friends)



#function to add status
def add_status(Status_message):
    if Status_message!=None:
        print "Your current status is: " + Status_message
    else:
        print "You don't have any status"

    ques2 = raw_input("Do you want to select any previously saved status (Y/N): ")
    if ques2.upper() == "N":
        new_status = raw_input("Enter new Status: ")
        if len(new_status) > 0:
            if new_status == Status_message:
                print "It is same as your current status, Enter different status to update!"
                #condition checked by boolean variable
            elif new_status in All_Status == True:
                print "It's there in your status book."
                Status_message = new_status
            else:
                #append() is used to append the variable
                All_Status.append(new_status)
                Status_message = new_status


            Status_message = new_status

        else:
            print "Enter something to update your status."
    else:
        #for loop here to print all possible status present
        for i in range(len(All_Status)):
            print str(i+1) + ". " + All_Status[i]

        num1 = raw_input("Enter the status which you want to update: ")
        if len(num1)>0:
            num1 = int(num1)
            if num1 <= len(All_Status) and num1 > 0:
                if Status_message == All_Status[num1-1]:
                    print "It is already your current status!"
                else:
                    Status_message = All_Status[num1-1]
            else:
                print"Invalid Input"
        else:
            print "Enter number to update your status"
    #returning some value
    return Status_message

#function to represent menu items
def choose_an_option(Spy_name,Spy_age,Spy_rating):
    acti = True
    Status_edit = None
    #while loop until condition is true
    while acti == True:
        print "1) Add a Status Update\n2) Add a friend\n3) Send a secret message\n4) Read a secret message\n" \
              "5) Read chats from a user\n6) Close Application"
        q = raw_input("What you want to do: ")
        if len(q)>0:
            q =int(q)
            #nested if else
            #call functions
            if q == 1:
                Status_edit = add_status(Status_edit)
                print "Your updated is " + Status_edit
            elif q == 2:
                add_friend(Spy_rating)
            elif q == 3:
                send_a_message()
            elif q == 4:
                read_a_message()
            elif q == 5:
                read_chat(Spy_name)
            elif q==6:
                exit()
            else:
                print "Invalid Input"

#Starting project by asking to choose whether to enter details from default spy or enter new details
Ques1 = raw_input("Do you want to continue as " + spy["Salutation"] + " " + spy["Name"] + " (Y/N): ")
#checking for condition if the user has entered anything
if len(Ques1) > 0:
    #condition -flow statement to check for Yes/No condtion
    if Ques1.upper() == "Y":
        #Entering default spy details
        print "%s , age: %d , rating: %.1f; Welcome back!" %(spy["Salutation"] + ". " + spy["Name"],spy["Age"],spy["Rating"])
        choose_an_option(spy["Salutation"] + ". " + spy["Name"],spy["Age"],spy["Rating"])

    else:
        #Entering new details
        #NAME
        Spy_name = raw_input("Enter your name: ")
        if len(Spy_name)>0:
            #checking if first letter of name is Alphabet or not
            if Spy_name[0].isalpha() :
                print  Spy_name + ", Glad to have you!"
                #Input Salutation
                Spy_salutation = raw_input("What should we call you? (Mr/Mrs/Other): ")
                if Spy_salutation.isalpha():
                    Spy_name = Spy_salutation + ". " + Spy_name
                    print "Alright " + Spy_name +  ". We need to know a little bit more about you before we proceed!"

                    #Entering AGE of Spy:
                    Spy_age = raw_input("Enter age: ")
                    #checking normal condition
                    if len(Spy_age) > 0 and Spy_age.isdigit():
                        #converting string to int
                        Spy_age = int(Spy_age)
                        #checking given conditions of SpyAge
                        if Spy_age > 12 and Spy_age < 50:

                            #Entering Spy-Rating
                            Spy_rating = raw_input("Enter Spy Rating: ")
                            #checking basic conditions for Spy-Age
                            if len(Spy_rating) > 0 and not Spy_rating.isalpha():
                                #converting string to float
                                Spy_rating = float(Spy_rating)
                                #Checking given conditions of Spy-Age
                                if Spy_rating > 4.5:
                                    print "You are a great ACE."
                                elif Spy_rating > 3.5 and Spy_rating <= 4.5:
                                    print "You are an above average Spy."
                                elif Spy_rating >= 2.5 and Spy_rating <=3.5:
                                    print "You can perform better."
                                else:
                                    print "You can be helpful in the office."

                                #Entering Online status for Spy
                                Spy_is_ONLINE = raw_input("Is he/she online? (True/False): ")
                                #checking basic condition
                                if len(Spy_is_ONLINE) > 0 and (Spy_is_ONLINE == "True" or Spy_is_ONLINE == "False"):
                                    #converting string to bool
                                    Spy_is_ONLINE = bool(Spy_is_ONLINE)
                                    print "%s , age: %d, Rating: %.1f. Great to have you onboard." %(Spy_name,Spy_age,Spy_rating)
                                    choose_an_option(Spy_name,Spy_age,Spy_rating)

                                else:
                                    print "Enter valid online status!!"
                            else:
                                print "Enter valid Spy_rating!!"
                        else:
                            print "You are not eligible to become a spy!"
                    else:
                        print "Enter valid Age!!"
                else:
                    print "Salutation can only be alphabet"
            else:
                print "Name cannot start with Symbols or numbers! Start with alphabet!"
        else:
            print "Please Enter your name as an IDENTITY to continue!!!! "
else:
    print "Nothing Entered! Please Enter something to continue!"
