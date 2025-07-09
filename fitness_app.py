users = {}


class User():
    def __init__(self,userName,password,age,weight,height):
        self.userName = userName
        self.password = password
        self.age = age
        self.weight = weight
        self.height = height
        self.fitnessGoals = None
        self.isLoggedIn = False
        self.activity_log = []
        self.customPlans = []

    def track_activity(self, newActivity):
        self.activity_log.append(newActivity)
        
    def register(self):
            users['user_name'] = self.userName


            
            print(f"\naccount is created for {self.userName}")

    def login(self,userName,password):
        if userName in users["user_name"]:
            if self.password == password:
                print("authentication successfull")
                self.isLoggedIn = True
            else:
                print("password not matched")
        else:
            print("user not found.create account before login")
    def show_profile(self):
        if self.isLoggedIn:
            print("\n----------- PROFILE ------------")
            print("\nUser Name : ", self.userName)
            print("Age : ", self.age)
            print("Weight : ", self.weight)
            print("Height : ", self.height)
            print("--------------- * --------------\n")
        else:
            print("login to view profile")
  