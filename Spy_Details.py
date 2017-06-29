from datetime import datetime
class Spy_Detailss:
    def __init__(self, name, salutation, age, rating, online):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = online
        self.chats = []
        self.current_status_message = None

# Chat Class
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = {
        "Name": "Bond",
        "Salutation": "Mr",
        "Age": 28,
        "Rating": 4.8,
        "is_online": True
    }

# Declaring default friend list
f1 = Spy_Detailss("James","Mr", 30, 4.0,True)
f2 = Spy_Detailss("Raj","Mr", 28, 5.0,False)
f3 = Spy_Detailss("Sam","Mr",45,3.3,True)
Friends=[f1,f2,f3]

# Old Status Messages list
All_Status = ["At Work", "I'm Busy", "At Gym", "Sports", "Hang ON!"]


