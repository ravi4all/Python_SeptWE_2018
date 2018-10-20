import readWrite

users = []

def loginSuccess():
    print("""
    1. Post
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    choice = input("Enter your choice : ")

    operations = {
        "1" : post,
        "2" : viewProfile,
        "3" : updateProfile,
        "4" : deleteProfile,
        "5" : logout
    }

    operations.get(choice)()

def post():
    pass

def viewProfile():
    pass

def updateProfile():
    pass

def deleteProfile():
    pass

def logout():
    pass

def register():
    data = readWrite.read_Data()
    name = input("Enter your name : ")
    flag = True
    while flag:
        email = input("Enter your mailId : ")
        for user in users:
            if email == user['email']:
                print("EmailId Already Exist")
                break
        else:
            flag = False

    pwd = input("Enter your password : ")
    userData = {'name' : name, 'email' : email, 'pwd' : pwd}
    users.append(userData)
    for user in users:
        print(user)

    readWrite.write_Data(users)

def login():
    emailId = input("Enter emailID : ")
    pwd = input("Enter password : ")

    # for user in users:
    #     if user['email'] == emailId and user['pwd'] == pwd:
    #         print("Login Success")
    #         break
    # else:
    #     print("Login Failed")

    for user in users:
        if user['email'] == emailId:
            if user['pwd'] == pwd:
                print("Login Success")
                loginSuccess()
                break
            else:
                print("Invalid Password")
    else:
        print("Login Failed")

def home():
    while True:
        print("""
        1. Login
        2. Register
        """)

        userCh = input("Enter your choice : ")
        operations = {
            "1" : login,
            "2" : register
        }
        operations.get(userCh)()

if __name__ == '__main__':
    home()
