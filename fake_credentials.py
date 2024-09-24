
from faker import Faker

fake = Faker("de_CH")

fake_phone_number = fake.phone_number()
print(fake_phone_number)
fake_email = fake.email()
name = fake.name()
canton = fake.canton()
address = fake.address()
print(fake_email)
profile = fake.profile()

# print(dir(fake))
#
# print(fake_email, name, canton, address,)

print(profile)