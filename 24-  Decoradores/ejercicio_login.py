from decorators import authenticate_class, validate_password

@authenticate_class
class User:
    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password

    def say_hello(self):
        print(f"Hi {self.user_name}, welcome to our system!")

    @validate_password
    def show_password(self):
        print(f"Hi {self.user_name}, your password starts by: \n {self.password[0:4]}{len(self.password[4:]) * '*'}")



if __name__ == "__main__":
    my_class = User("pablo","pablo123")
    my_class.say_hello()
    my_class.show_password()
