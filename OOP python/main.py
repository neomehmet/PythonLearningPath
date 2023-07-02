from user import User

def main():
    mehmet = User("mehmet","1234")
    mehmet.save()
    burak = User("burak","1256", "12345678")
    print(mehmet.verify("1234"))
    emir = User("emir","5678")
    emir.save()
main()