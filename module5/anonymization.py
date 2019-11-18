"""Anonymize data with Faker"""

#%%
from pprint import pprint
from faker import Faker
from faker.providers import internet

fake = Faker()
print(fake.name())

#%%
print(fake.address())

#%%
fake_fr = Faker('fr_FR')
for _ in range(10):
    print(fake_fr.name())

#%%
fake_nl = Faker('nl_NL')
for _ in range(10):
    print(fake_nl.name())

#%%
fake.add_provider(internet)
print(fake.ipv4_public())

#%%
profile = fake.simple_profile()
pprint(profile)
