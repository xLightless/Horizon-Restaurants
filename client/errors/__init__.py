class InvalidCredentialsError(Exception):
    def __init__(self):
        self.message = f"{self.__class__.__name__}: Invalid credentials used to access the system."
        super().__init__(self.message)
        
class AccountCreationError(Exception):
    def __init__(self):
        self.message = f"{self.__class__.__name__} Could not create a users account. \nCheck the credentials correctness."
        super().__init__(self.message)
        
        
class AccountDeletionError(object):
    def __init__(self):
        self.message = f"{self.__class__.__name__} Unable to delete this user. Check for the correct values being entered."