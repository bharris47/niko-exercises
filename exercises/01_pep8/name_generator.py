import random
firstNames =['Bob', 'Alice', 'Frank',  'Ben', 'Niko', 'Vicky', 'Amanda']
lastNames=['Harris', 'Barretto', 'Hansen',   'Smith']

def getRandomName():
    firstName = random.choice(firstNames)
    lastName = random.choice(lastNames)
    return ' '.join([firstName, lastName])

if __name__ == '__main__':
    print(getRandomName())