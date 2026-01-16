class User:
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return f"{self.username}"
        
class Message:
    def __init__(self, sender, body):
        self.sender = sender
        self.body = body

class ChatRoom:
    def __init__(self, roomName):
        self.roomName = roomName
        self.users = {} # username:userObject
        self.__messages = [] # Private History
        
    def joinRoom(self, userObject):
        self.users[userObject.username] = userObject
        print(f"{userObject.username} Joined {self.roomName} !")
        
    def exitRoom(self, userObject):
        try:
            del self.users[userObject.username]
            print(f"{userObject.username} Left {self.roomName} !")
        except:
            return f"{userObject.username} is already Not a member of {self.roomName} !"
        
    def postMessage(self, userObject, msg):
        if userObject.username in self.users.keys():
            self.__messages.append(msg)
            print(f"{msg.body} ------ sent by {userObject.username}")
        else:
            print(f"Sorry {userObject.username} ! You don't not have access to {self.roomName}. Pleae join {self.roomName} to send messages here.")
    
    def chatRoomHistory(self):
        print(f"----- History of messages sent to {self.roomName} -----")
        for msg in self.__messages:
            print(f"{msg.body} --------- by {msg.sender}")
            

# Creating Users
sonu = User("Sonu")
shanu = User("Shanu")
ma = User("Paramita")

# Creating 2 Chat rooms
fashion_room = ChatRoom("Fashion For Dummies")
cook_room = ChatRoom("Cooking for Non-cooks")

# Joining Rooms
fashion_room.joinRoom(sonu)
fashion_room.joinRoom(shanu)
fashion_room.joinRoom(ma)

cook_room.joinRoom(shanu)
cook_room.joinRoom(ma)

# Events in fashion_room
fashion_room.postMessage(sonu, Message(sonu, "Hello, I don't know anything about fashion !"))
fashion_room.postMessage(shanu, Message(shanu, "I know that Dude !"))
fashion_room.postMessage(ma, Message(ma, "Shanu oke sikhiye de ektu ! O kichui janena !"))
fashion_room.exitRoom(sonu)
fashion_room.chatRoomHistory()

print("\n\n\n\n")

# Events in cook room
cook_room.postMessage(sonu, Message(sonu, "I am a Pro cook !"))
cook_room.postMessage(shanu, Message(shanu, "I cook like hell !"))
cook_room.postMessage(ma, Message(ma, "Ami sikhiye debo, dara leave kore abar join korchi !"))
cook_room.exitRoom(ma)
cook_room.exitRoom(sonu)
cook_room.joinRoom(ma)
cook_room.chatRoomHistory()
cook_room.postMessage(ma, Message(ma, "Chinta korisna sikhiye debo...Let's cook then !"))
cook_room.chatRoomHistory()