# This is the start of the main file of the repository. Happy coding :)
choice_dict = {}
#device_type = int()
success_msg = str()
choice_dict = {'1': 'LAPTOP', '2': 'ANDROID', '3': 'IOS'}
student_choice_dict = {
    '1': 'Primary/Pre-Primary (Pre-Nursery, Nursery, Kindergarten, Grade 1 & Grade 2)', '2': 'Junior School (Grade 3 to Grade 5)', '3': 'Middle School (Grade 6 to Grade 8)', '4': 'Junior High School (Grade 9 to Grade 10)', '5': 'Senior High School (Grade 11 to Grade 12)'}

profession_choice_dict = {'1':'Student','2':'Software Developer','3':'Business Person','4':'Data Scientist',\
                          '5': 'Common person (Beginner knowledge of Tech)'}

def end_msg(response):
    if response.lower() == 'y':
        Select_DeviceType()
    elif response.lower() == 'n':
        print("Thankyou for using. Exiting now!!")
        exit()
    else:
        print('Press "y" to retry & "n" to exit.\n')
        response = input()
        end_msg(response)

def Select_DeviceType ():
    device_type = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option. \n"))
    #choice = 0
    success_msg = "has been selected."
    if device_type > 3:
        print("Choice not found. Press 'y' to retry & 'n' to exit.\n")
        response = input()
        end_msg(response)
    else:
        print("{} {}".format(choice_dict.get(str(device_type)), success_msg))
    return "LAPTOP"
            
def intro_ques():
    response = input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \n")
    #response = int(input())
    if response == "1":
        print("Student it is.")
        student_school_ques()
    elif int(response) > 5:
        print("Okie Dokie!!")
        yes_no = input("Do you want to continue? YES or NO \n").upper()
        if yes_no == "YES":
            intro_ques()
        else:
            end_msg('n')
    return response

def student_school_ques():
    ques_1 = "Are you in school or in college?"
    print(ques_1)
    validate = input().upper()
    if validate == "SCHOOL":
        print("Hola school kid!")
        print("What kind of school? \n Choose one from the following: \n 1. Primary/Pre-Primary (Pre-Nursery, Nursery, Kindergarten, Grade 1 & Grade 2) \
             \n 2. Junior School (Grade 3 to Grade 5)\n 3. Middle School (Grade 6 to Grade 8) \
              \n 4. Junior High School (Grade 9 to Grade 10) \n 5. Senior High School (Grade 11 to Grade 12) \
              \n Choose a number from the given options.")
        choice = int(input())
        if choice == 1:
            print("{} has been selected.".format(student_choice_dict.get(str(choice))))
        elif choice == 2:
            print("{} has been selected.".format(student_choice_dict.get(str(choice))))
        elif choice == 3:
            print("{} has been selected.".format(student_choice_dict.get(str(choice))))
        elif choice == 4:
            print("{} has been selected.".format(student_choice_dict.get(str(choice))))
        elif choice == 5:
            print("{} has been selected.".format(student_choice_dict.get(str(choice))))
        elif choice > 5:
            print("Okie Dokie!!")
            yes_no = input("Do you want to continue? YES or NO \n").upper()
            if yes_no == "YES":
                intro_ques()
            else:
                end_msg('n')
    elif validate == "COLLEGE":
        print("Hola college kid!")
    else:
        yes_no = input("I'm afraid your response is incorrect. Do you want to continue? YES or NO \n").upper()
        if yes_no == "YES":
            student_school_ques()
        elif yes_no == "NO":
            intro_ques()

#def student_college_ques():


def main():
    device_selected = Select_DeviceType()
    if device_selected == "LAPTOP":
        profession = intro_ques()
        if profession == 1:
            student_school_ques()

main()



