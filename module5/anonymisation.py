"""Anonymise date with Faker"""

#%%
from faker import Faker
fake = Faker()

fake.name()

#%%
fake.address()

#%%
fake.text()

#%%
for _ in range(10):
    print(fake.name())
