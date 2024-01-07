class InvalidCredentialsError(Exception):
    def __init__(self):
        self.message = f"{self.__class__.__name__}: Invalid credentials used to access the system."
        super().__init__(self.message)
        
class AccountCreationError(Exception):
    def __init__(self):
        self.message = f"{self.__class__.__name__} Could not create a users account. \nPlease check the credentials."
        super().__init__(self.message)