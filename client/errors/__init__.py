class InvalidCredentialsError(Exception):
    def __init__(self):
        self.message = f"{self.__class__.__name__}: Invalid credentials used to access the system."
        super().__init__(self.message)