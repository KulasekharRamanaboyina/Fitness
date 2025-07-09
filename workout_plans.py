class Workout_plan():
    def __init__(self,work_out_name, exercises = []):
        self.work_out_name = work_out_name
        self.exercises = exercises



predefined_plan_1 = Workout_plan("Beginner Full Body Workout",["Squats","push ups", "pull ups"])
predefined_plan_2 = Workout_plan("Intermediate Strength Training Plan",["Squats","push ups", "pull ups"])
predefined_plan_3 = Workout_plan("Lower body focus",["warm up","leg press", "plank"])
