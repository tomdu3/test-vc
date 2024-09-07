import random
import cowsay

def random_list(limit):
    if limit < 0:
        return None
    return random.sample(range(0, 100), limit)


cowsay.cow("Random List Generator")

print(random_list(-1))

print(random_list(10))