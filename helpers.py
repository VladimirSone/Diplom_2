from faker import Faker

fake = Faker(locale='ru_RU')

def random_email():
    email = fake.free_email()
    return email

def random_password():
    password = fake.password(length=10, upper_case=True, lower_case=True)
    return password

def random_username():
    username = fake.first_name()
    return username