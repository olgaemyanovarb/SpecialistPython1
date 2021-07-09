import random
random_list = [random.randint(-100,100) for i in range(int(input(">>")))]
new_random_list = []
print(random_list)
for i in random_list:
    if i % 2 == 0:
        new_random_list.append(int(i))
print(new_random_list)
