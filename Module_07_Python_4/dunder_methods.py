class ChatHistory:
    def __init__(self):
        self.messages = []

    # 1. String representation (for users)
    def __str__(self):
        return f"ChatHistory contains {len(self.messages)} messages."

    # 2. Developer representation (for debugging)
    def __repr__(self):
        return f"ChatHistory(messages={self.messages})"

    # 3. Length of the object
    def __len__(self):
        return len(self.messages)

    # 4. Operator Overloading (Merging two histories)
    def __add__(self, other):
        if isinstance(other, ChatHistory):
            combined = ChatHistory()
            combined.messages = self.messages + other.messages
            return combined
        return NotImplemented

    # 5. List-like behavior (Accessing via index)
    def __getitem__(self, index):
        return self.messages[index]

# --- Using the Magic ---
chat1 = ChatHistory()
chat1.messages = ["Hi!", "Hello."]

chat2 = ChatHistory()
chat2.messages = ["How are you?"]

# Triggers __str__
print(chat1) 

# Triggers __len__
print(f"Total count: {len(chat1)}") 

# Triggers __add__
merged_chat = chat1 + chat2 
print(merged_chat.messages)

# Triggers __getitem__
print(f"First message: {merged_chat[0]}")