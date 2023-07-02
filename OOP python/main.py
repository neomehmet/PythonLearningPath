import json
import hashlib

class User:
    def __init__(self, name, password=None, phone=None):
        data = self.load()
        self.user_name = name
        self.password = ""
        self.phone = ""
        self.load()
        
        if name in data:
            self.password = data[name]["password"]
            self.phone = data[name]["phone"]

        if password is not None:
            self.password = hashlib.md5(password.encode()).hexdigest()
        print("User created", self.user_name)

        if phone is not None:
            self.phone = phone

    def __del__(self):
        print("User deleted")
    
    def verify(self, password):
        if self.password == hashlib.md5(password.encode()).hexdigest():
            print("User verified")
            return True
        else:
            print("Wrong password")
            return False
    def save(self):
        data = self.load()
        data[self.user_name] = {"password": self.password,
                                "phone": self.phone}
        with open("data.json", "w") as f:
            f.write(json.dumps(data, indent=2))            

    def load(self):
        data = {}
        with open("data.json", "a+") as f:
            try:
                f.seek(0)
                data = json.load(f)
            except:
                data = {}
        return data


def main():
    mehmet = User("mehmet","1234")
    mehmet.save()
    burak = User("burak","1256", "12345678")
    burak.save()
    print(mehmet.verify("1234"))
    emir = User("emir","5678")
    emir.save()
main()