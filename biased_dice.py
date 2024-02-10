import random

def biased_die_roll():
    # random number between 1 and 100
    random_number = random.randint(1, 100)

    # if the random number falls within the 40% range for getting a 6
    if random_number <= 40:
        return 6
    else:
        # For the remaining 60% of the time, return a random number from 1 to 5
        return random.randint(1, 5)

# Example usage
lis = []
lis6 = 0
for i in range(99):
    result = biased_die_roll()
    # print("Result of biased die roll:", result)
    lis.append(result)
    if result == 6:
        lis6 += 1
print(lis6)
