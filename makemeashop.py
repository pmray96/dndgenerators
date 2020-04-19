#!/usr/bin/env
import random
import string

f = open('names.txt', 'r')
names = f.readlines()
f.close()

f = open('shops.txt', 'r')
shops = f.readlines()
f.close()

f = open('adjectives.txt', 'r')
adjectives = f.readlines()
f.close()

print(random.choice(adjectives).rstrip('\n') + " " + random.choice(names).rstrip('\n') + " " + random.choice(shops).rstrip('\n'))