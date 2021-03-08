# This file is an enhanced version of main.py that uses OOPS

# Constant values
DEVICE_OPTIONS = {'1': 'LAPTOP', '2': 'ANDROID', '3': 'IOS'}
JOB_OPTIONS = {'1': 'Student', '2': 'Software Developer', '3': 'Business Person', '4': 'Data Scientist','5': 'Common person (Beginner knowledge of Tech)'}
SCHOOL_OPTIONS = {
    '1': 'Primary', '2': 'Junior School', '3': 'Middle School', '4': 'Junior High School', '5': 'Senior High School'}
DEVICES = 3
JOBS = 5

# Main Device Selection class
class DeviceSelector:
    def __init__(self, deviceType, profession):
        self.deviceType = deviceType
        self.profession = profession
    
    def success_msg(self):
        print("{} has been selected.".format(self.deviceType))
        print("User is a {}".format(self.profession))
        return self.profession

class Laptop(DeviceSelector):
    def __init__(self,profession):
        self.deviceType = 'LAPTOP'
        self.profession = profession
        DeviceSelector.__init__(self, self.deviceType, self.profession)

class Android(DeviceSelector):
    def __init__(self, profession):
        self.deviceType = 'ANDROID'
        self.profession = profession
        DeviceSelector.__init__(self, self.deviceType, self.profession)

class Ios(DeviceSelector):
    def __init__(self, profession):
        self.deviceType = 'IOS'
        self.profession = profession
        DeviceSelector.__init__(self, self.deviceType, self.profession)
    
class Student(Laptop, Android, Ios):
    def __init__(self, studentType, deviceType):
        self.studentType = SCHOOL_OPTIONS.get(str(int(input("What kind of school? \n Choose one from the following: \n 1. Primary/Pre-Primary (Pre-Nursery, Nursery, Kindergarten, Grade 1 & Grade 2) \
             \n 2. Junior School (Grade 3 to Grade 5)\n 3. Middle School (Grade 6 to Grade 8) \
              \n 4. Junior High School (Grade 9 to Grade 10) \n 5. Senior High School (Grade 11 to Grade 12) \
              \n Choose a number from the given options."))))
        self.deviceType = deviceType
        if self.deviceType == "LAPTOP":
            Laptop.__init__(self, 'Student')
        elif self.deviceType == "ANDROID":
            Android.__init__(self, 'Student')
        elif self.deviceType == "IOS":
            Ios.__init__(self, 'Student')
    
    def student_type(self):
        return self.studentType

class Primary(Student):
    def __init__(self):
        self.studentType = 'Primary'
        Student.__init__(self, self.studentType, self.deviceType)

class JuniorSchool(Student):
    def __init__(self):
        self.studentType = 'Junior School'
        Student.__init__(self, self.studentType, self.deviceType)

class MiddleSchool(Student):
    def __init__(self):
        self.studentType = 'Middle School'
        Student.__init__(self, self.studentType, self.deviceType)

class JuniorHigh(Student):
    def __init__(self):
        self.studentType = 'Junior High School'
        Student.__init__(self, self.studentType, self.deviceType)

class SeniorHigh(Student):
    def __init__(self):
        self.studentType = 'Senior High School'
        Student.__init__(self, self.studentType, self.deviceType)
        

def device_input(): # Taking choice input for selecting device.
    seq = 1
    device_type = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option.\n"))

    if device_type > DEVICES or device_type <= 0:
        print("Choice not found. You would have to retry.")
        device_type = end_msg(seq)
        return device_type
    else:
        return device_type

def profession_input():  # Taking choice input for selecting profession.
    seq = 2
    profession_choice = int(input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \nType number of option.\n"))

    if profession_choice > JOBS or profession_choice <= 0:
        print("Choice not found. You would have to retry.") 
        profession_choice = end_msg(seq)
        return profession_choice
    else:
        return profession_choice

def ask_input(): # Handling all the major inputs
    device_type = device_input()
    profession_choice = profession_input()

    return device_type, profession_choice

def end_msg(seq): # Confirmation end message to handle errors.
    
    if seq == 1:
        end_validation = input("Press 'y' to retry & 'n' to exit.\n").lower()
        if end_validation == 'y' or end_validation == 'yes':
            return device_input()
        elif end_validation == 'n' or end_validation == 'no':
            print("Thankyou for using. Exiting now!!")
            exit()
    elif seq == 2:
        end_validation = input("Press 'y' to retry & 'n' to exit.\n").lower()
        if end_validation == 'y' or end_validation == 'yes':
            return profession_input()
        elif end_validation == 'n' or end_validation == 'no':
            print("Thankyou for using. Exiting now!!")
            exit()

"""def output(job, device):
    if job == "Student" and device == "LAPTOP":
        studentA = Student(job, device)
        print("Hello school kid!")
        print("{} has been selected.".format(studentA.studentType))
"""
# Input and choosing values
"""choices = ask_input()
device_obj = DeviceSelector(DEVICE_OPTIONS.get(str(choices[0])), JOB_OPTIONS.get(str(choices[1])))
job = device_obj.success_msg()
#output(JOB_OPTIONS.get(str(choices[1])), DEVICE_OPTIONS.get(str(choices[0])))
"""


print("Ended!")

class Input():
    def __init__(self):
        self.deviceInput = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option.\n"))
        self.deviceInput = self.input_device(self.deviceInput, DEVICES)
        self.device = DEVICE_OPTIONS.get(str(self.deviceInput))
        self.professionInput = int(input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \nType number of option.\n"))
        self.professionInput = self.input_profession(self.professionInput, JOBS)
        self.profession = JOB_OPTIONS.get(str(self.professionInput))

    def input_device (self, deviceInput, DEVICES):
        if deviceInput > DEVICES or deviceInput <= 0:
            print("Choice not found. You would have to retry.")
            deviceInput = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option.\n"))
            deviceInput = self.input_device(deviceInput, DEVICES)
        return deviceInput

    def input_profession (self, professionInput, JOBS):
        if professionInput > JOBS or professionInput <= 0:
            print("Choice not found. You would have to retry.")
            professionInput = int(input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \nType number of option.\n"))
            professionInput = self.input_profession(professionInput, JOBS)
        return professionInput

    def output (self):
        print("{} has been queried & the user is a {}".format(self.device, self.profession))

obj = Input()
job = obj.profession
deviceinp = obj.device
print(job)
print(deviceinp)