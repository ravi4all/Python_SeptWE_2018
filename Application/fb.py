users = []

def loginSuccess():
    print("""
    1. Post
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

def post():
    pass

def viewProfile():
    pass

def updateProfile():
    pass

def deleteProfile():
    pass

def register():
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

def login():
    pass

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
