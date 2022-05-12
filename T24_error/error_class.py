class CustomError(Exception):
    def __init__(self, status_code: int, code: str, type: str, message: str) -> None:
        self.status_code = status_code
        self.code = code
        self.type = type
        self.message = message
