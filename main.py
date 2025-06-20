
class User:
    def __init__(self, username, password, name):
        self.username = username
        self.__password = password
        self.name = name
    def check_password(self, password):
        return self.__password == password
    def view_profile(self):
        print("\n Profile for {self.username}")
        print("\n Name = {self.name}")
    def update_name(self, newname):
        newname = input("Enter new name: ")
        self.name = newname
        print("Name has been updated successfully")
    def update_pass(self, oldpassword, newpassword):
        if self.check_password(oldpassword):
            self.__password = newpassword
        else:
            print("Incorrect password")

users = {}
def register():
    print("User Registration")
    username = input("Enter a username:").strip().lower()

    if username in users:
        print("This username is already taken.\nPlease try another")
        return
    password = input("Enter a password: ").strip()
    name = input("Enter your name: ")
    
    new_user = User(username,password,name)

    users[username] = new_user
    print("Registered successfully")
def login():
    print("\n User login")
    username = input("Enter your username: ").strip().lower()

    if username not in users:
        print("Username not found")
        return None
    password = input("Enter your password: ")
    user = users[username]

    if user.check_password(password):
        print("Successfull")
        return user
    else:
        print("Incorrect password")
        return None
    
def menu(): # User should not be passed in here in the menu function as your information is not yet available
    
    #user = User() user should not be initialized here as you don't have user date yet
    while True:
        print("Welcome")
        print("1 --> View Profile")    
        print("2 --> Update Profile")    
        print("3 --> Change Password")    
        print("4 --> Log out")

        choice = int(input("Enter your choice from (1-4)"))

        if choice == 1:
            # user information should be available here before you can view it, like username, to fetch the user
            user.view_profile()
        if choice == 2:
            # user information should be available here before you can update it, like username, to fetch the user to update it
            newname = input("Enter your new name: ")
            user.update_name(newname)    
        if choice == 3:
            # user information should be available here before you can update it, like username, to fetch the user to update its password
            old_pass = input("Enter your current password: ")
            new_pass = input("Enter your nre password: ")
            user.update_pass(old_pass,new_pass)
        if choice == 4:
            print("Logging out...")
            break
        else:
            print("Invalid choice")
        
menu()