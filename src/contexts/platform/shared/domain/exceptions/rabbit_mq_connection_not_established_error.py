class RabbitMqConnectionNotEstablishedError(Exception):
    def __init__(self) -> None:
        message = "RabbitMq connection not established. Unable to publish events."
        super().__init__(message)
