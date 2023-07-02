import json

data = {} 

class User:
    def __init__(self, name, password=None, phone=None):
        self.user_name = name
        self.password = ""
        self.phone = phone
        if password is not None:
            self.password = password
        print("User created", self.user_name)

    def __del__(self):
        print("User deleted")
    
    def verify(self, password):
        if self.password == password:
            print("User verified")
            return True
        else:
            print("Wrong password")
            return False
    def save(self):
        print("User saved")
        data[self.user_name] = {"password": self.password,
                                "phone": self.phone}
        with open("data.json", "w") as f:
            f.write(json.dumps(data, indent=2))            

def main():
    user = User("mehmet",1234)
    user.save()
    print(data)
    user2 = User("emir",5678)
    user2.save()
    print(data)

main()