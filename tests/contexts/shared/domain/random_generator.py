from faker import Faker


class RandomGenerator:
    faker = Faker()

    @classmethod
    def uuid(cls) -> str:
        return str(cls.faker.uuid4())

    @classmethod
    def word(cls) -> str:
        return cls.faker.word()

    @classmethod
    def sentence(cls) -> str:
        return cls.faker.sentence()
