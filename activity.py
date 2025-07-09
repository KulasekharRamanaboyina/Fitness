class Activity():
    def __init__(self,activity_type,duration,distance,heart_rate):
        self.activity_type = activity_type
        self.duration = duration
        self.distance = distance
        self.pace = duration / distance
        self.heart_rate = heart_rate