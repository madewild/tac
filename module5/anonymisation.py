"""Anonymise date with Faker"""

#%%
from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

print(fake.name())

#%%
print(fake.address())

#%%
fake_fr = Faker('fr_FR')
for _ in range(10):
    print(fake_fr.name())

#%%
print(fake.ipv4_public())

#%%
