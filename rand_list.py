import random

def random_list(limit):
    if limit < 0:
        return None
    return random.sample(range(0, 100), limit)

print(random_list(-1))