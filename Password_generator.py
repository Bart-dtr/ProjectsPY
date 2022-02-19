import random
import string

n_znakow = 8
n_typ = 2

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits

rand_lower = random.sample(lowercase, n_typ)
rand_upper = random.sample(uppercase, n_typ)
rand_punctuation = random.sample(punctuation, n_typ)
rand_digits = random.sample(digits, n_typ)

wszystkie_znaki = rand_lower + rand_upper + rand_punctuation + rand_digits
losowe_znaki = random.sample(wszystkie_znaki, n_znakow)
haslo = ''.join(losowe_znaki)

print()
print(haslo)
print()
