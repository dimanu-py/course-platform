class InvalidEmailFormatError(Exception):
    def __init__(self, value: str) -> None:
        message = f"Invalid email format: {value}"
        super().__init__(message)
