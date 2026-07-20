class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would like to to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("Signup successful!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found. Please signup first.")
            self.menu()
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == self.username and password == self.password:
                print("Signin successful!")
                self.loggedin = True
                
            else:
                print("Invalid credentials. Please try again.")
        print("\n")
        self.menu()
    
    def write_post(self):
        if self.loggedin:
            post = input("Write your post: ")
            print("Post published!")
        else:
            print("You need to signin first.")
        print("\n")
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend}!")
        else:
            print("You need to signin first.")
        print("\n")
        self.menu()

obj = chatbook()



