# This file is an enhanced version of main.py that uses OOPS

# Constant values
DEVICE_OPTIONS = {'1': 'LAPTOP', '2': 'ANDROID', '3': 'IOS'}
JOB_OPTIONS = {'1': 'Student', '2': 'Software Developer', '3': 'Business Person', '4': 'Data Scientist','5': 'Common person (Beginner knowledge of Tech)'}
SCHOOL_OPTIONS = {
    '1': 'Primary', '2': 'Junior School', '3': 'Middle School', '4': 'Junior High School', '5': 'Senior High School'}
SDE_OPTIONS = {'1': 'SDE 1', '2' : 'SDE 2', '3': 'SDE 3'}
BUSINESS_OPTIONS = {'1': 'Manufacturing', '2': 'Service', '3': 'Merchandising', '4': 'Hybrid'}
DEVICES = 3
JOBS = 5
SCHOOLS = 5
SOFTWARE_DEVELOPERS = 3

# Main Input Handling class
class Input():
    def __init__(self):
        #self.seq = 0
        self.deviceInput = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option.\n"))
        self.deviceInput = self.input_device(self.deviceInput, DEVICES)
        self.device = DEVICE_OPTIONS.get(str(self.deviceInput))
        self.professionInput = int(input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \nType number of option.\n"))
        self.professionInput = self.input_profession(self.professionInput, JOBS)
        self.profession = JOB_OPTIONS.get(str(self.professionInput))
        self.professionSubType = self.input_professionType(self.profession)

    def input_device (self, deviceInput, DEVICES):
        #self.seq = 1
        if deviceInput > DEVICES or deviceInput <= 0:
            print("Choice not found. You would have to retry.")
            deviceInput = int(input("What type of device do you want? \n Choose one from the following: \n 1. LAPTOP \n 2. ANDROID \
        \n 3. IOS \n Type numbers for selecting the option.\n"))
            deviceInput = self.input_device(deviceInput, DEVICES)
        return deviceInput

    def input_profession (self, professionInput, JOBS):
        #self.seq = 2
        if professionInput > JOBS or professionInput <= 0:
            print("Choice not found. You would have to retry.")
            professionInput = int(input("What is your profession? \n Choose one from the following: \n 1. Student \n 2. Software Developer \n 3. Business Person \
        \n 4. Data Scientist \n 5. Common person (Beginner knowledge of Tech) \nType number of option.\n"))
            professionInput = self.input_profession(professionInput, JOBS)
        return professionInput

    def input_professionType (self, profession):
        #self.seq = 3
        if profession == 'Student':
            #studentType = ""
            professionSubType = int(input("What kind of school? \n Choose one from the following: \n 1. Primary/Pre-Primary (Pre-Nursery, Nursery, Kindergarten, Grade 1 & Grade 2) \
             \n 2. Junior School (Grade 3 to Grade 5)\n 3. Middle School (Grade 6 to Grade 8) \
              \n 4. Junior High School (Grade 9 to Grade 10) \n 5. Senior High School (Grade 11 to Grade 12) \
              \n Choose a number from the given options.\n"))
            if professionSubType > SCHOOLS or professionSubType <= 0:
                print("Choice not found. You would have to retry.")
                professionSubType = self.input_professionType(self.profession)
                studentType = professionSubType
                return studentType
            else:
                studentType = SCHOOL_OPTIONS.get(str(professionSubType))
                return studentType
            
        if profession == 'Software Developer':
            professionSubType = int(input("Please mention the tier of of your Software Development. \n Choose one from the following: \n 1. Tier 1\
                \n 2. Tier 2 \n 3. Tier 3 \n Write number to select option."))
            if professionSubType > SOFTWARE_DEVELOPERS or professionSubType <= 0:
                print("Choice not found. You would have to retry.")
                professionSubType = self.input_professionType(self.profession)
                SDEType = professionSubType
                return SDEType
            else:
                SDEType = SDE_OPTIONS.get(str(professionSubType))
                return SDEType
    
    def output (self):
        return(str("{} has been queried & the user is a {}".format(self.device, self.profession)))

"""class DeviceSelector(Input):
    def __init__(self):
        Input.__init__(self)
        self.deviceType = self.device
        self.profession = self.profession
        self.successMsg = self.success_msg()
    
    def success_msg(self):
        return (("{} has been selected.\nUser is a {}.").format(self.deviceType, self.profession))
"""    
class Student(Input):
    Student_response = []

    def __init__(self, professionSubType, profession):
        self.StudentType = professionSubType

    def mainStudent(self, StudentType):
        if StudentType == 'Primary':
            print("{} has been selected.".format(self.StudentType))
            self.Student_response.append(self.primary_quiz('Student'))

        elif StudentType == 'Junior School':
            print("{} has been selected.".format(self.StudentType))
            self.Student_response.append(self.juniorSchool_quiz('Junior School'))

        elif StudentType == 'Middle School':
            print("{} has been selected.".format(self.StudentType))
            self.Student_response.append(self.middleSchool_quiz('Middle School'))
        
        elif StudentType == 'Junior High School':
            print("{} has been selected.".format(self.StudentType))
            self.Student_response.append(self.juniorHighSchool_quiz('Junior High School'))

        elif StudentType == 'Senior High School':
            print("{} has been selected.".format(self.StudentType))
            self.Student_response.append(self.seniorHighSchool_quiz('Senior High School'))

        return self.Student_response

    def primary_quiz(self, StudentType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        primary_response = (ques1, ques2, ques3, ques4, ques5)
        return primary_response

    def juniorSchool_quiz(self, StudentType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        junior_response = (ques1, ques2, ques3, ques4, ques5)
        return junior_response

    def middleSchool_quiz(self, StudentType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        middle_response = (ques1, ques2, ques3, ques4, ques5)
        return middle_response

    def juniorHighSchool_quiz(self, StudentType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        juniorHigh_response = (ques1, ques2, ques3, ques4, ques5)
        return juniorHigh_response

    def seniorHighSchool_quiz(self, StudentType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        seniorHigh_response = (ques1, ques2, ques3, ques4, ques5)
        return seniorHigh_response

class SoftwareDevloper(Input):
    SDE_response = []

    def __init__(self, professionSubType, profession):
        self.SDEType = professionSubType

    def mainSDE(self, SDEType):
        if SDEType == 'SDE 1':
            print("{} has been selected.".format(self.SDEType))
            self.SDE_response.append(self.SDE1_quiz('SDE 1'))

        elif SDEType == 'SDE 2':
            print("{} has been selected.".format(self.SDEType))
            self.SDE_response.append(self.SDE2_quiz('SDE 2'))

        elif SDEType == 'SDE 3':
            print("{} has been selected.".format(self.SDEType))
            self.SDE_response.append(self.SDE2_quiz('SDE 2'))
        
        return self.SDE_response

    def SDE1_quiz(self, SDEType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        SDE1_response = (ques1, ques2, ques3, ques4, ques5)
        return SDE1_response

    def SDE2_quiz(self, SDEType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        SDE2_response = (ques1, ques2, ques3, ques4, ques5)
        return SDE2_response

    def SDE3_quiz(self, SDEType):
        ques1 = input("")
        ques2 = input("")
        ques3 = input("")
        ques4 = input("")
        ques5 = input("")
        SDE3_response = (ques1, ques2, ques3, ques4, ques5)
        return SDE3_response

#obj = DeviceSelector() # Class for debugging
obj = Input()
job = obj.profession
deviceinp = obj.device
jobType = obj.professionSubType
print(job)
print(jobType)
print(obj.output())
if obj.profession == 'Student':
    studentA = Student(jobType, job)
    print(studentA.mainStudent(jobType))

elif obj.profession == 'Software Developer':
    softwareDevA = SoftwareDevloper(jobType, job) 
    print(softwareDevA.mainSDE(jobType))


