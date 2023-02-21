import random as r

types = ['old', 'fat', 'short']

what_do = r.randint(0, len(types))

word = input('type: ')

fin = 'yo mama so {0} shes as {0} as {1}'.format(types[what_do], word)

print(fin)
