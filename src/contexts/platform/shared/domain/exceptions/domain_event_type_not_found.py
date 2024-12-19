class DomainEventTypeNotFound(Exception):
    def __init__(self, name: str) -> None:
        message = f"Event type {name} not found among subscriber."
        super().__init__(message)
