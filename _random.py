import random

result = dir(random)

result = random.random() # 0.0 - 1.0

result = int(random.uniform(1,10))

result = random.randint(1,100)

names = ['ali','yağmur','deniz','cenk']

result = names[random.randint(0,len(names) -1)]

result = random.choice(names)

liste = list(range(10))

random.shuffle(liste)

result = liste

liste = range(100)

result = random.sample(liste,3)

print(result)