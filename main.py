from fitness_app import *
from activity import *
from workout_plans import *
newUser = None



def createCustomPlans():
    exercises = []
    planName = input("enter plan name : ")
    print("add exercises...press S when done adding.")
    while True:
        exc = input()
        if exc == "s":
            break
        else:
            exercises.append(exc)
    custom_plan = Workout_plan(planName,exercises)
    return custom_plan

        

def workOutPlans():
    while True:
        print("\n1. predefined plans")
        print("2. custom plans")
        print("3. create custom plan")
        print("4. Exit to main menu\n")

        choice = int(input("enter your choice : "))

        match choice:
            case 1:
                print("\npre defined plans\n")
                print("Plan Name : ",predefined_plan_1.work_out_name)
                print("Exercises : ")
                for exercise in predefined_plan_1.exercises:
                    print(exercise)
                print("\nPlan Name : ",predefined_plan_2.work_out_name)
                print("Exercises : ")
                for exercise in predefined_plan_2.exercises:
                    print(exercise)
                print("\nPlan Name : ",predefined_plan_3.work_out_name)
                print("Exercises : ")
                for exercise in predefined_plan_3.exercises:
                    print(exercise)
            case 2:
                if newUser.customPlans is not None:
                    print("\nCustom plans\n")
                    for plan in newUser.customPlans:
                        print("Plan Name : ",plan.work_out_name)
                        print("Exercises : ")
                        for exc in plan.exercises:
                            print(exc)
                else:
                    print("No plans found. create one to view")
            case 3:
                plan = createCustomPlans()
                newUser.customPlans.append(plan)
            case 4:
                break



while True:
    print("\n1. register")
    print("2. login")
    print("3. view profile")
    print("4. record activities")
    print("5. Track activities")
    print("6. Workout plans")
    print("7. Set goals")
    print("8. connect with friends")
    print("9. Exit\n")

    choice = int(input("\n enter your choice : "))

    match choice:
        case 1:
            name = input("enter your name : ")
            password = input("create password : ")
            age = int(input("enter your age : "))
            weight = float(input("enter your weight(kgs) "))
            height = float(input("enter your height(cms) "))

            newUser = User(name,password,age,weight,height)
            newUser.register()
        case 2:
            if newUser is not None:
                userName = input("enter user name : ")
                password = input("enter password : ")
                newUser.login(userName,password)
            else:
                print("register first")
        case 3:
            if newUser is not None:
               newUser.show_profile()
            else:
                print("register first")
        case 4:
            if newUser is not None:
                if newUser.isLoggedIn:
                    activityType = input("enter activity type:")
                    duration = float(input("enter duration(minutes):"))
                    distance = float(input("enter distance(km):"))
                    heart_rate = input("enter heart rate(optional):")
                    if heart_rate.strip():
                        heart_rate = float(heart_rate)
                    else:
                        heart_rate = None
                    newActivity = Activity(activityType,duration,distance,heart_rate)
                    newUser.track_activity(newActivity)
                    print("Activity recorded successfully")
                else:
                    print("please login to record an activity")
            else:
                print("register first")

        case 5:
            if newUser is not None:
                if newUser.isLoggedIn:
                    if newActivity is not None:
                       print("---------------------------------- ACTIVITIES-----------------------------------\n")
                       print("Activity Type          Duration         Distance         Pace          Heart Rate")
                       for activity in newUser.activity_log:
                          
                           print(f"{activity.activity_type}                {activity.duration}              {activity.distance}          {activity.pace:.2f}               {activity.heart_rate}")
                    else:
                        print("Record activity to track activities")
                else:
                    print("Log in to track activities")
            else:
                print("First create account")
        case 6:
            if newUser is not None:
                if newUser.isLoggedIn:
                    workOutPlans()
                else:
                    print("Log in to access workout plans")
            else:
                print("First create account")
        case 9:
            break